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
  etiquetas: null,
  resultado: null,
  vista: "total",
  dimension: null,
  opcionMapa: null,
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

// ------------------------------------------------------------------ tema
function aplicarTema(t) {
  if (t) document.documentElement.dataset.theme = t; else delete document.documentElement.dataset.theme;
  try { t ? localStorage.setItem("tema", t) : localStorage.removeItem("tema"); } catch (_) { /* sin almacenamiento */ }
  if (estado.resultado) pintarMapaResultado();
}
try { const t = localStorage.getItem("tema"); if (t) document.documentElement.dataset.theme = t; } catch (_) { /* sin almacenamiento */ }
$("#tema").addEventListener("click", () => {
  const oscuro = document.documentElement.dataset.theme
    ? document.documentElement.dataset.theme === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches;
  aplicarTema(oscuro ? "light" : "dark");
});

// ------------------------------------------------------------------ mapa
const mapa = L.map("mapa", { zoomControl: true, attributionControl: true, minZoom: 4 }).setView([40.2, -3.6], 6);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 12,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> · límites: INE',
}).addTo(mapa);
const capas = { CCAA: null, PROV: null };
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

function crearCapa(nivel) {
  return L.geoJSON(geo, {
    filter: (f) => f.properties.nivel === nivel,
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
  for (const n of ["CCAA", "PROV"]) if (capas[n]) capas[n].setStyle(estado.opcionMapa != null && n === "CCAA" ? estiloMapa : estiloBase);
}

function ponerNivel(nivel) {
  estado.nivel = nivel;
  document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === nivel)));
  for (const n of ["CCAA", "PROV"]) {
    if (capas[n] && mapa.hasLayer(capas[n])) mapa.removeLayer(capas[n]);
  }
  const visible = nivel === "PROV" ? "PROV" : "CCAA";
  if (capas[visible]) capas[visible].addTo(mapa);
  if (nivel === "ES") elegirTerritorio("ES", "España");
}
document.querySelectorAll(".niveles button").forEach((b) => b.addEventListener("click", () => ponerNivel(b.dataset.nivel)));
$("#canarias").addEventListener("click", () => mapa.flyTo([28.3, -15.8], 7));

function elegirTerritorio(codigo, nombre) {
  if (estado.nivel === "ES" && codigo !== "ES") {
    estado.nivel = codigo.startsWith("PROV") ? "PROV" : "CCAA";
    document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === estado.nivel)));
  }
  estado.territorio = codigo;
  estado.nombre = nombre;
  $("#territorio-nombre").textContent = nombre;
  if (codigo !== "ES" && estado.tamano === 1_000_000) estado.tamano = 100_000;
  pintarTamanos();
  refrescarEstilos();
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
  if (p?.lista) {
    e.innerHTML = `<span class="indicador" style="background:var(--bueno)"></span> Lista para preguntar · ${p.tamano.toLocaleString("es-ES")} personas sintéticas`;
  } else {
    const minutos = estado.tamano >= 500_000 ? "30-60 minutos" : estado.tamano >= 100_000 ? "unos 10 minutos" : "unos minutos";
    e.innerHTML = `<span class="indicador" style="background:var(--texto-3)"></span> ${p ? "Le faltan capas" : "Aún no generada"} · tarda ${minutos}`;
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
    caja.hidden = r.preguntas.length === 0;
  } catch (_) { caja.hidden = true; }
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
      const t = await post("/api/preguntas", { run_id: p.run_id, enunciado, opciones });
      r = await seguir(t.trabajo, msg);
      pintarResultado(r, enunciado, opciones, p);
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
  return `<div class="tabla-envoltorio"><table class="tabla-calor"><thead><tr><th></th>${cab}</tr></thead><tbody>${filas.join("")}</tbody></table></div>
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
  estado.opcionMapa = null;
  const dims = [...new Set(Object.keys(r.por_subgrupo).map((k) => k.split("=")[0]))];
  estado.dimension = dims[0] ?? null;
  const caja = $("#resultado");
  caja.hidden = false;
  const conf = r.confianza.total;
  const llm = r.versiones?.modelo_llm ? `con ${escapar(r.versiones.modelo_llm)}` : "sin modelo de lenguaje";
  const permiteMapa = Object.keys(r.por_subgrupo).some((k) => k.startsWith("ccaa=")) && pob.territorio === "ES";
  caja.innerHTML = `
    <h3>${escapar(enunciado)}</h3>
    <div class="metas"><span>${escapar(estado.nombre)}</span><span>${pob.tamano.toLocaleString("es-ES")} personas</span><span>Estimador ${llm}</span></div>
    <div class="conmutador" role="group" aria-label="Qué se estima">
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
    ${dims.length ? `<p class="seccion-titulo">Por grupos</p>
      <div class="dimensiones" id="dimensiones">${dims.map((d, i) => `<button aria-pressed="${i === 0}" data-d="${d}">${escapar(estado.etiquetas?.dimensiones?.[d] ?? d)}</button>`).join("")}</div>
      <div id="zona-tabla">${tablaSubgrupos(r, estado.dimension, opciones)}</div>` : ""}
    ${permiteMapa ? `<p class="seccion-titulo">En el mapa</p><div class="fila"><select id="opcion-mapa" aria-label="Opción para colorear el mapa"><option value="">Elige una opción para colorear las comunidades…</option>${opciones.map((o, i) => `<option value="${i}">${escapar(o)}</option>`).join("")}</select></div>` : ""}
    ${r.preguntas_similares?.length ? `<p class="seccion-titulo">Se apoya en estas preguntas del CIS</p><ol class="parecidas">${r.preguntas_similares.map((x) => `<li>${escapar(x)}</li>`).join("")}</ol>` : ""}
    <p class="aviso">${escapar(r.aviso)}</p>
    <p class="coste">Coste: ${r.coste.llamadas} llamadas al modelo de lenguaje · ${r.coste.eur.toLocaleString("es-ES", { maximumFractionDigits: 3 })} € · ${Math.round(r.coste.segundos)} s</p>
    <div class="acciones-resultado"><button class="secundario" id="descargar" type="button">Descargar JSON</button></div>`;
  activarTooltipsBarras(caja);
  activarTooltipsTabla(caja);
  caja.querySelectorAll(".conmutador button").forEach((b) => b.addEventListener("click", () => {
    caja.querySelectorAll(".conmutador button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    $("#zona-barras").innerHTML = barras(r[b.dataset.v], opciones);
    activarTooltipsBarras($("#zona-barras"));
  }));
  caja.querySelectorAll("#dimensiones button").forEach((b) => b.addEventListener("click", () => {
    caja.querySelectorAll("#dimensiones button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    $("#zona-tabla").innerHTML = tablaSubgrupos(r, b.dataset.d, opciones);
    activarTooltipsTabla($("#zona-tabla"));
  }));
  $("#opcion-mapa")?.addEventListener("change", (e) => {
    estado.opcionMapa = e.target.value === "" ? null : +e.target.value;
    if (estado.opcionMapa != null) ponerNivelSinSeleccion("CCAA");
    pintarMapaResultado();
  });
  $("#descargar").addEventListener("click", () => {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([JSON.stringify(r, null, 1)], { type: "application/json" }));
    a.download = `${r.id}.json`;
    a.click();
  });
  pintarMapaResultado();
  caja.scrollIntoView({ behavior: "smooth", block: "start" });
}

function ponerNivelSinSeleccion(nivel) {
  document.querySelectorAll(".niveles button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.nivel === nivel)));
  for (const n of ["CCAA", "PROV"]) if (capas[n] && mapa.hasLayer(capas[n])) mapa.removeLayer(capas[n]);
  capas[nivel].addTo(mapa);
}

// coloreado del mapa con una opción del resultado (solo población nacional, desglose por comunidad)
let rangoMapa = [0, 1];
function valorMapa(prop) {
  const r = estado.resultado;
  if (!r || estado.opcionMapa == null || prop.nivel !== "CCAA") return null;
  const k = `ccaa=${prop.codigo}`;
  const d = r.por_subgrupo[k];
  if (!d) return null;
  return { p: d[r.opciones[estado.opcionMapa]].p, c: r.confianza.por_subgrupo[k] };
}
function estiloMapa(f) {
  const v = valorMapa(f.properties);
  if (!v) return { color: css("--texto-3"), weight: 0.6, fillOpacity: 0.05 };
  return { color: css("--superficie"), weight: 1.2, opacity: 1, fillColor: colorSecuencial(v.p, ...rangoMapa), fillOpacity: v.c < 0.5 ? 0.45 : 0.85 };
}
function pintarMapaResultado() {
  const ley = $("#leyenda-mapa");
  if (estado.opcionMapa == null || !estado.resultado) { ley.hidden = true; refrescarEstilos(); return; }
  const r = estado.resultado;
  const vals = Object.entries(r.por_subgrupo).filter(([k]) => k.startsWith("ccaa=")).map(([, d]) => d[r.opciones[estado.opcionMapa]].p);
  rangoMapa = [Math.min(...vals), Math.max(...vals)];
  capas.CCAA.setStyle(estiloMapa);
  ley.hidden = false;
  ley.innerHTML = `<b>${escapar(r.opciones[estado.opcionMapa])}</b> por comunidad
    <div class="escala">${SEQ.map((v) => `<i style="background:var(${v})"></i>`).join("")}</div>
    <div class="extremos"><span>${pct(rangoMapa[0])}</span><span>${pct(rangoMapa[1])}</span></div>
    <div style="color:var(--texto-3);margin-top:4px">Más transparente: confianza baja.</div>
    <button type="button" id="quitar-mapa">Quitar coloreado</button>`;
  $("#quitar-mapa").addEventListener("click", () => { estado.opcionMapa = null; const s = $("#opcion-mapa"); if (s) s.value = ""; pintarMapaResultado(); });
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

// ------------------------------------------------------------------ arranque
(async function iniciar() {
  pintarOpciones();
  try {
    const [g, et] = await Promise.all([api("/api/territorios"), api("/api/etiquetas")]);
    geo = g;
    estado.etiquetas = et;
    capas.CCAA = crearCapa("CCAA");
    capas.PROV = crearCapa("PROV");
    capas.CCAA.addTo(mapa);
    mapa.fitBounds(capas.CCAA.getBounds().pad(-0.05), { maxZoom: 6 });
    mapa.setView([40.0, -3.7], mapa.getZoom());
  } catch (e) {
    $("#estado-poblacion").textContent = `No se pudo cargar el mapa: ${e.message}`;
  }
  await cargarPoblaciones();
  actualizarLLM();
})();
