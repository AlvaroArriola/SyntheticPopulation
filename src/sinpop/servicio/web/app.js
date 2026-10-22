// España sintética · interfaz (F14, D-075). Sin dependencias salvo Leaflet.
const $ = (s) => document.querySelector(s);
const pct = (x, d = 0) => (x == null ? "—" : (100 * x).toLocaleString("es-ES", { maximumFractionDigits: d, minimumFractionDigits: d }) + " %");
const miles = (n) => (n >= 1e6 ? `${(n / 1e6).toLocaleString("es-ES")} millón` : `${(n / 1e3).toLocaleString("es-ES")} mil`);
const PLANTILLAS = {
  si_no: ["Sí", "No"],
  acuerdo: ["Muy de acuerdo", "De acuerdo", "Ni de acuerdo ni en desacuerdo", "En desacuerdo", "Muy en desacuerdo"],
  valoracion: ["Muy buena", "Buena", "Regular", "Mala", "Muy mala"],
  intensidad: ["Mucho", "Bastante", "Poco", "Nada"],
};
const NSNC = ["N.S.", "N.C."];
const SEQ = ["--seq-1", "--seq-2", "--seq-3", "--seq-4", "--seq-5", "--seq-6", "--seq-7"];

const estado = {
  nivel: "ES",
  territorio: "ES",
  nombre: "España",
  tamano: 1_000_000,
  tamanos: [],
  poblaciones: [],
  opciones: [...PLANTILLAS.valoracion],
  modo: "pregunta",
  paquete: false,
  etiquetas: null,
  resultado: null,
  vista: "total",
  dimension: null,
  opcionMapa: null,
  nivelMapa: "CCAA",
};

// ------------------------------------------------------------------ utilidades
async function api(ruta, opciones) {
  const r = await fetch(ruta, opciones);
  if (!r.ok) {
    let msg = r.statusText;
    try { msg = (await r.json()).detail || msg; } catch (_) { /* respuesta sin JSON */ }
    throw new Error(typeof msg === "string" ? msg : JSON.stringify(msg));
  }
  return r.json();
}
const post = (ruta, cuerpo) => api(ruta, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(cuerpo) });
const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
function escapar(t) { const d = document.createElement("div"); d.textContent = t ?? ""; return d.innerHTML; }

const tooltip = $("#tooltip");
function mostrarTooltip(ev, html) {
  tooltip.innerHTML = html;
  tooltip.hidden = false;
  const x = Math.min(ev.clientX + 14, window.innerWidth - tooltip.offsetWidth - 8);
  const y = Math.min(ev.clientY + 14, window.innerHeight - tooltip.offsetHeight - 8);
  tooltip.style.left = `${x}px`;
  tooltip.style.top = `${y}px`;
}
const ocultarTooltip = () => { tooltip.hidden = true; };

// ------------------------------------------------------------------ mapa
// sin atribución sobre el mapa: el crédito obligatorio de OpenStreetMap va al pie del panel (D-084)
const mapa = L.map("mapa", { zoomControl: true, attributionControl: false, minZoom: 4 }).setView([40.2, -3.6], 6);
const TESELAS = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";
L.tileLayer(TESELAS, { maxZoom: 12 }).addTo(mapa);
// recuadro de Canarias: un segundo mapa fijo, con las islas en su sitio y las mismas capas
const mapaCanarias = L.map("mapa-canarias", {
  zoomControl: false, attributionControl: false, dragging: false, scrollWheelZoom: false,
  doubleClickZoom: false, boxZoom: false, keyboard: false, touchZoom: false, zoomSnap: 0.25,
}).setView([28.4, -15.9], 6);
L.tileLayer(TESELAS, { maxZoom: 12 }).addTo(mapaCanarias);
const CANARIAS = new Set(["CCAA:05", "PROV:35", "PROV:38"]);
const capas = { CCAA: null, PROV: null };
const capasCanarias = { CCAA: null, PROV: null };
const todas = (n) => [capas[n], capasCanarias[n]].filter(Boolean);
function mostrarNivel(nivel) {
  for (const n of ["CCAA", "PROV"]) {
    if (capas[n] && mapa.hasLayer(capas[n])) mapa.removeLayer(capas[n]);
    if (capasCanarias[n] && mapaCanarias.hasLayer(capasCanarias[n])) mapaCanarias.removeLayer(capasCanarias[n]);
  }
  capas[nivel].addTo(mapa);
  capasCanarias[nivel].addTo(mapaCanarias);
}
let geo = null;

function estiloBase(f) {
  const sel = f.properties.territorio === estado.territorio;
  const lista = estado.poblaciones.some((p) => p.territorio === f.properties.territorio && p.lista);
  return {
    color: sel ? css("--acento-fuerte") : css("--acento"),
    weight: sel ? 3 : 1,
    opacity: 0.9,
    fillColor: css("--acento"),
    fillOpacity: sel ? 0.32 : lista ? 0.14 : 0.05,
  };
}

function crearCapa(nivel, soloCanarias = false) {
  return L.geoJSON(geo, {
    filter: (f) => f.properties.nivel === nivel && (!soloCanarias || CANARIAS.has(f.properties.territorio)),
    style: estiloBase,
    onEachFeature: (f, capa) => {
      capa.bindTooltip(() => etiquetaTerritorio(f), { sticky: true, className: "etiqueta-territorio" });
      capa.on({
        mouseover: (e) => e.target.setStyle({ weight: 2.5, fillOpacity: 0.28 }),
        mouseout: () => refrescarEstilos(),
        click: () => elegirTerritorio(f.properties.territorio, f.properties.nombre),
      });
    },
  });
}

function etiquetaTerritorio(f) {
  const p = f.properties;
  const listas = estado.poblaciones.filter((x) => x.territorio === p.territorio && x.lista).map((x) => miles(x.tamano_solicitado));
  let extra = listas.length ? `Listas: ${listas.join(", ")}` : "Sin población generada";
  if (estado.opcionMapa != null && estado.resultado) {
    const v = valorMapa(p);
    if (v != null) extra = `${escapar(estado.resultado.opciones[estado.opcionMapa])}: <b>${pct(v.p)}</b> (confianza ${pct(v.c)})`;
  }
  return `<b>${escapar(p.nombre)}</b><br><span style="color:var(--texto-3)">${extra}</span>`;
}

function refrescarEstilos() {
  for (const n of ["CCAA", "PROV"]) for (const c of todas(n)) c.setStyle(estado.opcionMapa != null && n === estado.nivelMapa ? estiloMapa : estiloBase);
}

function ponerNivel(nivel) {
  estado.nivel = nivel;
  document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === nivel)));
  if (capas.CCAA) mostrarNivel(nivel === "PROV" ? "PROV" : "CCAA");
  if (nivel === "ES") elegirTerritorio("ES", "España");
}
document.querySelectorAll(".niveles button").forEach((b) => b.addEventListener("click", () => ponerNivel(b.dataset.nivel)));

function elegirTerritorio(codigo, nombre) {
  if (estado.nivel === "ES" && codigo !== "ES") {
    estado.nivel = codigo.startsWith("PROV") ? "PROV" : "CCAA";
    document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === estado.nivel)));
  }
  estado.territorio = codigo;
  estado.nombre = nombre;
  $("#territorio-nombre").textContent = nombre;
  if (codigo !== "ES" && estado.tamano === 1_000_000) estado.tamano = 100_000;
  // si el tamaño elegido no está listo y hay otro que sí, se pasa a ese
  const listos = estado.poblaciones.filter((p) => p.territorio === codigo && p.lista && p.semilla === 1);
  if (listos.length && !listos.some((p) => p.tamano_solicitado === estado.tamano)) {
    estado.tamano = Math.max(...listos.map((p) => p.tamano_solicitado));
  }
  pintarTamanos();
  refrescarEstilos();
  asistente();
}

// ------------------------------------------------------------------ poblaciones
function poblacionActual() {
  return estado.poblaciones.find((p) => p.territorio === estado.territorio && p.tamano_solicitado === estado.tamano && p.semilla === 1);
}

function pintarTamanos() {
  const cont = $("#tamanos");
  cont.innerHTML = "";
  for (const t of estado.tamanos) {
    const b = document.createElement("button");
    b.setAttribute("role", "radio");
    b.setAttribute("aria-checked", String(t === estado.tamano));
    b.textContent = miles(t);
    const lista = estado.poblaciones.some((p) => p.territorio === estado.territorio && p.tamano_solicitado === t && p.lista);
    if (lista) { const i = document.createElement("span"); i.className = "punto"; i.title = "Población lista"; b.append(i); }
    b.addEventListener("click", () => { estado.tamano = t; pintarTamanos(); });
    cont.append(b);
  }
  const p = poblacionActual();
  const e = $("#estado-poblacion");
  cargarFidelidad(p?.lista ? p.run_id : null);
  if (p?.lista) {
    e.innerHTML = `<span class="indicador" style="background:var(--bueno)"></span><span>Lista para preguntar · ${p.tamano.toLocaleString("es-ES")} personas sintéticas</span>`;
  } else if (estado.paquete) {
    // el paquete portable no tiene microdatos: solo se consultan las poblaciones que trae
    e.innerHTML = `<span class="indicador" style="background:var(--texto-3)"></span><span>No incluida en el paquete. Elige un tamaño con punto verde; para generar otras hacen falta los datos originales.</span>`;
  } else {
    const minutos = estado.tamano >= 500_000 ? "30-60 minutos" : estado.tamano >= 100_000 ? "unos 10 minutos" : "unos minutos";
    e.innerHTML = `<span class="indicador" style="background:var(--texto-3)"></span><span>${p ? "Le faltan capas" : "Aún no generada"} · tarda ${minutos}</span>`;
    const b = document.createElement("button");
    b.className = "secundario";
    b.textContent = "Generar población";
    b.addEventListener("click", generarPoblacion);
    e.append(b);
  }
  $("#preguntar").disabled = !p?.lista;
}

async function cargarPoblaciones() {
  const r = await api("/api/poblaciones");
  estado.poblaciones = r.poblaciones;
  estado.tamanos = r.tamanos;
  pintarTamanos();
  refrescarEstilos();
}

async function generarPoblacion() {
  try {
    const r = await post("/api/poblaciones", { territorio: estado.territorio, tamano: estado.tamano });
    if (r.trabajo) await seguir(r.trabajo, $("#estado-poblacion"));
    await cargarPoblaciones();
  } catch (e) {
    $("#estado-poblacion").textContent = `No se pudo generar: ${e.message}`;
  }
}

// ------------------------------------------------------------------ trabajos
async function seguir(id, destino) {
  for (;;) {
    const t = await api(`/api/trabajos/${id}`);
    destino.innerHTML = `<span class="girando" aria-hidden="true"></span> ${escapar(t.mensaje)}`;
    if (t.estado === "hecho") { destino.textContent = ""; return t.resultado; }
    if (t.estado === "error") throw new Error(t.mensaje);
    await new Promise((r) => setTimeout(r, 1200));
  }
}

// ------------------------------------------------------------------ pregunta
function pintarOpciones() {
  const cont = $("#opciones");
  cont.innerHTML = "";
  estado.opciones.forEach((o, i) => {
    const c = document.createElement("span");
    c.className = "opcion";
    c.innerHTML = `${escapar(o)} <button type="button" aria-label="Quitar ${escapar(o)}">×</button>`;
    c.querySelector("button").addEventListener("click", () => { estado.opciones.splice(i, 1); pintarOpciones(); });
    cont.append(c);
  });
}
$("#nueva-opcion").addEventListener("keydown", (e) => {
  if (e.key !== "Enter") return;
  e.preventDefault();
  const v = e.target.value.trim();
  if (v && !estado.opciones.includes(v)) { estado.opciones.push(v); pintarOpciones(); }
  e.target.value = "";
});
$("#plantillas").addEventListener("change", (e) => {
  if (PLANTILLAS[e.target.value]) { estado.opciones = [...PLANTILLAS[e.target.value]]; pintarOpciones(); }
  e.target.value = "";
});
document.querySelectorAll(".pestanas button").forEach((b) => b.addEventListener("click", () => {
  estado.modo = b.dataset.modo;
  document.querySelectorAll(".pestanas button").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
  $("#evento-campos").hidden = estado.modo !== "evento";
  $("#preguntar").textContent = estado.modo === "evento" ? "Calcular el efecto del evento" : "Preguntar a la población";
}));

let temporizador = null;
$("#enunciado").addEventListener("input", (e) => {
  clearTimeout(temporizador);
  temporizador = setTimeout(() => buscarParecidas(e.target.value), 450);
});
async function buscarParecidas(texto) {
  const caja = $("#sugerencias");
  if (texto.trim().length < 8) { caja.hidden = true; return; }
  try {
    const r = await api(`/api/banco?q=${encodeURIComponent(texto)}&k=5`);
    const ula = $("#lista-atributos");
    ula.innerHTML = "";
    for (const a of r.atributos || []) {
      const li = document.createElement("li");
      const b = document.createElement("button");
      b.type = "button";
      b.className = "sugerencia-dato";
      b.innerHTML = `${escapar(a.descripcion)}<small>Dato oficial · ${escapar(a.fuente_texto || a.fuente_principal || "")} · ${escapar(a.universo)}</small>`;
      b.addEventListener("click", () => { caja.hidden = true; mostrarAtributo(a.variable); });
      li.append(b);
      ula.append(li);
    }
    $("#grupo-atributos").hidden = !(r.atributos || []).length;
    const ul = $("#lista-sugerencias");
    ul.innerHTML = "";
    for (const q of r.preguntas) {
      const li = document.createElement("li");
      const b = document.createElement("button");
      b.type = "button";
      b.innerHTML = `${escapar(q.enunciado)}<small>CIS · ${q.fecha} · ${escapar(q.opciones.slice(0, 4).join(" / "))}${q.opciones.length > 4 ? " …" : ""}</small>`;
      b.addEventListener("click", () => {
        $("#enunciado").value = q.enunciado;
        estado.opciones = q.opciones
          .filter((o) => !/^N\.?S\.?$|^N\.?C\.?$/i.test(o))
          .map((o) => o.replace(/^\(NO LEER\)\s*/i, ""));
        pintarOpciones();
        caja.hidden = true;
      });
      li.append(b);
      ul.append(li);
    }
    $("#grupo-cis").hidden = r.preguntas.length === 0;
    caja.hidden = r.preguntas.length === 0 && !(r.atributos || []).length;
  } catch (_) { caja.hidden = true; }
}

// ------------------------------------------------------------------ datos de la población (D-077)
const PROCEDENCIA = {
  observada: "tomada del registro censal de la persona",
  emparejada: "copiada de una persona parecida de la encuesta oficial",
  modelada: "predicha con un modelo ajustado a la fuente",
  extrapolada: "asignada fuera del universo de la fuente",
};

async function mostrarAtributo(variable) {
  const p = poblacionActual();
  const msg = $("#trabajo");
  if (!p?.lista) { msg.textContent = "Elige primero una población lista."; return; }
  msg.textContent = "Consultando la población…";
  try {
    const d = await api(`/api/atributos/${encodeURIComponent(variable)}?run_id=${encodeURIComponent(p.run_id)}`);
    msg.textContent = "";
    pintarAtributo(d, p);
    guardarHistorial({ tipo: "dato", titulo: d.descripcion, variable, run_id: p.run_id, territorio: estado.territorio, nombre: estado.nombre });
  } catch (e) {
    msg.textContent = `No se pudo consultar: ${e.message}`;
  }
}

function barrasDato(dist, cats, et) {
  const filas = cats.map((c) => {
    const d = dist[c];
    return `<div class="etiqueta" title="${escapar(et[c] ?? c)}">${escapar(et[c] ?? c)}</div>
      <div class="pista" data-o="${escapar(et[c] ?? c)}" data-p="${d.p}" data-a95="${d.ic95[0]}" data-b95="${d.ic95[1]}">
        <span class="ic80" style="left:${100 * d.ic95[0]}%;width:${100 * (d.ic95[1] - d.ic95[0])}%"></span>
        <span class="barra" style="width:${100 * d.p}%"></span>
      </div>
      <div class="valor">${pct(d.p)}</div>`;
  });
  return `<div class="barras">${filas.join("")}</div>
    <div class="leyenda-barras"><span><i style="background:var(--serie)"></i>Proporción</span><span><i style="background:var(--rango)"></i>Margen de simulación (95 %)</span></div>`;
}

function tablaDato(d, dim) {
  const et = d.etiquetas;
  const cats = d.categorias.filter((c) => c !== "NC" || d.total[c].p >= 0.005);
  const claves = Object.keys(d.por_subgrupo).filter((k) => k.startsWith(dim + "="));
  if (!claves.length) return "<p class='nota'>Sin desglose para esta dimensión.</p>";
  const vals = claves.flatMap((k) => cats.map((c) => d.por_subgrupo[k][c].p));
  const min = Math.min(...vals), max = Math.max(...vals);
  const cab = cats.map((c) => { const o = et[c] ?? c; return `<th scope="col" title="${escapar(o)}">${escapar(o.length > 14 ? o.slice(0, 13) + "…" : o)}</th>`; }).join("");
  const filas = claves.map((k) => {
    const nivel = k.split("=")[1];
    const celdas = cats.map((c) => {
      const x = d.por_subgrupo[k][c];
      const t = max > min ? (x.p - min) / (max - min) : 0.5;
      const i = Math.round(t * (SEQ.length - 1));
      return `<td style="background-color:${colorSecuencial(x.p, min, max)};color:${tintaSobre(i)}"
        data-t="${escapar(nombreNivel(dim, nivel))} · ${escapar(et[c] ?? c)}" data-p="${x.p}" data-a="${x.ic95[0]}" data-b="${x.ic95[1]}">${pct(x.p)}</td>`;
    }).join("");
    return `<tr><th scope="row">${escapar(nombreNivel(dim, nivel))}</th>${celdas}</tr>`;
  });
  return `<div class="tabla-envoltorio" tabindex="0" role="region" aria-label="Tabla por grupos"><table class="tabla-calor dato"><thead><tr><th scope="col"><span class="oculto">Grupo</span></th>${cab}</tr></thead><tbody>${filas.join("")}</tbody></table></div>
    <p class="nota">Color más intenso, mayor proporción. Pasa el ratón por una celda para ver su margen de simulación.</p>`;
}

function pintarAtributo(d, pob) {
  const et = d.etiquetas;
  const cats = d.categorias.filter((c) => c !== "NC" || d.total[c].p >= 0.005);
  // para el coloreado del mapa se reutiliza la forma de un resultado de pregunta
  const opciones = cats.map((c) => et[c] ?? c);
  const conv = (dist) => Object.fromEntries(cats.map((c) => [et[c] ?? c, dist[c]]));
  const porSub = Object.fromEntries(Object.entries(d.por_subgrupo).map(([k, v]) => [k, conv(v)]));
  estado.resultado = { tipo: "dato", opciones, enunciado: d.descripcion, total: conv(d.total), por_subgrupo: porSub,
    confianza: { por_subgrupo: Object.fromEntries(Object.keys(porSub).map((k) => [k, 1])) }, dato: d };
  prepararMapa(estado.resultado);
  const tablaD = (dim) => tablaDato(d, dim);
  const caja = $("#resultado");
  caja.hidden = false;
  const proc = Object.entries(d.procedencia || {}).filter(([, v]) => v > 0).sort((a, b) => b[1] - a[1])
    .map(([k, v]) => `${pct(v)} ${escapar(k)} <span class="nota-inline">(${escapar(PROCEDENCIA[k] || k)})</span>`).join("; ");
  const fuentes = d.fuentes.map((f) => `<li>${escapar(f.nombre)}${f.organismo ? ` (${escapar(f.organismo)})` : ""}${f.variable_original ? ` · variable ${escapar(f.variable_original)}` : ""}</li>`).join("");
  caja.innerHTML = `
    <span class="sello-dato">Dato oficial · se lee de la población, no se estima</span>
    <h3>${escapar(d.descripcion)}</h3>
    <div class="metas"><span>${escapar(estado.nombre)}</span><span>${pob.tamano.toLocaleString("es-ES")} personas</span><span>Universo: ${escapar(d.universo)} (${pct(d.cuota_universo)} de los adultos)</span></div>
    <div id="zona-barras">${barrasDato(d.total, cats, et)}</div>
    <div class="procedencia"><b>De dónde sale.</b> La población sintética está calibrada con las fuentes oficiales; este atributo es ${proc || "—"}. El margen solo recoge el error de simulación: el de la fuente y el del emparejamiento se miden en la validación (reports/fase_06.md y fase_07.md).</div>
    ${seccionRegiones(estado.resultado, pob)}
    ${seccionGrupos(estado.resultado, tablaD)}
    <h4 class="seccion-titulo">Fuentes</h4><ul class="fuentes">${fuentes}</ul>
    <p class="aviso">${escapar(d.aviso)}</p>
    <div class="acciones-resultado"><button class="secundario" id="descargar" type="button">Descargar JSON</button><button class="secundario" id="descargar-csv" type="button">Descargar CSV</button><button class="secundario" id="descargar-pdf" type="button">Informe PDF</button></div>`;
  caja.querySelectorAll(".pista").forEach((el) => {
    el.addEventListener("mousemove", (ev) => mostrarTooltip(ev, `<b>${escapar(el.dataset.o)}</b>: ${pct(+el.dataset.p, 1)}<br>Margen de simulación (95 %): ${pct(+el.dataset.a95, 1)} – ${pct(+el.dataset.b95, 1)}`));
    el.addEventListener("mouseleave", ocultarTooltip);
  });
  const tips = (raiz) => raiz.querySelectorAll(".tabla-calor td").forEach((td) => {
    td.addEventListener("mousemove", (ev) => mostrarTooltip(ev, `<b>${td.dataset.t}</b><br>${pct(+td.dataset.p, 1)} (margen de simulación: ${pct(+td.dataset.a, 1)} – ${pct(+td.dataset.b, 1)})`));
    td.addEventListener("mouseleave", ocultarTooltip);
  });
  tips(caja);
  activarGrupos(tablaD, tips);
  activarRegiones(d.descripcion, opciones);
  $("#descargar").addEventListener("click", () => descargar(`${d.variable}_${pob.run_id}.json`, JSON.stringify(d, null, 1), "application/json"));
  $("#descargar-csv").addEventListener("click", () => descargar(`${d.variable}_${pob.run_id}.csv`, csvDato(d), "text/csv"));
  $("#descargar-pdf").addEventListener("click", () => informePdf("dato", d, { run_id: pob.run_id, tamano: pob.tamano.toLocaleString("es-ES") }));
  pintarMapaResultado();
  caja.scrollIntoView({ behavior: "smooth", block: "start" });
}

function csvDato(d) {
  const filas = [["grupo", "categoria", "proporcion", "margen95_inf", "margen95_sup"]];
  const add = (g, dist) => d.categorias.forEach((c) => filas.push([g, d.etiquetas[c] ?? c, dist[c].p, dist[c].ic95[0], dist[c].ic95[1]]));
  add("total", d.total);
  Object.entries(d.por_subgrupo).forEach(([k, v]) => add(k, v));
  return aCsv(filas);
}

$("#preguntar").addEventListener("click", async () => {
  const enunciado = $("#enunciado").value.trim();
  const p = poblacionActual();
  const msg = $("#trabajo");
  if (enunciado.length < 3) { msg.textContent = "Escribe la pregunta."; return; }
  if (estado.opciones.length < 2) { msg.textContent = "Hacen falta al menos dos opciones."; return; }
  const opciones = [...estado.opciones, ...($("#nsnc").checked ? NSNC.filter((x) => !estado.opciones.includes(x)) : [])];
  const boton = $("#preguntar");
  boton.disabled = true;
  try {
    let r;
    if (estado.modo === "evento") {
      const descripcion = $("#evento-descripcion").value.trim();
      if (descripcion.length < 3) throw new Error("Describe el evento.");
      const t = await post("/api/eventos", { run_id: p.run_id, enunciado, opciones, descripcion, fecha: $("#evento-fecha").value });
      r = await seguir(t.trabajo, msg);
      pintarEvento(r, enunciado, opciones, p);
    } else {
      const t = await post("/api/preguntas", { run_id: p.run_id, enunciado, opciones, subgrupos: estado.etiquetas?.subgrupos_ampliados });
      r = await seguir(t.trabajo, msg);
      pintarResultado(r, enunciado, opciones, p);
      guardarHistorial({ tipo: "pregunta", titulo: enunciado, opciones, r, run_id: p.run_id, territorio: estado.territorio, nombre: estado.nombre });
    }
    actualizarLLM();
  } catch (e) {
    msg.textContent = `No se pudo calcular: ${e.message}`;
  } finally {
    boton.disabled = false;
  }
});

// ------------------------------------------------------------------ resultado
function nombreNivel(dim, valor) {
  const e = estado.etiquetas || {};
  if (dim === "edad_4") return valor === "65+" ? "65 y más" : valor.replace("-", "–") + " años";
  return e[dim]?.[valor] ?? valor;
}

function barras(dist, opciones) {
  const filas = opciones.map((o) => {
    const d = dist[o];
    return `<div class="etiqueta" title="${escapar(o)}">${escapar(o)}</div>
      <div class="pista" data-o="${escapar(o)}" data-p="${d.p}" data-a80="${d.ic80[0]}" data-b80="${d.ic80[1]}" data-a95="${d.ic95[0]}" data-b95="${d.ic95[1]}">
        <span class="ic95" style="left:${100 * d.ic95[0]}%;width:${100 * (d.ic95[1] - d.ic95[0])}%"></span>
        <span class="ic80" style="left:${100 * d.ic80[0]}%;width:${100 * (d.ic80[1] - d.ic80[0])}%"></span>
        <span class="barra" style="width:${100 * d.p}%"></span>
      </div>
      <div class="valor">${pct(d.p)}</div>`;
  });
  return `<div class="barras">${filas.join("")}</div>
    <div class="leyenda-barras"><span><i style="background:var(--serie)"></i>Estimación</span><span><i style="background:var(--rango)"></i>Intervalo del 80 %</span><span><i style="background:var(--texto-3);height:2px"></i>Intervalo del 95 %</span></div>`;
}

function activarTooltipsBarras(raiz) {
  raiz.querySelectorAll(".pista").forEach((el) => {
    el.addEventListener("mousemove", (ev) => mostrarTooltip(ev,
      `<b>${escapar(el.dataset.o)}</b>: ${pct(+el.dataset.p, 1)}<br>IC 80 %: ${pct(+el.dataset.a80, 1)} – ${pct(+el.dataset.b80, 1)}<br>IC 95 %: ${pct(+el.dataset.a95, 1)} – ${pct(+el.dataset.b95, 1)}`));
    el.addEventListener("mouseleave", ocultarTooltip);
  });
}

function colorSecuencial(v, min, max) {
  const t = max > min ? (v - min) / (max - min) : 0.5;
  return css(SEQ[Math.max(0, Math.min(SEQ.length - 1, Math.round(t * (SEQ.length - 1))))]);
}
function tintaSobre(i) { return i >= 4 ? "#fff" : css("--texto"); }

function tablaSubgrupos(r, dim, opciones) {
  const claves = Object.keys(r.por_subgrupo).filter((k) => k.startsWith(dim + "="));
  if (!claves.length) return "<p class='nota'>Sin desglose para esta dimensión.</p>";
  const valores = claves.flatMap((k) => opciones.map((o) => r.por_subgrupo[k][o].p));
  const min = Math.min(...valores), max = Math.max(...valores);
  const cab = opciones.map((o) => `<th scope="col" title="${escapar(o)}">${escapar(o.length > 14 ? o.slice(0, 13) + "…" : o)}</th>`).join("");
  const filas = claves.map((k) => {
    const nivel = k.split("=")[1];
    const conf = r.confianza.por_subgrupo[k];
    const celdas = opciones.map((o) => {
      const d = r.por_subgrupo[k][o];
      const t = max > min ? (d.p - min) / (max - min) : 0.5;
      const i = Math.round(t * (SEQ.length - 1));
      return `<td class="${conf < 0.5 ? "baja" : ""}" style="background-color:${colorSecuencial(d.p, min, max)};color:${tintaSobre(i)}"
        data-t="${escapar(nombreNivel(dim, nivel))} · ${escapar(o)}" data-p="${d.p}" data-a="${d.ic80[0]}" data-b="${d.ic80[1]}" data-c="${conf}">${pct(d.p)}</td>`;
    }).join("");
    return `<tr><th scope="row">${escapar(nombreNivel(dim, nivel))}</th>${celdas}</tr>`;
  });
  return `<div class="tabla-envoltorio" tabindex="0" role="region" aria-label="Tabla por grupos"><table class="tabla-calor"><thead><tr><th scope="col"><span class="oculto">Grupo</span></th>${cab}</tr></thead><tbody>${filas.join("")}</tbody></table></div>
    <p class="nota">Color más intenso, mayor proporción. Las celdas rayadas tienen confianza baja (menos del 50 %): pocos datos para ese grupo.</p>`;
}

function activarTooltipsTabla(raiz) {
  raiz.querySelectorAll(".tabla-calor td").forEach((td) => {
    td.addEventListener("mousemove", (ev) => mostrarTooltip(ev,
      `<b>${td.dataset.t}</b><br>${pct(+td.dataset.p, 1)} (IC 80 %: ${pct(+td.dataset.a, 1)} – ${pct(+td.dataset.b, 1)})<br>Confianza: ${pct(+td.dataset.c)}`));
    td.addEventListener("mouseleave", ocultarTooltip);
  });
}

function pintarResultado(r, enunciado, opciones, pob) {
  estado.resultado = { ...r, opciones, enunciado };
  prepararMapa(estado.resultado);
  const caja = $("#resultado");
  caja.hidden = false;
  const conf = r.confianza.total;
  const llm = r.versiones?.modelo_llm ? `con ${escapar(r.versiones.modelo_llm)}` : "sin modelo de lenguaje";
  const tablaPregunta = (dim) => tablaSubgrupos(r, dim, opciones);
  caja.innerHTML = `
    <h3>${escapar(enunciado)}</h3>
    <div class="metas"><span>${escapar(estado.nombre)}</span><span>${pob.tamano.toLocaleString("es-ES")} personas</span><span>Estimador ${llm}</span></div>
    <div class="conmutador" id="vista" role="group" aria-label="Qué se estima">
      <button aria-pressed="true" data-v="total">Lo que piensa la población</button>
      <button aria-pressed="false" data-v="medicion_cis">Como lo mediría el CIS</button>
    </div>
    <div id="zona-barras">${barras(r.total, opciones)}</div>
    <div class="confianza">
      <span class="numero">${pct(conf)}</span>
      <span class="medidor" role="meter" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(100 * conf)}" aria-label="Confianza"><i style="width:${100 * conf}%"></i></span>
      <p title="${escapar(r.confianza.metodo || "")}">Confianza: probabilidad de que el error total de la distribución sea menor de 10 puntos, según el historial de aciertos del sistema en preguntas parecidas.</p>
    </div>
    ${r.parametros_llm?.justificacion ? `<p class="justificacion">«${escapar(r.parametros_llm.justificacion)}»</p>` : ""}
    ${seccionEvolucion(r, opciones)}
    ${seccionRegiones(estado.resultado, pob)}
    ${seccionGrupos(estado.resultado, tablaPregunta)}
    ${seccionRetratos(r, opciones)}
    ${seccionCruce()}
    ${r.preguntas_similares?.length ? `<p class="seccion-titulo">Se apoya en estas preguntas del CIS</p><ol class="parecidas">${r.preguntas_similares.map((x) => `<li>${escapar(x)}</li>`).join("")}</ol>` : ""}
    <p class="aviso">${escapar(r.aviso)}</p>
    <p class="coste">Coste: ${r.coste.llamadas} llamadas al modelo de lenguaje · ${r.coste.eur.toLocaleString("es-ES", { maximumFractionDigits: 3 })} € · ${Math.round(r.coste.segundos)} s</p>
    <div class="acciones-resultado"><button class="secundario" id="descargar-pdf" type="button">Informe PDF</button><button class="secundario" id="descargar-csv" type="button">Descargar CSV</button><button class="secundario" id="descargar" type="button">Descargar JSON</button></div>`;
  activarTooltipsBarras(caja);
  activarTooltipsTabla(caja);
  caja.querySelectorAll("#vista button").forEach((b) => b.addEventListener("click", () => {
    caja.querySelectorAll("#vista button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    $("#zona-barras").innerHTML = barras(r[b.dataset.v], opciones);
    activarTooltipsBarras($("#zona-barras"));
  }));
  activarGrupos(tablaPregunta, activarTooltipsTabla);
  activarRegiones(enunciado, opciones);
  activarEvolucion(caja);
  activarRetratos(r, opciones);
  activarCruce(enunciado, opciones, pob);
  $("#descargar").addEventListener("click", () => descargar(`${r.id}.json`, JSON.stringify(r, null, 1), "application/json"));
  $("#descargar-csv").addEventListener("click", () => descargar(`${r.id}.csv`, csvPregunta(r), "text/csv"));
  $("#descargar-pdf").addEventListener("click", () => informePdf("pregunta", r, { enunciado, run_id: pob.run_id, tamano: pob.tamano.toLocaleString("es-ES") }));
  pintarMapaResultado();
  caja.scrollIntoView({ behavior: "smooth", block: "start" });
}

// ------------------------------------------------------------------ fidelidad (D-081)
// ¿Se parece a la población real? Grupos vigilados de la auditoría de F7 frente a la cifra oficial
const ESTADO_AUDITORIA = {
  verde: ["Cuadra", "bueno"],
  ambar: ["Cuadra con matices", "aviso"],
  rojo: ["Revisar", "critico"],
};
let fidelidadCargada = null;
async function cargarFidelidad(rid) {
  const caja = $("#fidelidad");
  if (!rid) { caja.hidden = true; fidelidadCargada = null; return; }
  if (rid === fidelidadCargada) return;
  fidelidadCargada = rid;
  try {
    const d = await api(`/api/auditoria/${encodeURIComponent(rid)}`);
    const filas = d.grupos.filter((g) => g.proporcion_oficial != null && g.proporcion_sintetica != null);
    const cuadran = filas.filter((g) => g.ratio != null && Math.abs(g.ratio - 1) <= 0.1).length;
    $("#fidelidad-resumen").innerHTML = `¿Se parece a la población real? <span class="fidelidad-cifra">${cuadran} de ${filas.length} cifras oficiales reproducidas</span>`;
    $("#fidelidad-cuerpo").innerHTML = `<p class="nota">Comparación con fuentes oficiales (INE, ECV, EPA…) de los grupos que más fácilmente salen mal en una población sintética. «Reproducida» = diferencia menor del 10 %. El estado también revisa el perfil del grupo y que no salga de pocas personas repetidas.</p>
      <div class="tabla-envoltorio" tabindex="0" role="region" aria-label="Comparación con cifras oficiales"><table class="tabla-asistente tabla-fidelidad"><thead><tr><th scope="col">Grupo</th><th scope="col">Sintética</th><th scope="col">Oficial</th><th scope="col">Estado</th></tr></thead><tbody>
      ${filas.map((g) => { const [txt, color] = ESTADO_AUDITORIA[g.semaforo] || ["—", "texto-3"]; return `<tr title="${escapar(g.fuente || "")}${g.motivo ? " · " + escapar(g.motivo) : ""}"><th scope="row">${escapar(g.nombre)}</th><td>${pct(g.proporcion_sintetica, 1)}</td><td>${pct(g.proporcion_oficial, 1)}</td><td><span class="punto-estado" style="background:var(--${color})"></span>${txt}</td></tr>`; }).join("")}
      </tbody></table></div>`;
    caja.hidden = false;
  } catch (_) {
    caja.hidden = true;
  }
}

// ------------------------------------------------------------------ evolución, retratos y cruces (D-082, D-083)
// paleta categórica de referencia (dataviz), en orden fijo; NS/NC en gris
const CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"];
const GRIS = "#8f8e86";
const mesNum = (f) => +f.slice(0, 4) * 12 + (+f.slice(5, 7) - 1);
function colorOpcion(opciones, o) {
  if (NSNC.includes(o)) return GRIS;
  const i = sustantivas(opciones).indexOf(o);
  return i >= 0 && i < CAT.length ? CAT[i] : GRIS;
}

function seccionEvolucion(r, opciones) {
  const pts = r.evolucion?.puntos || [];
  if (pts.length < 3) return "";
  const W = 420, H = 230, m = { l: 34, r: 92, t: 12, b: 24 };
  const hoy = mesNum(r.evolucion.hoy + "-01");
  const x0 = mesNum(pts[0].fecha), x1 = hoy;
  const series = sustantivas(opciones).slice(0, CAT.length);
  const dest = r.medicion_cis || r.total;
  let ymax = 0;
  for (const p of pts) for (const o of series) ymax = Math.max(ymax, p.dist[o]);
  for (const o of series) ymax = Math.max(ymax, dest[o].ic80[1]);
  ymax = Math.min(1, Math.ceil((ymax + 0.02) * 10) / 10);
  const X = (mm) => m.l + ((mm - x0) / Math.max(x1 - x0, 1)) * (W - m.l - m.r);
  const Y = (p) => H - m.b - (p / ymax) * (H - m.t - m.b);
  const ticksY = [0, ymax / 2, ymax].map((v) => `<line x1="${m.l}" x2="${W - m.r}" y1="${Y(v)}" y2="${Y(v)}" class="rejilla"/><text x="${m.l - 6}" y="${Y(v) + 3}" class="eje" text-anchor="end">${Math.round(v * 100)} %</text>`).join("");
  const anios = [];
  for (let a = Math.ceil(x0 / 12); a * 12 <= x1; a++) anios.push(a);
  const ticksX = anios.map((a) => `<text x="${X(a * 12)}" y="${H - 6}" class="eje" text-anchor="middle">${a}</text>`).join("");
  // posiciones de las etiquetas finales sin solaparse
  const finales = series.map((o) => ({ o, y: Y(dest[o].p) })).sort((a, b) => a.y - b.y);
  for (let i = 1; i < finales.length; i++) if (finales[i].y - finales[i - 1].y < 11) finales[i].y = finales[i - 1].y + 11;
  const yEtiqueta = Object.fromEntries(finales.map((f) => [f.o, f.y]));
  const lineas = series.map((o) => {
    const c = colorOpcion(opciones, o);
    const camino = pts.map((p) => `${X(mesNum(p.fecha)).toFixed(1)},${Y(p.dist[o]).toFixed(1)}`).join(" ");
    const ultimo = pts.at(-1);
    const d = dest[o];
    return `<polyline points="${camino}" fill="none" stroke="${c}" stroke-width="2" stroke-linejoin="round"/>
      <line x1="${X(mesNum(ultimo.fecha))}" y1="${Y(ultimo.dist[o])}" x2="${X(hoy)}" y2="${Y(d.p)}" stroke="${c}" stroke-width="1.5" stroke-dasharray="3 3"/>
      ${pts.map((p) => `<circle cx="${X(mesNum(p.fecha))}" cy="${Y(p.dist[o])}" r="3.2" fill="${c}" stroke="#fff" stroke-width="1.5" class="punto-serie" data-t="${escapar(o)} · ${p.fecha.slice(0, 7)} (estudio ${escapar(p.estudio)})" data-p="${p.dist[o]}"/>`).join("")}
      <line x1="${X(hoy)}" x2="${X(hoy)}" y1="${Y(d.ic80[0])}" y2="${Y(d.ic80[1])}" stroke="${c}" stroke-width="2"/>
      <rect x="${X(hoy) - 4.5}" y="${Y(d.p) - 4.5}" width="9" height="9" transform="rotate(45 ${X(hoy)} ${Y(d.p)})" fill="${c}" stroke="#fff" stroke-width="1.5" class="punto-serie" data-t="${escapar(o)} · hoy (estimación, IC 80 % ${pct(d.ic80[0])}–${pct(d.ic80[1])})" data-p="${d.p}"/>
      <text x="${X(hoy) + 9}" y="${yEtiqueta[o] + 3}" class="etiqueta-serie">${escapar(o.length > 13 ? o.slice(0, 12) + "…" : o)} ${Math.round(100 * d.p)} %</text>`;
  }).join("");
  const desde = pts[0].fecha.slice(0, 7), hasta = pts.at(-1).fecha.slice(0, 7);
  return `<section class="seccion" aria-labelledby="t-evolucion">
    <h4 class="seccion-titulo" id="t-evolucion">Cómo ha cambiado</h4>
    <p class="nota">El CIS hizo esta pregunta (o una casi igual) ${pts.length} veces entre ${desde} y ${hasta}. La estimación de hoy pesa más lo reciente: una medición pierde la mitad de su peso cada ${r.evolucion.vida_media_meses} meses (D-082).</p>
    <div class="leyenda-series">${series.map((o) => `<span><i style="background:${colorOpcion(opciones, o)}"></i>${escapar(o)}</span>`).join("")}</div>
    <svg class="grafico-evolucion" viewBox="0 0 ${W} ${H}" role="img" aria-label="Evolución de las respuestas desde ${desde} hasta hoy">
      ${ticksY}${ticksX}
      <line x1="${X(hoy)}" x2="${X(hoy)}" y1="${m.t}" y2="${H - m.b}" class="linea-hoy"/>
      <text x="${X(hoy)}" y="${m.t + 2}" class="eje" text-anchor="middle">hoy</text>
      ${lineas}
    </svg>
    <p class="nota">Puntos: lo que midió el CIS en cada barómetro. Rombo: estimación de hoy, como la mediría el CIS, con su intervalo del 80 %.</p>
  </section>`;
}
function activarEvolucion(raiz) {
  raiz.querySelectorAll(".punto-serie").forEach((el) => {
    el.addEventListener("mousemove", (ev) => mostrarTooltip(ev, `<b>${el.dataset.t}</b><br>${pct(+el.dataset.p, 1)}`));
    el.addEventListener("mouseleave", ocultarTooltip);
  });
}

// retratos: personas sintéticas concretas con su probabilidad de cada respuesta
const ACTIVIDAD_UNA = { ocupado: "Trabaja", parado: "En paro", inactivo: "Inactivo" };
// religiosidad de una persona (las etiquetas de los grupos van en plural)
const RELIGION_UNA = {
  catolico_practicante: ["Católico practicante", "Católica practicante"],
  catolico_no_practicante: ["Católico no practicante", "Católica no practicante"],
  otra_religion: ["Otra religión", "Otra religión"],
  agnostico: ["Agnóstico", "Agnóstica"],
  indiferente: ["Indiferente", "Indiferente"],
  ateo: ["Ateo", "Atea"],
};
const femenino = (t, sexo) => (sexo === "mujer" ? t.replace(/^Inactivo$/, "Inactiva") : t);
function chipsPersona(p) {
  const e = estado.etiquetas || {};
  const chips = [];
  const prov = e.provincia?.[p.provincia] ?? p.provincia;
  if (p.provincia && prov !== e.ccaa?.[p.ccaa] && !(e.ccaa?.[p.ccaa] || "").includes(prov)) chips.push(prov);
  if (p.estudios_3) chips.push(`Estudios: ${(e.estudios_3?.[p.estudios_3] ?? p.estudios_3).toLowerCase()}`);
  if (p.actividad_3) chips.push(femenino(ACTIVIDAD_UNA[p.actividad_3] ?? p.actividad_3, p.sexo));
  if (p.tamano_municipio_cis) chips.push(`Municipio de ${(e.tamano_municipio_cis?.[p.tamano_municipio_cis] ?? p.tamano_municipio_cis).toLowerCase()}`);
  if (RELIGION_UNA[p.religiosidad]) chips.push(RELIGION_UNA[p.religiosidad][p.sexo === "mujer" ? 1 : 0]);
  if (p.ideologia_bloque) chips.push(`Ideología: ${(e.ideologia_bloque?.[p.ideologia_bloque] ?? p.ideologia_bloque).toLowerCase()}`);
  if (p.clase_subjetiva && !["NC", "NS"].includes(p.clase_subjetiva)) chips.push(`Clase ${(e.clase_subjetiva?.[p.clase_subjetiva] ?? p.clase_subjetiva).toLowerCase()}`);
  if (p.recuerdo_voto_generales_familia) chips.push(`Voto 2023: ${(e.recuerdo_voto_generales_familia?.[p.recuerdo_voto_generales_familia] ?? p.recuerdo_voto_generales_familia).toLowerCase()}`);
  return chips;
}
function tarjetaPersona(p, opciones) {
  const orden = sustantivas(opciones).sort((a, b) => p.probabilidades[b] - p.probabilidades[a]);
  const top = orden[0];
  const barra = opciones.map((o) => `<i style="width:${100 * p.probabilidades[o]}%;background:${colorOpcion(opciones, o)}" title="${escapar(o)}: ${pct(p.probabilidades[o])}"></i>`).join("");
  return `<article class="persona">
    <div class="persona-cabecera"><span class="avatar" aria-hidden="true">${p.sexo === "mujer" ? "M" : "H"}</span>
      <div><b>${p.sexo === "mujer" ? "Mujer" : "Hombre"}, ${p.edad} años</b><span>${escapar(estado.etiquetas?.ccaa?.[p.ccaa] ?? "")}</span></div></div>
    <div class="persona-chips">${chipsPersona(p).map((c) => `<span>${escapar(c)}</span>`).join("")}</div>
    <p class="persona-respuesta">Lo más probable: <b>«${escapar(top)}»</b> (${pct(p.probabilidades[top])})</p>
    <div class="barra-apilada" role="img" aria-label="${opciones.map((o) => `${o} ${pct(p.probabilidades[o])}`).join(", ")}">${barra}</div>
  </article>`;
}
let paginaRetratos = 0;
function seccionRetratos(r, opciones) {
  if (!r.retratos?.length) return "";
  paginaRetratos = 0;
  return `<section class="seccion" aria-labelledby="t-retratos">
    <div class="cabecera-seccion"><h4 class="seccion-titulo" id="t-retratos">Personas de esta población</h4>
      <button class="enlace" id="otras-personas" type="button">Ver otras cuatro</button></div>
    <div class="leyenda-series">${opciones.map((o) => `<span><i style="background:${colorOpcion(opciones, o)}"></i>${escapar(o)}</span>`).join("")}</div>
    <div class="personas" id="personas"></div>
    <p class="nota">Son personas sintéticas: perfiles plausibles de esta población, no personas reales. La probabilidad es la de alguien con ese perfil.</p>
  </section>`;
}
function pintarRetratos(r, opciones) {
  const caja = $("#personas");
  if (!caja) return;
  const n = r.retratos.length;
  const grupo = [0, 1, 2, 3].map((k) => r.retratos[(paginaRetratos * 4 + k) % n]);
  caja.innerHTML = grupo.map((p) => tarjetaPersona(p, opciones)).join("");
}
function activarRetratos(r, opciones) {
  pintarRetratos(r, opciones);
  $("#otras-personas")?.addEventListener("click", () => { paginaRetratos++; pintarRetratos(r, opciones); });
}

// cruce con otra pregunta
function seccionCruce() {
  return `<section class="seccion" aria-labelledby="t-cruce">
    <h4 class="seccion-titulo" id="t-cruce">Cruzar con otra pregunta</h4>
    <p class="nota">Cómo responde a otra pregunta cada grupo según su respuesta a esta. Por ejemplo, la valoración del Gobierno según cómo se ve la economía.</p>
    <label class="campo"><span>Otra pregunta</span><input id="cruce-enunciado" type="text" placeholder="Escribe y elige una pregunta parecida del CIS"></label>
    <ul class="sugerencias-cruce" id="cruce-sugerencias" hidden></ul>
    <label class="campo"><span>Sus respuestas (separadas por «;»)</span><input id="cruce-opciones" type="text" placeholder="Muy buena; Buena; Regular; Mala; Muy mala"></label>
    <button class="secundario" id="cruzar" type="button">Cruzar</button>
    <div id="zona-cruce" aria-live="polite"></div>
  </section>`;
}
function activarCruce(enunciado, opciones, pob) {
  const inp = $("#cruce-enunciado");
  if (!inp) return;
  let t = null;
  inp.addEventListener("input", () => {
    clearTimeout(t);
    t = setTimeout(async () => {
      const ul = $("#cruce-sugerencias");
      if (inp.value.trim().length < 6) { ul.hidden = true; return; }
      try {
        const r = await api(`/api/banco?q=${encodeURIComponent(inp.value)}&k=5`);
        ul.innerHTML = r.preguntas.map((q, i) => `<li><button type="button" data-i="${i}">${escapar(q.enunciado)}<small>CIS · ${q.fecha} · ${escapar(q.opciones.slice(0, 4).join(" / "))}${q.opciones.length > 4 ? " …" : ""}</small></button></li>`).join("");
        ul.hidden = !r.preguntas.length;
        ul.querySelectorAll("button").forEach((b) => b.addEventListener("click", () => {
          const q = r.preguntas[+b.dataset.i];
          inp.value = q.enunciado;
          $("#cruce-opciones").value = q.opciones.map((o) => o.replace(/^\(NO LEER\)\s*/i, "")).join("; ");
          ul.hidden = true;
        }));
      } catch (_) { ul.hidden = true; }
    }, 400);
  });
  $("#cruzar").addEventListener("click", async () => {
    const zona = $("#zona-cruce");
    const b = { enunciado: inp.value.trim(), opciones: $("#cruce-opciones").value.split(";").map((x) => x.trim()).filter(Boolean) };
    if (b.enunciado.length < 3 || b.opciones.length < 2) { zona.textContent = "Escribe la otra pregunta y al menos dos respuestas."; return; }
    $("#cruzar").disabled = true;
    try {
      const tr = await post("/api/cruce", { run_id: pob.run_id, a: { enunciado, opciones }, b });
      pintarCruce(await seguir(tr.trabajo, zona));
    } catch (e) {
      zona.textContent = `No se pudo cruzar: ${e.message}`;
    } finally {
      $("#cruzar").disabled = false;
    }
  });
}
function pintarCruce(c) {
  const zona = $("#zona-cruce");
  const fuerza = c.v_cramer >= 0.3 ? "fuerte" : c.v_cramer >= 0.1 ? "moderada" : "débil";
  const filas = c.a.opciones.map((oa, i) => ({ oa, i })).filter((x) => c.a.total[x.i] >= 0.005);
  const cols = c.b.opciones.map((ob, j) => ({ ob, j })).filter((x) => c.b.total[x.j] >= 0.005);
  // frase destacada: en la respuesta más frecuente a A, la respuesta más probable a B
  const ia = filas.reduce((a, b) => (c.a.total[a.i] >= c.a.total[b.i] ? a : b)).i;
  const jb = cols.reduce((a, b) => (c.b_segun_a[ia][a.j] >= c.b_segun_a[ia][b.j] ? a : b)).j;
  const html = filas.map(({ oa, i }) => {
    const celdas = cols.map(({ j }) => {
      const v = c.b_segun_a[i][j];
      const n = Math.max(0, Math.min(SEQ.length - 1, Math.round(v * (SEQ.length - 1) / 0.8)));
      return `<td style="background:var(${SEQ[n]});color:${n >= 4 ? "#fff" : "var(--texto)"}">${pct(v)}</td>`;
    }).join("");
    return `<tr><th scope="row">${escapar(oa)} <small>(${pct(c.a.total[i])})</small></th>${celdas}</tr>`;
  }).join("");
  zona.innerHTML = `
    <p class="destacado-texto">Entre quienes responden «${escapar(c.a.opciones[ia])}», lo más frecuente es «${escapar(c.b.opciones[jb])}» (${pct(c.b_segun_a[ia][jb])}). Relación <b>${fuerza}</b> (V de Cramér ${c.v_cramer.toLocaleString("es-ES")}).</p>
    <div class="tabla-envoltorio" tabindex="0" role="region" aria-label="Cruce de las dos preguntas"><table class="tabla-calor tabla-cruce">
      <thead><tr><th scope="col"><span class="oculto">Respuesta a esta pregunta</span></th>${cols.map(({ ob }) => `<th scope="col" title="${escapar(ob)}">${escapar(ob.length > 12 ? ob.slice(0, 11) + "…" : ob)}</th>`).join("")}</tr></thead>
      <tbody>${html}</tbody></table></div>
    <p class="nota">Cada fila suma 100 %: cómo responde a la otra pregunta quien da esa respuesta a esta. ${escapar(c.fuente_relacion.nota)}</p>`;
}

// ------------------------------------------------------------------ regiones y grupos (D-081)
const PREFIJO = { CCAA: "ccaa", PROV: "provincia" };
const TERRITORIALES = ["ccaa", "provincia"];
const sustantivas = (ops) => ops.filter((o) => !NSNC.includes(o));
const confDe = (r, k) => r.confianza?.por_subgrupo?.[k] ?? 1;
const intervaloDe = (x) => x.ic80 || x.ic95;
function opcionPrincipal(r) {
  const s = sustantivas(r.opciones);
  return s.reduce((a, b) => (r.total[a].p >= r.total[b].p ? a : b));
}
function nivelesRegion(r) {
  return ["CCAA", "PROV"].filter((n) => Object.keys(r.por_subgrupo).filter((k) => k.startsWith(PREFIJO[n] + "=")).length >= 2);
}
function valorRegion(r, nivel, codigo, op) {
  if (nivel === "CCAA" && r.comparacion) {
    const t = r.comparacion.territorios[`CCAA:${codigo}`];
    return t ? { p: t.total[op].p, ic: t.total[op].ic80, c: t.confianza } : null;
  }
  const k = `${PREFIJO[nivel]}=${codigo}`;
  const d = r.por_subgrupo[k]?.[op];
  return d ? { p: d.p, ic: intervaloDe(d), c: confDe(r, k) } : null;
}
function codigosRegion(r, nivel) {
  return Object.keys(r.por_subgrupo).filter((k) => k.startsWith(PREFIJO[nivel] + "=")).map((k) => k.split("=")[1]);
}
function nombreRegion(nivel, codigo) {
  return estado.etiquetas?.[PREFIJO[nivel]]?.[codigo] ?? codigo;
}

function seccionRegiones(r, pob) {
  const niveles = nivelesRegion(r);
  if (!niveles.length) return "";
  const comparable = niveles.includes("CCAA") && pob.territorio === "ES" && r.tipo !== "dato";
  return `<section class="seccion" aria-labelledby="t-regiones">
    <div class="cabecera-seccion"><h4 class="seccion-titulo" id="t-regiones">Por regiones</h4>
      ${niveles.length > 1 ? `<div class="conmutador mini" role="group" aria-label="Nivel" id="nivel-region">${niveles.map((n) => `<button type="button" aria-pressed="${n === estado.nivelMapa}" data-n="${n}">${n === "CCAA" ? "Comunidades" : "Provincias"}</button>`).join("")}</div>` : ""}
    </div>
    <label class="campo-mini fila-opcion"><span>Respuesta que se compara</span>
      <select id="opcion-region">${r.opciones.map((o, i) => `<option value="${i}"${i === estado.opcionMapa ? " selected" : ""}>${escapar(o)}</option>`).join("")}</select></label>
    <div id="lista-regiones" class="lista-regiones" tabindex="0" role="region" aria-label="Ranking por regiones"></div>
    <p class="nota">El mapa se colorea igual. ${r.tipo === "dato" ? "" : "Las filas más claras tienen confianza baja (pocos encuestados del CIS en esa región)."}</p>
    ${comparable ? `<div class="comparar"><button class="secundario" id="comparar" type="button">Recalcular cada comunidad con su propia población</button>
      <p class="nota">Más fino que el desglose de la población nacional: usa las 19 poblaciones de 100 000 personas. Tarda unos 2 minutos.</p><div id="zona-comparar"></div></div>` : ""}
  </section>`;
}

function pintarListaRegiones() {
  const r = estado.resultado;
  const caja = $("#lista-regiones");
  if (!r || !caja) return;
  const op = r.opciones[estado.opcionMapa];
  const filas = codigosRegion(r, estado.nivelMapa)
    .map((c) => ({ c, nombre: nombreRegion(estado.nivelMapa, c), v: valorRegion(r, estado.nivelMapa, c, op) }))
    .filter((x) => x.v)
    .sort((a, b) => b.v.p - a.v.p);
  const max = Math.max(...filas.map((x) => x.v.ic?.[1] ?? x.v.p), 0.01);
  caja.innerHTML = filas.map((x) => `<div class="fila-region${x.v.c < 0.5 ? " baja" : ""}" data-t="${escapar(x.nombre)}" data-p="${x.v.p}" data-a="${x.v.ic?.[0] ?? ""}" data-b="${x.v.ic?.[1] ?? ""}" data-c="${x.v.c}">
      <span class="nombre">${escapar(x.nombre)}</span>
      <span class="pista-mini">${x.v.ic ? `<em style="left:${(100 * x.v.ic[0]) / max}%;width:${(100 * (x.v.ic[1] - x.v.ic[0])) / max}%"></em>` : ""}<i style="width:${(100 * x.v.p) / max}%"></i></span>
      <span class="valor">${pct(x.v.p)}</span></div>`).join("");
  caja.querySelectorAll(".fila-region").forEach((el) => {
    el.addEventListener("mousemove", (ev) => mostrarTooltip(ev, `<b>${el.dataset.t}</b><br>${escapar(op)}: ${pct(+el.dataset.p, 1)}${el.dataset.a !== "" ? `<br>${r.tipo === "dato" ? "Margen de simulación" : "IC 80 %"}: ${pct(+el.dataset.a, 1)} – ${pct(+el.dataset.b, 1)}` : ""}${r.tipo === "dato" ? "" : `<br>Confianza: ${pct(+el.dataset.c)}`}`));
    el.addEventListener("mouseleave", ocultarTooltip);
  });
}

function activarRegiones(enunciado, opciones) {
  $("#opcion-region")?.addEventListener("change", (e) => { estado.opcionMapa = +e.target.value; pintarListaRegiones(); pintarMapaResultado(); });
  document.querySelectorAll("#nivel-region button").forEach((b) => b.addEventListener("click", () => {
    document.querySelectorAll("#nivel-region button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    estado.nivelMapa = b.dataset.n;
    pintarListaRegiones();
    pintarMapaResultado();
  }));
  $("#comparar")?.addEventListener("click", () => compararComunidades(enunciado, opciones));
  pintarListaRegiones();
}

// grupos (sin los territoriales, que van en «Por regiones»), ordenados por cuánto separan las
// respuestas; los tres que más separan llevan una estrella
function destacados(r) {
  const dims = [...new Set(Object.keys(r.por_subgrupo).map((k) => k.split("=")[0]))].filter((d) => !TERRITORIALES.includes(d));
  return dims.map((d) => {
    const ks = Object.keys(r.por_subgrupo).filter((k) => k.startsWith(d + "=") && confDe(r, k) >= 0.5 && !/=(NC|NS|NS_NC)$/.test(k));
    let mejor = { d, dif: 0 };
    for (const o of sustantivas(r.opciones)) {
      const v = ks.map((k) => ({ k, p: r.por_subgrupo[k][o].p })).sort((a, b) => a.p - b.p);
      if (v.length >= 2 && v.at(-1).p - v[0].p > mejor.dif) mejor = { d, dif: v.at(-1).p - v[0].p, o, lo: v[0], hi: v.at(-1) };
    }
    return mejor;
  }).sort((a, b) => b.dif - a.dif);
}

function seccionGrupos(r, tabla) {
  const des = destacados(r);
  if (!des.length) return "";
  estado.dimension = des[0].d;
  const estrellas = new Set(des.slice(0, 3).filter((x) => x.dif >= 0.05).map((x) => x.d));
  const nombreDim = (d) => estado.etiquetas?.dimensiones?.[d] ?? d;
  const presentes = new Set(des.map((x) => x.d));
  const grupos = Object.entries(estado.etiquetas?.grupos_dimensiones || { Grupos: [...presentes] })
    .map(([t, ds]) => [t, ds.filter((d) => presentes.has(d))]).filter(([, ds]) => ds.length);
  const top = des[0];
  const frase = top.dif >= 0.05
    ? `Lo que más cambia es <b>${escapar(nombreDim(top.d).toLowerCase())}</b>: «${escapar(top.o)}» va del ${pct(top.lo.p)} (${escapar(nombreNivel(top.d, top.lo.k.split("=")[1]))}) al ${pct(top.hi.p)} (${escapar(nombreNivel(top.d, top.hi.k.split("=")[1]))}).`
    : "Las diferencias entre grupos son pequeñas (menos de 5 puntos).";
  return `<section class="seccion" aria-labelledby="t-grupos">
    <h4 class="seccion-titulo" id="t-grupos">Por grupos</h4>
    <p class="destacado-texto">${frase}</p>
    ${grupos.map(([t, ds]) => `<div class="grupo-dims"><span class="grupo-titulo">${escapar(t)}</span>
      <div class="dimensiones">${ds.map((d) => `<button type="button" aria-pressed="${d === estado.dimension}" data-d="${d}"${estrellas.has(d) ? ' class="estrella" title="Separa mucho las respuestas"' : ""}>${estrellas.has(d) ? "★ " : ""}${escapar(nombreDim(d))}</button>`).join("")}</div></div>`).join("")}
    <div id="zona-tabla">${tabla(estado.dimension)}</div>
  </section>`;
}

function activarGrupos(tabla, tips) {
  document.querySelectorAll(".grupo-dims button").forEach((b) => b.addEventListener("click", () => {
    document.querySelectorAll(".grupo-dims button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    estado.dimension = b.dataset.d;
    $("#zona-tabla").innerHTML = tabla(b.dataset.d);
    tips($("#zona-tabla"));
  }));
}

function prepararMapa(r) {
  const niveles = nivelesRegion(r);
  estado.nivelMapa = niveles[0] ?? "CCAA";
  estado.opcionMapa = niveles.length ? r.opciones.indexOf(opcionPrincipal(r)) : null;
}

// ------------------------------------------------------------------ asistente de tamaño (D-079)
const TECHO = {
  alta: "Hay bastantes encuestados del CIS de este territorio: la confianza puede ser alta.",
  media: "Hay un número moderado de encuestados del CIS de este territorio: la confianza será media como mucho.",
  baja: "Hay muy pocos encuestados del CIS de este territorio: la confianza será baja con cualquier tamaño. Más personas sintéticas no lo arreglan.",
};
async function asistente() {
  if (!$("#asistente").open) return;
  const caja = $("#asis-resultado");
  caja.textContent = "Calculando…";
  try {
    const r = await api(`/api/tamano?territorio=${encodeURIComponent(estado.territorio)}&margen=${$("#asis-margen").value}&detalle=${$("#asis-detalle").value}`);
    const filas = r.tamanos.map((t) => `<tr${t.tamano === r.recomendado ? ' class="recomendado"' : ""}><th scope="row">${miles(t.tamano)}</th><td>± ${(100 * t.margen_prediccion).toLocaleString("es-ES", { maximumFractionDigits: 1 })}</td><td>± ${(100 * t.margen_datos).toLocaleString("es-ES", { maximumFractionDigits: 1 })}</td></tr>`).join("");
    caja.innerHTML = `
      <p><b>Recomendado: ${miles(r.recomendado)}.</b> ${r.alcanzable ? "Cumple el margen pedido en el grupo más pequeño" : `Ningún tamaño llega a ese margen en el grupo más pequeño (${pct(r.cuota_grupo_mas_pequeno, 1)} de la población): las predicciones usan como mucho ${miles(r.muestra_prediccion)} personas`} (${pct(r.cuota_grupo_mas_pequeno, 1)} de la población).</p>
      <table class="tabla-asistente"><thead><tr><th scope="col">Tamaño</th><th scope="col">Margen en predicciones (puntos)</th><th scope="col">Margen en datos de la población</th></tr></thead><tbody>${filas}</tbody></table>
      ${r.techo_confianza ? `<p class="techo techo-${r.techo_confianza}"><b>Confianza esperable:</b> ${TECHO[r.techo_confianza]} Mediana de ${Math.round(r.encuestados_cis_mediana).toLocaleString("es-ES")} encuestados por pregunta.</p>` : ""}
      <button class="secundario" id="asis-usar" type="button">Usar ${miles(r.recomendado)}</button>`;
    $("#asis-usar").addEventListener("click", () => { estado.tamano = r.recomendado; pintarTamanos(); });
  } catch (e) {
    caja.textContent = `No se pudo calcular: ${e.message}`;
  }
}
$("#asistente").addEventListener("toggle", asistente);
$("#asis-detalle").addEventListener("change", asistente);
$("#asis-margen").addEventListener("change", asistente);

// ------------------------------------------------------------------ historial (solo en este navegador)
const HISTORIAL = "historial-v1";
const MAX_HISTORIAL = 10;
function leerHistorial() {
  try { return JSON.parse(localStorage.getItem(HISTORIAL) || "[]"); } catch (_) { return []; }
}
function guardarHistorial(e) {
  const h = leerHistorial().filter((x) => !(x.titulo === e.titulo && x.run_id === e.run_id));
  h.unshift({ ...e, fecha: new Date().toISOString() });
  for (let n = Math.min(h.length, MAX_HISTORIAL); n > 0; n--) {
    try { localStorage.setItem(HISTORIAL, JSON.stringify(h.slice(0, n))); break; } catch (_) { /* sin sitio: se guardan menos */ }
  }
  pintarHistorial();
}
function pintarHistorial() {
  const h = leerHistorial();
  $("#historial").hidden = h.length === 0;
  const ul = $("#lista-historial");
  ul.innerHTML = "";
  h.forEach((e) => {
    const li = document.createElement("li");
    const b = document.createElement("button");
    b.type = "button";
    const cuando = new Date(e.fecha).toLocaleString("es-ES", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
    b.innerHTML = `${escapar(e.titulo)}<small>${e.tipo === "dato" ? "Dato de la población" : "Pregunta"} · ${escapar(e.nombre)} · ${cuando}</small>`;
    b.addEventListener("click", () => abrirHistorial(e));
    li.append(b);
    ul.append(li);
  });
}
function abrirHistorial(e) {
  if (e.territorio !== estado.territorio) {
    ponerNivelSinSeleccion(e.territorio.startsWith("PROV") ? "PROV" : "CCAA");
    estado.nivel = e.territorio === "ES" ? "ES" : e.territorio.startsWith("PROV") ? "PROV" : "CCAA";
    elegirTerritorio(e.territorio, e.nombre);
  }
  const p = estado.poblaciones.find((x) => x.run_id === e.run_id);
  if (!p) { $("#trabajo").textContent = "Esa población ya no está disponible."; return; }
  estado.tamano = p.tamano_solicitado;
  pintarTamanos();
  if (e.tipo === "dato") mostrarAtributo(e.variable);
  else { $("#enunciado").value = e.titulo; pintarResultado(e.r, e.titulo, e.opciones, p); }
}
$("#borrar-historial").addEventListener("click", () => {
  try { localStorage.removeItem(HISTORIAL); } catch (_) { /* sin almacenamiento */ }
  pintarHistorial();
});

// ------------------------------------------------------------------ comparar comunidades (D-080)
async function compararComunidades(enunciado, opciones) {
  const zona = $("#zona-comparar");
  const boton = $("#comparar");
  boton.disabled = true;
  try {
    const t = await post("/api/comparar", { enunciado, opciones, nivel: "CCAA" });
    estado.resultado.comparacion = await seguir(t.trabajo, zona);
    zona.innerHTML = '<p class="nota"><b>Mostrando cada comunidad con su propia población.</b></p>';
    estado.nivelMapa = "CCAA";
    document.querySelectorAll("#nivel-region button").forEach((x) => x.setAttribute("aria-pressed", String(x.dataset.n === "CCAA")));
    pintarListaRegiones();
    pintarMapaResultado();
  } catch (e) {
    zona.textContent = `No se pudo comparar: ${e.message}`;
  } finally {
    boton.disabled = false;
  }
}

// ------------------------------------------------------------------ exportar
// CSV para Excel en español: separador «;» y decimales con coma (el JSON queda para programas)
function aCsv(filas) {
  const celda = (x) => (typeof x === "number" ? String(x).replace(".", ",") : `"${String(x).replaceAll('"', '""')}"`);
  return filas.map((f) => f.map(celda).join(";")).join("\n");
}
function descargar(nombre, contenido, tipo) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(contenido instanceof Blob ? contenido : new Blob(["\ufeff" + contenido], { type: `${tipo};charset=utf-8` }));
  a.download = nombre;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 5000);
}

function csvPregunta(r) {
  const filas = [["grupo", "opcion", "proporcion", "ic80_inf", "ic80_sup", "ic95_inf", "ic95_sup", "confianza"]];
  const add = (g, dist, c) => Object.entries(dist).forEach(([o, d]) => filas.push([g, o, d.p, d.ic80[0], d.ic80[1], d.ic95[0], d.ic95[1], c ?? ""]));
  add("total", r.total, r.confianza.total);
  if (r.medicion_cis) add("como_lo_mediria_el_cis", r.medicion_cis, "");
  Object.entries(r.por_subgrupo).forEach(([k, v]) => add(k, v, r.confianza.por_subgrupo[k]));
  return aCsv(filas);
}

async function informePdf(tipo, datos, extra = {}) {
  const msg = $("#trabajo");
  msg.textContent = "Preparando el informe PDF…";
  try {
    const contexto = { territorio: estado.territorio, territorio_nombre: estado.nombre, ...extra };
    const res = await fetch("/api/informe", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ tipo, datos, contexto }) });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    descargar(`informe_${(datos.id || datos.variable || "resultado")}.pdf`, await res.blob());
    msg.textContent = "";
  } catch (e) {
    msg.textContent = `No se pudo generar el informe: ${e.message}`;
  }
}

function ponerNivelSinSeleccion(nivel) {
  document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === nivel)));
  mostrarNivel(nivel);
}

// coloreado del mapa con una respuesta del resultado, por comunidades o por provincias
let rangoMapa = [0, 1];
function valorMapa(prop) {
  const r = estado.resultado;
  if (!r || estado.opcionMapa == null || prop.nivel !== estado.nivelMapa) return null;
  const v = valorRegion(r, prop.nivel, prop.codigo, r.opciones[estado.opcionMapa]);
  return v ? { p: v.p, c: v.c } : null;
}
function estiloMapa(f) {
  const v = valorMapa(f.properties);
  if (!v) return { color: css("--texto-3"), weight: 0.6, fillOpacity: 0.05 };
  return { color: "#ffffff", weight: 1.2, opacity: 1, fillColor: colorSecuencial(v.p, ...rangoMapa), fillOpacity: v.c < 0.5 ? 0.45 : 0.85 };
}
function pintarMapaResultado() {
  const ley = $("#leyenda-mapa");
  if (estado.opcionMapa == null || !estado.resultado) { ley.hidden = true; refrescarEstilos(); return; }
  const r = estado.resultado;
  const op = r.opciones[estado.opcionMapa];
  const nivel = estado.nivelMapa;
  const vals = codigosRegion(r, nivel).map((c) => valorRegion(r, nivel, c, op)?.p).filter((x) => x != null);
  if (!vals.length) { ley.hidden = true; refrescarEstilos(); return; }
  rangoMapa = [Math.min(...vals), Math.max(...vals)];
  ponerNivelSinSeleccion(nivel);
  for (const c of todas(nivel)) c.setStyle(estiloMapa);
  ley.hidden = false;
  ley.innerHTML = `<b>${escapar(op)}</b> por ${nivel === "CCAA" ? "comunidad" : "provincia"}${r.comparacion && nivel === "CCAA" ? " (población propia)" : ""}
    <div class="escala">${SEQ.map((v) => `<i style="background:var(${v})"></i>`).join("")}</div>
    <div class="extremos"><span>${pct(rangoMapa[0])}</span><span>${pct(rangoMapa[1])}</span></div>
    ${r.tipo === "dato" ? "" : '<div class="nota-leyenda">Más transparente: confianza baja.</div>'}
    <button type="button" id="quitar-mapa">Quitar colores</button>`;
  $("#quitar-mapa").addEventListener("click", () => { estado.opcionMapa = null; pintarMapaResultado(); });
}

// ------------------------------------------------------------------ evento
function pintarEvento(r, enunciado, opciones, pob) {
  estado.resultado = null;
  estado.opcionMapa = null;
  pintarMapaResultado();
  const caja = $("#resultado");
  caja.hidden = false;
  const conCambio = r.categorias.every((c) => c.despues != null);
  const filas = r.categorias.map((c) => {
    const a = c.antes, d = c.despues ?? c.antes;
    const izq = Math.min(a, d), ancho = Math.abs(d - a);
    return `<div class="etiqueta">${escapar(c.categoria)}</div>
      <div class="pista" data-o="${escapar(c.categoria)}" data-p="${a}" data-a80="${c.ic80_cambio?.[0] ?? 0}" data-b80="${c.ic80_cambio?.[1] ?? 0}" data-a95="${d}" data-b95="${d}">
        <span class="barra" style="width:${100 * a}%;background:var(--texto-3);opacity:0.35"></span>
        <span class="ic80" style="left:${100 * izq}%;width:${100 * ancho}%"></span>
        <span class="marca-p" style="left:calc(${100 * a}% - 1px);background:var(--texto-3)"></span>
        ${conCambio ? `<span class="marca-p" style="left:calc(${100 * d}% - 1px);background:var(--serie);width:4px"></span>` : ""}
      </div>
      <div class="valor">${conCambio ? `${(100 * (d - a) >= 0 ? "+" : "")}${(100 * (d - a)).toLocaleString("es-ES", { maximumFractionDigits: 1 })}` : pct(a)}</div>`;
  });
  caja.innerHTML = `
    <h3>${escapar(enunciado)}</h3>
    <div class="metas"><span>${escapar(estado.nombre)}</span><span>Evento: ${escapar($("#evento-descripcion").value)}</span><span>${escapar(r.fecha_evento)}</span></div>
    <div class="barras">${filas.join("")}</div>
    <div class="leyenda-barras"><span><i style="background:var(--texto-3)"></i>Antes</span>${conCambio ? `<span><i style="background:var(--serie)"></i>Después</span><span>Valor: cambio en puntos</span>` : ""}</div>
    ${r.justificacion_llm ? `<p class="justificacion">«${escapar(r.justificacion_llm)}»</p>` : ""}
    ${!conCambio ? `<p class="aviso">${escapar(r.motivo || "Sin cambio estimado.")}</p>` : ""}
    <p class="aviso">${escapar(r.aviso)}</p>`;
  caja.querySelectorAll(".pista").forEach((el, i) => {
    const c = r.categorias[i];
    el.addEventListener("mousemove", (ev) => mostrarTooltip(ev, `<b>${escapar(c.categoria)}</b><br>Antes: ${pct(c.antes, 1)}${c.despues != null ? `<br>Después: ${pct(c.despues, 1)}<br>Cambio (IC 80 %): ${pct(c.ic80_cambio[0], 1)} a ${pct(c.ic80_cambio[1], 1)}` : ""}`));
    el.addEventListener("mouseleave", ocultarTooltip);
  });
  caja.scrollIntoView({ behavior: "smooth", block: "start" });
}

// ------------------------------------------------------------------ LLM
async function actualizarLLM() {
  try {
    const r = await api("/api/llm");
    const f = (x) => x.toLocaleString("es-ES", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    $("#llm").textContent = r.activo ? `LLM ${f(r.gastado_eur)} € de ${f(r.tope_total_eur)} €` : "LLM desactivado";
  } catch (_) { /* informativo */ }
}

// gancho para las pruebas de extremo a extremo (tools/prueba_interfaz.py)
window.sinpop = { elegirTerritorio, ponerNivel };

// ------------------------------------------------------------------ arranque
(async function iniciar() {
  pintarOpciones();
  try {
    const [g, et] = await Promise.all([api("/api/territorios"), api("/api/etiquetas")]);
    geo = g;
    estado.etiquetas = et;
    capas.CCAA = crearCapa("CCAA");
    capas.PROV = crearCapa("PROV");
    capasCanarias.CCAA = crearCapa("CCAA", true);
    capasCanarias.PROV = crearCapa("PROV", true);
    capas.CCAA.addTo(mapa);
    capasCanarias.CCAA.addTo(mapaCanarias);
    // el recuadro se encuadra cuando ya tiene tamaño (fuentes cargadas, panel colocado) y cada vez
    // que cambia: si no, Leaflet lo calcula con 0 px y las islas quedan fuera de la vista
    const encuadrar = () => { mapaCanarias.invalidateSize(); mapaCanarias.fitBounds(capasCanarias.CCAA.getBounds(), { padding: [8, 8] }); };
    encuadrar();
    requestAnimationFrame(encuadrar);
    window.addEventListener("load", encuadrar);
    if (window.ResizeObserver) new ResizeObserver(encuadrar).observe($("#mapa-canarias"));
    // vista inicial: península, Baleares, Ceuta y Melilla (Canarias va en su recuadro)
    const sinCanarias = L.featureGroup(capas.CCAA.getLayers().filter((c) => !CANARIAS.has(c.feature.properties.territorio)));
    mapa.fitBounds(sinCanarias.getBounds(), { padding: [24, 24], maxZoom: 7 });
  } catch (e) {
    $("#estado-poblacion").textContent = `No se pudo cargar el mapa: ${e.message}`;
  }
  try { estado.paquete = (await api("/api/modo")).paquete; } catch { estado.paquete = false; }
  await cargarPoblaciones();
  pintarHistorial();
  actualizarLLM();
})();
