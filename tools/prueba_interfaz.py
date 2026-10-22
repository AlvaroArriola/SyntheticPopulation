"""Pruebas de extremo a extremo de la interfaz (F14: G14.1-G14.3) con un navegador real.

Necesita el servicio en marcha (`sinpop serve`) y Playwright para Python con un Chromium local.
Recorre las pantallas de pregunta (España y una comunidad), evento y exploración; comprueba en el
DOM que ninguna cifra sale sin intervalo ni confianza y que el aviso de simulación está siempre
(G14.2); pasa axe-core para la accesibilidad (G14.3); y guarda capturas en `reports/fase_14/`.

Uso: `python tools/prueba_interfaz.py [url] [chromium]`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "reports" / "fase_14"
AXE = Path(__file__).parent / "vendor" / "axe.min.js"
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PREGUNTA = "¿Cómo calificaría usted la situación económica actual de España?"

COMPROBAR_RESULTADO = """() => {
  const r = document.querySelector('#resultado');
  const pistas = [...r.querySelectorAll('.pista')];
  const sinIntervalo = pistas.filter(p => !(p.querySelector('.ic80') && p.querySelector('.ic95'))).length;
  const celdas = [...r.querySelectorAll('.tabla-calor td')];
  const sinConfianza = celdas.filter(td => td.dataset.c === undefined || td.dataset.c === '').length;
  return {
    barras: pistas.length,
    barras_sin_intervalo: sinIntervalo,
    confianza_total: !!r.querySelector('.confianza [role=meter]'),
    celdas: celdas.length,
    celdas_sin_confianza: sinConfianza,
    aviso: (r.querySelector('.aviso')?.textContent || '').includes('simulado'),
  };
}"""


def main(url: str = "http://127.0.0.1:8000", chromium: str = CHROMIUM) -> dict:
    from playwright.sync_api import sync_playwright

    DESTINO.mkdir(parents=True, exist_ok=True)
    res: dict = {"pantallas": {}, "errores_js": []}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chromium)
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.on("pageerror", lambda e: res["errores_js"].append(str(e)))
        pg.goto(url, wait_until="domcontentloaded")
        pg.wait_for_function(
            "window.sinpop && document.querySelectorAll('.leaflet-interactive').length > 0"
        )
        pg.wait_for_timeout(800)
        pg.screenshot(path=DESTINO / "1_inicio.png")

        # pregunta sobre España
        pg.fill("#enunciado", PREGUNTA)
        pg.wait_for_selector("#sugerencias:not([hidden]) li", timeout=20000)
        pg.screenshot(path=DESTINO / "2_sugerencias.png")
        pg.click("#preguntar")
        pg.wait_for_selector("#resultado:not([hidden]) .barras", timeout=600000)
        pg.wait_for_timeout(500)
        res["pantallas"]["pregunta_es"] = pg.evaluate(COMPROBAR_RESULTADO)
        pg.screenshot(path=DESTINO / "3_resultado.png")
        pg.select_option("#opcion-mapa", "3")
        pg.wait_for_timeout(800)
        res["pantallas"]["mapa_coloreado"] = pg.evaluate(
            "() => !document.querySelector('#leyenda-mapa').hidden"
        )
        pg.screenshot(path=DESTINO / "4_mapa_coloreado.png")

        # accesibilidad (axe-core) sobre la pantalla con resultados
        pg.add_script_tag(path=str(AXE))
        axe = pg.evaluate(
            "async () => (await axe.run(document, {resultTypes: ['violations']})).violations"
            ".map(v => ({id: v.id, impacto: v.impact, nodos: v.nodes.length}))"
        )
        res["accesibilidad"] = axe

        # una comunidad (Madrid) con su propia población
        pg.evaluate(
            "() => { window.sinpop.ponerNivel('CCAA'); window.sinpop.elegirTerritorio('CCAA:13', 'Madrid, Comunidad de'); }"
        )
        pg.wait_for_timeout(500)
        pg.click("#tamanos button:has-text('100 mil')")
        pg.wait_for_timeout(300)
        lista = pg.evaluate("() => !document.querySelector('#preguntar').disabled")
        res["pantallas"]["comunidad_lista"] = lista
        if lista:
            pg.click("#preguntar")
            pg.wait_for_function(
                "document.querySelector('#resultado .metas')?.textContent.includes('Madrid')",
                timeout=600000,
            )
            pg.wait_for_timeout(500)
            res["pantallas"]["pregunta_comunidad"] = pg.evaluate(COMPROBAR_RESULTADO)
            pg.screenshot(path=DESTINO / "5_comunidad.png")

        # evento
        pg.click("#tab-evento")
        pg.fill(
            "#evento-descripcion",
            "El Gobierno anuncia una subida general de impuestos sobre la renta",
        )
        pg.click("#preguntar")
        pg.wait_for_function(
            "document.querySelector('#resultado .metas')?.textContent.includes('Evento')",
            timeout=600000,
        )
        pg.wait_for_timeout(500)
        res["pantallas"]["evento"] = pg.evaluate(
            "() => ({filas: document.querySelectorAll('#resultado .pista').length,"
            " aviso: [...document.querySelectorAll('#resultado .aviso')].some(a => a.textContent.includes('simulado'))})"
        )
        pg.screenshot(path=DESTINO / "6_evento.png")

        # modo oscuro y móvil
        pg.evaluate("document.documentElement.dataset.theme='dark'")
        pg.wait_for_timeout(400)
        pg.screenshot(path=DESTINO / "7_oscuro.png")
        movil = b.new_page(viewport={"width": 390, "height": 844})
        movil.goto(url, wait_until="domcontentloaded")
        movil.wait_for_timeout(2500)
        res["movil_sin_scroll_horizontal"] = movil.evaluate(
            "() => document.documentElement.scrollWidth <= window.innerWidth + 1"
        )
        movil.screenshot(path=DESTINO / "8_movil.png", full_page=True)
        b.close()

    pr = res["pantallas"]
    g2 = [pr[k] for k in ("pregunta_es", "pregunta_comunidad") if k in pr]
    graves = [v for v in res["accesibilidad"] if v["impacto"] in ("critical", "serious")]
    res["g14_1"] = bool(
        "pregunta_es" in pr
        and pr.get("mapa_coloreado")
        and pr.get("evento", {}).get("filas")
        and not res["errores_js"]
    )
    res["g14_2"] = all(
        x["barras"] > 0
        and x["barras_sin_intervalo"] == 0
        and x["confianza_total"]
        and x["celdas_sin_confianza"] == 0
        and x["aviso"]
        for x in g2
    ) and pr.get("evento", {}).get("aviso", False)
    res["g14_3"] = not graves
    (DESTINO / "prueba_interfaz.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), "utf-8"
    )
    return res


if __name__ == "__main__":
    print(json.dumps(main(*sys.argv[1:]), ensure_ascii=False, indent=1))
