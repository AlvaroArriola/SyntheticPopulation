// España sintética · validación (D-091): lo que predijo el sistema frente a lo que midió el CIS.
const $ = (s) => document.querySelector(s);
const pct = (x, d = 0) => (x == null ? "—" : (100 * x).toLocaleString("es-ES", { maximumFractionDigits: d, minimumFractionDigits: d }) + " %");
const pts = (x, d = 1) => (x == null ? "—" : (100 * x).toLocaleString("es-ES", { maximumFractionDigits: d, minimumFractionDigits: d }));
const NSNC = new Set(["N.S.", "N.C."]);
const NOMBRES_DIM = {
  edad_4: "Edad", sexo: "Sexo", estudios_3: "Estudios", actividad_3: "Situación laboral",
  tamano_municipio_cis: "Tamaño del municipio", ccaa: "Comunidad", religiosidad: "Religiosidad",
  clase_subjetiva: "Clase social", ideologia_bloque: "Ideología", recuerdo_voto_generales_familia: "Recuerdo de voto",
};
const METODO = {
  analogas: "Preguntas parecidas del CIS",
  llm_anclado: "Modelo de lenguaje anclado en el banco",
};
const estado = { resumen: null, etiquetas: {}, estudio: "", tipo: "", orden: "cuestionario", texto: "", sel: null, detalle: null, dim: null, opcion: null };

async function api(ruta) {
  const r = await fetch(ruta);
  if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
  return r.json();
}
function escapar(t) { const d = document.createElement("div"); d.textContent = t ?? ""; return d.innerHTML; }
// «(NO LEER)» es una instrucción al entrevistador del cuestionario del CIS, no parte de la respuesta
const limpia = (o) => o.replace(/^\(NO LEER\)\s*/i, "");
const tooltip = $("#tooltip");
function tip(ev, html) {
  tooltip.innerHTML = html; tooltip.hidden = false;
  tooltip.style.left = `${Math.min(ev.clientX + 14, innerWidth - tooltip.offsetWidth - 8)}px`;
  tooltip.style.top = `${Math.min(ev.clientY + 14, innerHeight - tooltip.offsetHeight - 8)}px`;
}
const sinTip = () => { tooltip.hidden = true; };
function conTips(raiz) {
  raiz.querySelectorAll("[data-tip]").forEach((el) => {
    el.addEventListener("mousemove", (e) => tip(e, el.dataset.tip));
    el.addEventListener("mouseleave", sinTip);
  });
}
function nivel(dim, v) {
  if (dim === "edad_4") return v === "65+" ? "65 y más" : v.replace("-", "–") + " años";
  return estado.etiquetas[dim]?.[v] ?? v;
}
// calificación del error total (TVD): mismas fronteras que el informe de F9/F11
function calificar(t) {
  if (t == null) return ["Sin predicción", "neutro"];
  if (t <= 0.05) return ["Muy bien", "bueno"];
  if (t <= 0.10) return ["Bien", "bueno"];
  if (t <= 0.20) return ["Regular", "aviso"];
  return ["Mal", "critico"];
}

// ------------------------------------------------------------------ cifras de la batería
function pintarCifras() {
  const r = estado.resumen;
  const c = estado.estudio ? r.estudios.find((e) => e.estudio === estado.estudio).cifras : r.total;
  const s = r.sin_escalas_dudosas;
  $("#val-cifras").innerHTML = `
    <div class="cifra"><b data-objetivo="${100 * c.tvd_media}">${pts(c.tvd_media)}</b><span>puntos de error medio<br><small>(TVD media, ${c.con_prediccion} preguntas)</small></span></div>
    <div class="cifra"><b>${pct(c.bajo_10_puntos)}</b><span>de las preguntas con<br>menos de 10 puntos de error</span></div>
    <div class="cifra"><b>${pct(c.opciones_dentro_margen)}</b><span>de las respuestas dentro del<br>margen de muestreo del CIS</span></div>
    ${estado.estudio ? "" : `<div class="cifra cifra-nota"><b>${pts(s.tvd_media)}</b><span>sin las escalas 1-10 de<br>codificación dudosa (D-089)</span></div>`}`;
}

// ------------------------------------------------------------------ lista
function pintarEstudios() {
  const cont = $("#val-estudios");
  const opciones = [{ estudio: "", fecha: "Todos" }, ...estado.resumen.estudios];
  cont.innerHTML = opciones.map((e) => `<button type="button" aria-pressed="${e.estudio === estado.estudio}" data-e="${e.estudio}">${e.estudio ? `${mesLargo(e.fecha)}` : "Todos"}${e.estudio ? `<small>${e.uso.startsWith("eval") ? "final" : "validación"}</small>` : ""}</button>`).join("");
  cont.querySelectorAll("button").forEach((b) => b.addEventListener("click", () => { estado.estudio = b.dataset.e; pintarEstudios(); pintarCifras(); pintarLista(); }));
}
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
const mesLargo = (f) => `${MESES[+f.slice(5, 7) - 1]} ${f.slice(0, 4)}`;

function preguntasFiltradas() {
  let qs = estado.resumen.estudios.filter((e) => !estado.estudio || e.estudio === estado.estudio)
    .flatMap((e) => e.preguntas.map((q, i) => ({ ...q, estudio: e.estudio, fecha: e.fecha, orden: i })));
  if (estado.tipo) qs = qs.filter((q) => (estado.tipo === "politica") === q.politica);
  if (estado.texto) { const t = estado.texto.toLowerCase(); qs = qs.filter((q) => q.enunciado.toLowerCase().includes(t)); }
  if (estado.orden !== "cuestionario") qs.sort((a, b) => ((a.tvd ?? 9) - (b.tvd ?? 9)) * (estado.orden === "mejor" ? 1 : -1));
  return qs;
}
function pintarLista() {
  const qs = preguntasFiltradas();
  $("#val-cuenta").textContent = `${qs.length} preguntas`;
  $("#val-preguntas").innerHTML = qs.map((q) => {
    const [txt, color] = calificar(q.tvd);
    return `<li><button type="button" data-id="${escapar(q.id)}" aria-current="${q.id === estado.sel}">
      <span class="vp-texto">${escapar(q.enunciado)}</span>
      <span class="vp-meta">${mesLargo(q.fecha)} · ${q.politica ? "política" : "vida cotidiana"}${q.duda ? ' · <span class="etiqueta-duda">escala dudosa</span>' : ""}</span>
      <span class="vp-error estado-${color}" title="${txt}">${q.tvd == null ? "—" : pts(q.tvd)}</span></button></li>`;
  }).join("");
  $("#val-preguntas").querySelectorAll("button").forEach((b) => b.addEventListener("click", () => abrir(b.dataset.id)));
}

// ------------------------------------------------------------------ detalle
async function abrir(id) {
  estado.sel = id;
  pintarLista();
  const caja = $("#val-detalle");
  caja.innerHTML = '<div class="esqueleto" aria-hidden="true"><i class="e-titulo"></i><i class="e-chips"></i><i class="e-barra"></i><i class="e-barra"></i><i class="e-barra"></i><i class="e-bloque"></i></div>';
  try {
    const d = await api(`/api/validacion?id=${encodeURIComponent(id)}`);
    estado.detalle = d;
    const dims = [...new Set(d.grupos?.map((g) => g.dimension) || [])];
    estado.dim = dims.includes(estado.dim) ? estado.dim : dims[0];
    const sust = d.opciones.map((o, j) => [o, j]).filter(([o]) => !NSNC.has(o));
    estado.opcion = sust.sort((a, b) => d.observado.p[b[1]] - d.observado.p[a[1]])[0]?.[1] ?? 0;
    pintarDetalle();
    history.replaceState(null, "", `#${encodeURIComponent(id)}`);
    if (innerWidth < 900) caja.scrollIntoView({ behavior: "smooth" });
  } catch (e) {
    caja.innerHTML = `<p class="aviso">No se pudo cargar: ${escapar(e.message)}</p>`;
  }
}

function pista(prev, ic80, obs, ic95o) {
  const banda = ic95o ? `<span class="v-real-banda" style="left:${100 * ic95o[0]}%;width:${100 * (ic95o[1] - ic95o[0])}%"></span>` : "";
  const r80 = ic80 ? `<span class="v-ic80" style="left:${100 * ic80[0]}%;width:${100 * (ic80[1] - ic80[0])}%"></span>` : "";
  return `<span class="v-pista">${banda}${r80}<span class="v-prev" style="width:${100 * prev}%"></span><span class="v-real" style="left:calc(${100 * obs}% - 1.5px)"></span></span>`;
}

function pintarDetalle() {
  const d = estado.detalle;
  const caja = $("#val-detalle");
  if (!d.previsto) {
    caja.innerHTML = `<h3>${escapar(d.enunciado)}</h3><p class="aviso">${escapar(d.metodo)}</p>`;
    return;
  }
  const [txt, color] = calificar(d.tvd);
  const dentro = d.dentro_margen.filter(Boolean).length;
  const filas = d.opciones.map((o, j) => {
    const p = d.previsto.p[j], y = d.observado.p[j], dif = p - y;
    const fuera = !d.dentro_margen[j];
    return `<div class="etiqueta" title="${escapar(limpia(o))}">${escapar(limpia(o))}</div>
      <div data-tip="<b>${escapar(limpia(o))}</b><br>Previsto: ${pct(p, 1)}${d.previsto.ic80 ? ` (IC 80 %: ${pct(d.previsto.ic80[j][0], 1)} – ${pct(d.previsto.ic80[j][1], 1)})` : ""}<br>Real (CIS): ${pct(y, 1)} (margen 95 %: ${pct(d.observado.ic95[j][0], 1)} – ${pct(d.observado.ic95[j][1], 1)})">${pista(p, d.previsto.ic80?.[j], y, d.observado.ic95[j])}</div>
      <div class="v-num">${pct(p)}</div><div class="v-num v-num-real">${pct(y)}</div>
      <div class="v-dif ${fuera ? "fuera" : ""}">${dif >= 0 ? "+" : ""}${pts(dif)}</div>`;
  }).join("");
  const est = d.estudio;
  caja.innerHTML = `
    <h3>${escapar(d.enunciado)}</h3>
    <div class="metas"><span>Barómetro de ${mesLargo(est.fecha)} · estudio ${escapar(est.estudio)}</span><span>${d.observado.n.toLocaleString("es-ES")} encuestados</span><span>${escapar(METODO[d.metodo] || d.metodo)}</span>${d.similitud_max != null ? `<span>Similitud con el banco: ${pct(d.similitud_max)}</span>` : ""}</div>
    ${d.duda ? `<p class="aviso">Escala 1-10 con codificación dudosa en los datos de entrada (${d.duda}): este error no es fiable hasta revisarla.</p>` : ""}
    <div class="veredicto estado-borde-${color}">
      <div class="veredicto-cifra"><b>${pts(d.tvd)}</b><span>puntos de error</span></div>
      <div><span class="veredicto-etiqueta estado-${color}">${txt}</span>
      <p>Para pasar de lo previsto a lo que midió el CIS habría que mover <b>${pts(d.tvd)} puntos</b> de respuesta de unas opciones a otras. ${dentro} de ${d.opciones.length} respuestas caen dentro del margen de muestreo de la encuesta${d.previsto.confianza != null ? `; la confianza que declaraba el sistema era del ${pct(d.previsto.confianza)}` : ""}.</p></div>
    </div>
    <h4 class="seccion-titulo">Previsto frente a real</h4>
    <div class="v-barras"><span></span><span></span><span class="v-cab">Previsto</span><span class="v-cab">Real</span><span class="v-cab">Dif.</span>${filas}</div>
    <div class="leyenda-barras"><span><i style="background:var(--serie)"></i>Previsto</span><span><i style="background:var(--rango)"></i>Intervalo del 80 % previsto</span><span><i class="ley-real"></i>Real (CIS)</span><span><i style="background:rgba(11,11,11,0.12)"></i>Margen de muestreo del CIS (95 %)</span></div>
    <p class="nota">Diferencia en puntos; en rojo, las que salen del margen de muestreo de la encuesta.</p>
    ${seccionGrupos(d)}
    ${seccionImportancia(d)}
    ${seccionFuentes(d)}`;
  conTips(caja);
  activarGrupos();
}

function seccionGrupos(d) {
  if (!d.grupos?.length) return `<h4 class="seccion-titulo">Por grupos</h4><p class="nota">Sin grupos con datos suficientes.</p>`;
  const dims = [...new Set(d.grupos.map((g) => g.dimension))];
  const media = (dim) => { const v = d.grupos.filter((g) => g.dimension === dim).map((g) => g.tvd); return v.reduce((a, b) => a + b, 0) / v.length; };
  return `<h4 class="seccion-titulo">Por grupos: ¿acierta en cada grupo?</h4>
    <div class="dimensiones" id="v-dims">${dims.map((x) => `<button type="button" aria-pressed="${x === estado.dim}" data-d="${x}" title="Error medio en sus grupos: ${pts(media(x))} puntos">${NOMBRES_DIM[x] || x}<small>${pts(media(x))}</small></button>`).join("")}</div>
    <label class="fila-opcion">Respuesta <select id="v-opcion">${d.opciones.map((o, j) => `<option value="${j}" ${j === estado.opcion ? "selected" : ""}>${escapar(limpia(o))}</option>`).join("")}</select></label>
    <div id="v-grupos"></div>`;
}
function pintarGrupos() {
  const d = estado.detalle, j = estado.opcion;
  const gs = d.grupos.filter((g) => g.dimension === estado.dim);
  const filas = gs.map((g) => {
    const p = g.previsto[j], y = g.observado[j], [a, b] = g.ic95_observado[j];
    const fuera = p < a - 1e-9 || p > b + 1e-9;
    const lo = Math.min(p, y), w = Math.abs(p - y);
    return `<div class="vg-nombre">${escapar(nivel(g.dimension, g.nivel))}<small>${g.n.toLocaleString("es-ES")} enc.</small></div>
      <div class="vg-pista" data-tip="<b>${escapar(nivel(g.dimension, g.nivel))}</b> · ${escapar(limpia(d.opciones[j]))}<br>Previsto: ${pct(p, 1)}<br>Real: ${pct(y, 1)} (margen 95 %: ${pct(a, 1)} – ${pct(b, 1)}; ${g.n} encuestados)<br>Error del grupo en toda la pregunta: ${pts(g.tvd)} puntos${g.confianza != null ? `<br>Confianza declarada: ${pct(g.confianza)}` : ""}">
        <span class="v-real-banda" style="left:${100 * a}%;width:${100 * (b - a)}%"></span>
        <span class="vg-union" style="left:${100 * lo}%;width:${100 * w}%"></span>
        <span class="vg-real" style="left:calc(${100 * y}% - 5px)"></span>
        <span class="vg-prev" style="left:calc(${100 * p}% - 5px)"></span>
      </div>
      <div class="v-num">${pct(p)}</div><div class="v-num v-num-real">${pct(y)}</div>
      <div class="v-dif ${fuera ? "fuera" : ""}">${p - y >= 0 ? "+" : ""}${pts(p - y)}</div>
      <div class="v-num vg-tvd">${pts(g.tvd)}</div>`;
  }).join("");
  $("#v-grupos").innerHTML = `<div class="vg-tabla"><span></span><span class="v-cab vg-escala"><i>0 %</i><i>50 %</i><i>100 %</i></span><span class="v-cab">Previsto</span><span class="v-cab">Real</span><span class="v-cab">Dif.</span><span class="v-cab" title="Error (TVD) del grupo en todas las respuestas">Error</span>${filas}</div>
    <div class="leyenda-barras"><span><i class="ley-punto prev"></i>Previsto</span><span><i class="ley-punto real"></i>Real (CIS)</span><span><i style="background:rgba(11,11,11,0.12)"></i>Margen de muestreo del grupo (95 %)</span></div>
    <p class="nota">Cada grupo, con su número de encuestados del CIS: cuantos menos, más ancho el margen de lo real. «Error» es el de todas las respuestas del grupo (TVD, en puntos). Los grupos con menos de 50 encuestados no se muestran.</p>`;
  conTips($("#v-grupos"));
}
function activarGrupos() {
  if (!$("#v-dims")) return;
  $("#v-dims").querySelectorAll("button").forEach((b) => b.addEventListener("click", () => {
    estado.dim = b.dataset.d;
    $("#v-dims").querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    pintarGrupos();
  }));
  $("#v-opcion").addEventListener("change", (e) => { estado.opcion = +e.target.value; pintarGrupos(); });
  pintarGrupos();
}

function seccionImportancia(d) {
  const prev = d.importancia?.prevista || [], obs = d.importancia?.observada || [];
  if (!prev.length && !obs.length) return "";
  const dims = [...new Set([...obs.map((x) => x.dimension), ...prev.map((x) => x.dimension)])];
  const f = (lista, dim) => lista.find((x) => x.dimension === dim)?.fuerza ?? 0;
  const max = Math.max(0.05, ...dims.flatMap((x) => [f(prev, x), f(obs, x)]));
  const filas = dims.map((x) => `<div class="etiqueta">${NOMBRES_DIM[x] || x}</div>
    <div class="imp-barras" data-tip="<b>${NOMBRES_DIM[x] || x}</b><br>Fuerza prevista: ${f(prev, x).toFixed(2).replace(".", ",")}<br>Fuerza real: ${f(obs, x).toFixed(2).replace(".", ",")}">
      <span class="imp-prev" style="width:${(100 * f(prev, x)) / max}%"></span><span class="imp-obs" style="width:${(100 * f(obs, x)) / max}%"></span></div>
    <div class="v-num">${f(prev, x).toFixed(2).replace(".", ",")}</div><div class="v-num v-num-real">${f(obs, x).toFixed(2).replace(".", ",")}</div>`).join("");
  const top = obs[0], posPrev = top ? prev.findIndex((x) => x.dimension === top.dimension) + 1 : 0;
  const frase = top ? `En la realidad, lo que más separó las respuestas fue <b>${NOMBRES_DIM[top.dimension] || top.dimension}</b>: «${escapar(limpia(top.opcion))}» fue del ${pct(top.valor_bajo)} (${escapar(nivel(top.dimension, top.grupo_bajo))}) al ${pct(top.valor_alto)} (${escapar(nivel(top.dimension, top.grupo_alto))}). ${posPrev === 1 ? "La predicción también la ponía en primer lugar." : posPrev ? `La predicción la ponía en el puesto ${posPrev}.` : ""}` : "";
  return `<h4 class="seccion-titulo">¿De qué depende la respuesta?</h4>
    <p class="destacado-texto">${frase}</p>
    <div class="imp-tabla"><span></span><span></span><span class="v-cab">Previsto</span><span class="v-cab">Real</span>${filas}</div>
    <div class="leyenda-barras"><span><i style="background:var(--serie)"></i>Fuerza según la predicción</span><span><i style="background:#3d3c38"></i>Fuerza en la encuesta real</span></div>
    <p class="nota">Fuerza (η): cuánto separan las respuestas los grupos de cada variable; 0 si todos responden igual. En lo real se descuenta el ruido de muestreo de cada grupo. Es descriptiva, no causal. ${d.metodo === "llm_anclado" ? "El modelo de lenguaje solo estima por edad, sexo, estudios y comunidad." : ""}</p>`;
}

function seccionFuentes(d) {
  const an = (d.analogas || []).map((a) => `<li>${escapar(a.enunciado)} <small>CIS, estudio ${escapar(a.estudio)} (${mesLargo(a.fecha + "-01")}) · similitud ${pct(a.similitud)} · peso ${pct(a.peso)}</small></li>`).join("");
  const fu = (d.estudio.fuentes || []).map((f) => `<li><a href="${escapar(f.url)}" target="_blank" rel="noopener">${escapar(f.tipo)} del estudio ${escapar(d.estudio.estudio)}</a> <small>${escapar(f.condiciones || "")}</small></li>`).join("");
  return `<h4 class="seccion-titulo">En qué se basa</h4>
    ${d.metodo === "analogas" ? `<p class="nota">La predicción se hizo con estas preguntas anteriores del banco del CIS (sin ver la encuesta de ${mesLargo(d.estudio.fecha)}), ajustadas al perfil de la población sintética:</p><ol class="parecidas">${an}</ol>` : ""}
    ${d.justificacion_llm ? `<p class="nota">Sin preguntas parecidas fiables, respondió el modelo de lenguaje anclado en el banco. Su razonamiento:</p><p class="justificacion">«${escapar(d.justificacion_llm)}»</p>` : ""}
    <p class="nota">Lo real sale del estudio ${escapar(d.estudio.estudio)} del CIS: respuestas ponderadas de los españoles de 18 años o más (${d.observado.n.toLocaleString("es-ES")} encuestados; tamaño efectivo ${d.observado.n_efectivo.toLocaleString("es-ES")} por la ponderación).</p>
    <ul class="fuentes">${fu}</ul>`;
}

function pintarMetodo() {
  const r = estado.resumen;
  const dims = Object.entries(r.por_dimension).sort((a, b) => a[1].error - b[1].error);
  $("#val-metodo").innerHTML = `
    <ul class="val-lista-metodo">
      <li><b>Sin mirar la respuesta.</b> ${escapar(r.metodo)} Ninguno de estos resultados se ha usado para ajustar el sistema (regla 5 de CLAUDE.md): julio y septiembre son la ventana de validación (F9-F10) y octubre la evaluación final, ejecutada una sola vez (F11, reports/fase_11.md).</li>
      <li><b>Error (puntos).</b> Distancia de variación total (TVD) × 100: la mitad de la suma de las diferencias absolutas entre lo previsto y lo real. Son los puntos de respuesta que habría que mover para que coincidieran. Menos de 5, muy bien; menos de 10, bien.</li>
      <li><b>Margen de muestreo.</b> Lo real también tiene error: una encuesta de unas 4.000 personas. El margen del 95 % usa el tamaño efectivo de Kish (la ponderación lo reduce). En los grupos pequeños es ancho.</li>
      <li><b>Grupos.</b> Ocho variables del perfil que tienen a la vez la población sintética y los encuestados del CIS. Lo previsto para cada grupo es la población sintética de ese grupo; lo real, los encuestados del grupo.</li>
      <li><b>Importancia de las variables.</b> Fuerza de la asociación η (predict/importancia.py, D-090).</li>
      <li><b>Escalas dudosas.</b> Las escalas 1-10 de valoración de líderes y ministros tienen un problema de codificación en los datos de entrada (D-089); su error no es fiable hasta revisarlas.</li>
    </ul>
    <h4 class="seccion-titulo">¿Acierta en los subgrupos? Error medio en los grupos, por variable</h4>
    <div class="dim-errores">${dims.map(([d, v]) => `<div title="${v.grupos} grupos-pregunta"><span>${NOMBRES_DIM[d] || d}</span><span class="de-barra"><i class="de-err" style="width:${Math.min(100, 600 * v.error)}%"></i><i class="de-ruido" style="width:${Math.min(100, 600 * v.ruido_muestreo)}%"></i></span><b>${pts(v.error)}</b><small>ruido ${pts(v.ruido_muestreo)}</small></div>`).join("")}</div>
    <p class="nota">Puntos de error (TVD) medios en los grupos de cada variable, sin las escalas dudosas (D-089), y la parte que se espera solo por el <b>ruido de muestreo de lo real</b> (cada grupo tiene pocos cientos de encuestados del CIS). El error del total en esas mismas preguntas es de ${pts(r.sin_escalas_dudosas.tvd_media)} puntos: en los grupos se suma, sobre todo, ese mismo desvío más el ruido de la encuesta, no un fallo propio de los grupos.</p>
    <p class="nota">Batería generada el ${escapar(r.generado)} con <code>python -m sinpop.evaluate.bateria</code> · datos hasta ${escapar(r.corte_datos)}.</p>`;
}

// ------------------------------------------------------------------ arranque
$("#val-buscar").addEventListener("input", (e) => { estado.texto = e.target.value; pintarLista(); });
$("#val-tipo").addEventListener("change", (e) => { estado.tipo = e.target.value; pintarLista(); });
$("#val-orden").addEventListener("change", (e) => { estado.orden = e.target.value; pintarLista(); });
(async function iniciar() {
  try {
    const [r, et] = await Promise.all([api("/api/validacion"), api("/api/etiquetas")]);
    estado.resumen = r;
    estado.etiquetas = et;
    pintarEstudios();
    pintarCifras();
    pintarLista();
    pintarMetodo();
    const inicial = decodeURIComponent(location.hash.slice(1)) || r.estudios[0]?.preguntas.find((q) => q.tvd != null && !q.duda)?.id;
    if (inicial) abrir(inicial);
  } catch (e) {
    $("#val-detalle").innerHTML = `<p class="aviso">No se pudo cargar la batería: ${escapar(e.message)}</p>`;
  }
})();
// un enlace con #id abre esa pregunta (también al cambiarlo sin recargar)
addEventListener("hashchange", () => {
  const id = decodeURIComponent(location.hash.slice(1));
  if (id && id !== estado.sel) abrir(id);
});
window.sinpopValidacion = { estado, abrir };
