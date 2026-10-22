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
DESTINO = Path(__file__).parent / "web" / "territorios.geojson"


def construir() -> dict:
    import geopandas as gpd

    g = gpd.read_file(f"zip://{ZIP}!{CAPA}")[["CPRO", "NPRO", "CCA", "NCA", "geometry"]]
    g["geometry"] = g.buffer(0)
    out = []
    for nivel, cod, nom in [("PROV", "CPRO", "NPRO"), ("CCAA", "CCA", "NCA")]:
        d = g.dissolve(by=cod, aggfunc={nom: "first"}).reset_index()
        d["geometry"] = d.simplify(TOLERANCIA_M, preserve_topology=True)
        d = d.to_crs(4326)
        for r in d.itertuples():
            out.append(
                {
                    "type": "Feature",
                    "properties": {
                        "nivel": nivel,
                        "codigo": getattr(r, cod),
                        "territorio": f"{nivel}:{getattr(r, cod)}",
                        "nombre": getattr(r, nom),
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
