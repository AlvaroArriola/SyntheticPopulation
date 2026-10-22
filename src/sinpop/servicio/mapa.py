"""Límites de provincias y comunidades para el mapa de la interfaz (F14).

Se agregan los contornos oficiales de las secciones censales del INE (`cartografia_secciones`,
edición 2024) por código de provincia (`CPRO`) y de comunidad (`CCA`): los mismos códigos INE que
usa todo el proyecto, sin tablas de correspondencia inventadas. Se simplifican para la web
(tolerancia `TOLERANCIA_M` metros) y se pasan a WGS84 (EPSG:4326), que es lo que espera Leaflet
sobre las teselas de OpenStreetMap.

Comando: `python -m sinpop.servicio.mapa` → `src/sinpop/servicio/web/territorios.geojson`.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from sinpop import RAW_DIR

ZIP = RAW_DIR / "cartografia_secciones" / "2024" / "seccionado_2024.zip"
CAPA = "SECC_CE_20240101.shp"
TOLERANCIA_M = 600
# las secciones no encajan al milímetro: al disolverlas quedan rendijas y huecos diminutos que en el
# mapa se ven como manchas. Se cierran con un búfer de ida y vuelta y se quitan los huecos y las
# piezas por debajo de estos tamaños; los enclaves reales (Treviño, Petilla de Aragón, Llívia…)
# son mucho mayores y se conservan.
CIERRE_M = 60
HUECO_MIN_M2 = 5e6
PIEZA_MIN_M2 = 2e5
DESTINO = Path(__file__).parent / "web" / "territorios.geojson"


def nombre_natural(n: str) -> str:
    """«Palmas, Las» → «Las Palmas»: los nombres del INE llevan el artículo pospuesto."""
    m = re.fullmatch(r"(.+), (La|Las|El|Los|Les|L'|A|O|As|Os|Illes|Comunidad de|Comunitat)", n)
    if not m:
        return n
    sep = "" if m.group(2).endswith("'") else " "
    return f"{m.group(2)}{sep}{m.group(1)}"


def _limpiar(geom, otros, cerrar: bool = True):
    """Cierra rendijas y quita piezas diminutas. Un hueco se conserva solo si es grande y lo ocupa
    otro territorio (un enclave); los huecos vacíos son zonas sin secciones censales (territorios
    mancomunados sin municipio, como las Bardenas Reales) y se rellenan con el que los rodea."""
    from shapely.geometry import MultiPolygon, Polygon

    if cerrar:
        geom = geom.buffer(CIERRE_M).buffer(-CIERRE_M)
    piezas = []
    for p in getattr(geom, "geoms", [geom]):
        if p.geom_type != "Polygon" or p.area < PIEZA_MIN_M2:
            continue
        huecos = [
            h
            for h in p.interiors
            if Polygon(h).area >= HUECO_MIN_M2
            and Polygon(h).intersection(otros).area > 0.5 * Polygon(h).area
        ]
        piezas.append(Polygon(p.exterior, huecos))
    return MultiPolygon(piezas) if len(piezas) > 1 else piezas[0]


def construir() -> dict:
    import geopandas as gpd
    from shapely.ops import unary_union

    g = gpd.read_file(f"zip://{ZIP}!{CAPA}")[["CPRO", "NPRO", "CCA", "NCA", "geometry"]]
    g["geometry"] = g.buffer(0)
    out = []
    for nivel, cod, nom in [("PROV", "CPRO", "NPRO"), ("CCAA", "CCA", "NCA")]:
        d = g.dissolve(by=cod, aggfunc={nom: "first"}).reset_index()
        geoms = list(d.geometry)
        d["geometry"] = [
            _limpiar(gm, unary_union(geoms[:i] + geoms[i + 1 :])) for i, gm in enumerate(geoms)
        ]
        d["geometry"] = d.simplify(TOLERANCIA_M, preserve_topology=True).make_valid()
        # segunda pasada: la simplificación puede partir un hueco vacío en otros más pequeños
        geoms = list(d.geometry)
        d["geometry"] = [
            _limpiar(gm, unary_union(geoms[:i] + geoms[i + 1 :]), cerrar=False)
            for i, gm in enumerate(geoms)
        ]
        d = d.to_crs(4326)
        for r in d.itertuples():
            out.append(
                {
                    "type": "Feature",
                    "properties": {
                        "nivel": nivel,
                        "codigo": getattr(r, cod),
                        "territorio": f"{nivel}:{getattr(r, cod)}",
                        "nombre": nombre_natural(getattr(r, nom)),
                    },
                    "geometry": json.loads(gpd.GeoSeries([r.geometry]).to_json())["features"][0][
                        "geometry"
                    ],
                }
            )
    fc = {
        "type": "FeatureCollection",
        "fuente": "INE, Cartografía digitalizada de secciones censales 2024 (agregada)",
        "features": out,
    }
    texto = json.dumps(fc, ensure_ascii=False, separators=(",", ":"))
    # redondeo de coordenadas a 4 decimales (~10 m) para aligerar el fichero
    texto = re.sub(r"(-?\d+\.\d{4})\d+", r"\1", texto)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(texto, "utf-8")
    return {"provincias": sum(f["properties"]["nivel"] == "PROV" for f in out), "bytes": len(texto)}


if __name__ == "__main__":
    print(construir())
