"""Familia de cada candidatura de las últimas elecciones autonómicas.

Clave: (código de comunidad autónoma, nombre de la candidatura tal como figura en el boletín
oficial y en ``data/interim/elecciones_autonomicas_votos.parquet``, sin corregir erratas).
Valor: (familia, nota o None).

Se aplican los criterios aprobados en D-030 y D-032, iguales para todos los electorados, y
las candidaturas de las generales de 2023 ya clasificadas en ``configs/partidos.yaml`` sirven
de precedente para que el mismo partido tenga la misma familia en todas las elecciones:

1. Partidos estatales: por su posición si han tenido representación en el Congreso o en el
   Parlamento Europeo desde 2015; si no, «otros».
2. Federaciones, marcas territoriales y coaliciones encabezadas por un partido estatal: la
   familia de ese partido.
3. Partidos de una sola comunidad, provincia o municipio sin vínculo con un partido estatal:
   nacionalistas y regionalistas.
4. Listas de un solo territorio cuyo nombre indica claramente un partido no regional: «otros»
   (D-032).

Las listas cuyo nombre no se ha podido identificar con certeza se clasifican por su ámbito
y lo dicen en la nota; no se adivina su posición.
"""

FAMILIAS_AUTONOMICAS: dict[tuple[str, str], tuple[str, str | None]] = {
    # 01 Andalucía
    ("01", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("01", "PARTIDO SOCIALISTA OBRERO ESPAÑOL DE ANDALUCÍA"): (
        "socialdemocrata",
        "federación del PSOE en Andalucía",
    ),
    ("01", "VOX"): ("derecha_radical", None),
    ("01", "ADELANTE ANDALUCIA"): ("nacionalista_regionalista", None),
    (
        "01",
        "POR ANDALUCIA-IZQUIERDA UNIDA-PODEMOS-MOVIMIENTO SUMAR-INICIATIVA DEL PUEBLO ANDALUZ"
        "-VERDES EQUO-ALTERNATIVA REPUBLICANA-ALIANZA VERDE",
    ): ("izquierda_estatal", "coalición de IU, Podemos, Sumar y otros en Andalucía"),
    ("01", "SE ACABÓ LA FIESTA"): ("derecha_radical", None),
    ("01", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("01", "100X100 UNIDOS"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("01", "ANDALUCISTAS PUEBLO ANDALUZ"): ("nacionalista_regionalista", None),
    ("01", "ESCAÑOS EN BLANCO"): ("otros", None),
    ("01", "JAÉN MERECE MÁS"): ("nacionalista_regionalista", None),
    ("01", "PARTIDO COMUNISTA DEL PUEBLO ANDALUZ"): (
        "otros",
        "organización del PCPE en Andalucía (partido estatal sin representación)",
    ),
    ("01", "FALANGE ESPAÑOLA DE LAS JONS"): ("otros", None),
    ("01", "POR UN MUNDO MÁS JUSTO"): ("otros", None),
    ("01", "PARITDO AUTÓNOMOS"): ("otros", "nombre no regional (D-032); errata del boletín"),
    ("01", "NACIÓN ANDALUZA"): ("nacionalista_regionalista", None),
    ("01", "HUELVA EXISTE"): ("nacionalista_regionalista", None),
    ("01", "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"): ("otros", None),
    ("01", "PODER ANDAlUZ"): ("nacionalista_regionalista", "errata del boletín («ANDAlUZ»)"),
    ("01", "ALTERNATIVA MALAGUEÑA"): ("nacionalista_regionalista", None),
    ("01", "ALMERIENSES REGIONALISTAS PRO ALMERÍA"): ("nacionalista_regionalista", None),
    ("01", "PARTIDO ANDALUSÍ"): ("nacionalista_regionalista", None),
    ("01", "IZQUIERDA ANTICAPITALISTA REVOLUCIONARIA"): (
        "otros",
        "partido estatal sin representación (IZAR)",
    ),
    ("01", "PARTIDO DE JUBILADOS POR EL FUTURO, DIGNIDAD Y DEMOCRACIA"): (
        "otros",
        "nombre no regional (D-032)",
    ),
    ("01", "IZQUIERDA POR ALMERIA"): ("nacionalista_regionalista", None),
    ("01", "CONECTA ANDALUCÍA"): ("nacionalista_regionalista", None),
    ("01", "SOCIEDAD UNIDA"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    # 02 Aragón
    ("02", "PP"): ("centro_derecha_estatal", None),
    ("02", "PSOE"): ("socialdemocrata", None),
    ("02", "VOX"): ("derecha_radical", None),
    ("02", "CHA"): ("nacionalista_regionalista", None),
    ("02", "EXISTE"): ("nacionalista_regionalista", None),
    ("02", "IU- MOVIMIENTO SUMAR"): ("izquierda_estatal", None),
    ("02", "SALF"): ("derecha_radical", None),
    ("02", "PAR"): ("nacionalista_regionalista", None),
    ("02", "PODEMOS -AV"): ("izquierda_estatal", None),
    ("02", "ESCAÑOS EN BLANCO"): ("otros", None),
    ("02", "PACMA"): ("otros", None),
    ("02", "MUNDO+JUSTO"): ("otros", None),
    ("02", "PCTE"): ("otros", None),
    ("02", "COALICIÓN ARAGONESA"): ("nacionalista_regionalista", None),
    ("02", "ETXSBC"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    # 03 Principado de Asturias
    ("03", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("03", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("03", "VOX"): ("derecha_radical", None),
    ("03", "CONVOCATORIA POR ASTURIES IU-MÁS PAÍS-IAS"): (
        "izquierda_estatal",
        "coalición encabezada por IU con Más País",
    ),
    ("03", "PODEMOS ASTURIES"): ("izquierda_estatal", None),
    ("03", "FORO ASTURIAS"): ("nacionalista_regionalista", None),
    ("03", "CIUDADANOS-PARTIDO DE LA CIUDADANIA"): ("centro_derecha_estatal", None),
    ("03", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("03", "SOS ASTURIAS-ESPAÑA VACIADA"): ("nacionalista_regionalista", None),
    ("03", "SOS OCCIDENTE- ESPAÑA VACIADA"): ("nacionalista_regionalista", None),
    ("03", "VERDES EQUO ASTURIAS"): ("izquierda_estatal", "marca territorial de EQUO"),
    ("03", "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"): ("otros", None),
    ("03", "ANDECHA ASTUR"): ("nacionalista_regionalista", None),
    ("03", "SUMA PRINCIPADO"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("03", "POR UN MUNDO MAS JUSTO"): ("otros", None),
    ("03", "PARTIDO UNIONISTA ESTADO DE ESPAÑA"): ("otros", "nombre no regional (D-032)"),
    # 04 Illes Balears
    ("04", "Partido Popular"): ("centro_derecha_estatal", None),
    ("04", "Partit Socialista de les Illes Balears"): (
        "socialdemocrata",
        "federación del PSOE en Illes Balears",
    ),
    ("04", "VOX"): ("derecha_radical", None),
    ("04", "MÉS per Mallorca"): ("nacionalista_regionalista", None),
    ("04", "Unidas Podemos"): ("izquierda_estatal", None),
    ("04", "El PI-Proposta per les Illes Balears"): ("nacionalista_regionalista", None),
    ("04", "MÉS per Menorca"): ("nacionalista_regionalista", None),
    ("04", "Ciudadanos-Partido de la Ciudadanía"): ("centro_derecha_estatal", None),
    ("04", "Progreso en Verde-PACMA"): ("otros", "coalición encabezada por PACMA"),
    ("04", "Sa Unió de Formentera (PP-Compromís)"): (
        "centro_derecha_estatal",
        "coalición del PP con Compromís amb Formentera; el PP figura primero",
    ),
    ("04", "Gent per Formentera + Partit Socialista de les Illes Balears"): (
        "nacionalista_regionalista",
        "coalición encabezada por Gent per Formentera (partido insular) con el PSIB",
    ),
    ("04", "Ara Eivissa"): ("nacionalista_regionalista", None),
    ("04", "Proyecto Liberal Español"): ("otros", "nombre no regional (D-032)"),
    ("04", "Coalició per Balears"): ("nacionalista_regionalista", None),
    ("04", "EPIC-El PI"): ("nacionalista_regionalista", "coalición con El PI"),
    ("04", "Reset-Reinicio Político"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("04", "Per Balears"): ("nacionalista_regionalista", None),
    ("04", "Nuevo Orden Nacional-Nou Ordre Nacional"): ("otros", "nombre no regional (D-032)"),
    # 05 Canarias
    ("05", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("05", "COALICIÓN CANARIA"): ("nacionalista_regionalista", None),
    ("05", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("05", "VOX"): ("derecha_radical", None),
    ("05", "NUEVA CANARIAS"): ("nacionalista_regionalista", None),
    ("05", "UNIDAS SÍ PODEMOS"): ("izquierda_estatal", None),
    ("05", "DRAGO VERDES CANARIAS"): ("nacionalista_regionalista", None),
    ("05", "UNIDOS POR GRAN CANARIA"): ("nacionalista_regionalista", None),
    ("05", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("05", "CIUDADANOS PARTIDO DE LA CIUDADANÍA"): ("centro_derecha_estatal", None),
    ("05", "AGRUPACIÓN SOCIALISTA GOMERA"): ("nacionalista_regionalista", None),
    ("05", "ASAMBLEAS MUNICIPALES DE FUERTEVENTURA"): ("nacionalista_regionalista", None),
    ("05", "PARTIDO NACIONALISTA CANARIO"): ("nacionalista_regionalista", None),
    ("05", "REUNIR CANARIAS SOSTENIBLE"): ("nacionalista_regionalista", None),
    ("05", "AHORA CANARIAS - PARTIDO COMUNISTA DEL PUEBLO CANARIO"): (
        "nacionalista_regionalista",
        None,
    ),
    ("05", "HABLEMOS AHORA"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("05", "AHORA TÚ"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("05", "MÁS CANARIAS"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("05", "TERCERA EDAD EN ACCIÓN"): ("otros", None),
    ("05", "AGRUPACIÓN HERREÑA INDEPENDIENTE"): ("nacionalista_regionalista", None),
    ("05", "INICIATIVA POR LA GOMERA"): ("nacionalista_regionalista", None),
    ("05", "PAÍS CON GESTORES"): (
        "otros",
        "se presenta también en Castilla-La Mancha; nombre no regional (D-030, criterio 4)",
    ),
    ("05", "ASAMBLEA HERREÑA"): ("nacionalista_regionalista", None),
    ("05", "MOVIMIENTO ALTERNATIVO ELECTORAL"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("05", "CONTIGO SOMOS DEMOCRÁCIA"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("05", "UNIÓN DEMOCRÁTICA DE CANARIAS"): ("nacionalista_regionalista", None),
    # 06 Cantabria
    ("06", "PARTIDO POPULAR DE CANTABRIA"): ("centro_derecha_estatal", None),
    ("06", "PARTIDO REGIONALISTA DE CANTABRIA"): ("nacionalista_regionalista", None),
    ("06", "PARTIDO SOCIALISTA DE CANTABRIA-PSOE"): (
        "socialdemocrata",
        "federación del PSOE en Cantabria",
    ),
    ("06", "VOX"): ("derecha_radical", None),
    ("06", "PODEMOS-IZQUIERDA UNIDA"): ("izquierda_estatal", None),
    ("06", "CIUDADANOS-PARTIDO DE LA CIUDADANIA"): ("centro_derecha_estatal", None),
    ("06", "CANTABRISTAS"): ("nacionalista_regionalista", None),
    ("06", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("06", "VERDES EQUO"): ("izquierda_estatal", None),
    ("06", "OLA CANTABRIA"): ("nacionalista_regionalista", None),
    ("06", "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"): ("otros", None),
    ("06", "CANTABRIA DISTINTA"): ("nacionalista_regionalista", None),
    # 07 Castilla y León
    ("07", "PARTIDO POPULAR (PP)"): ("centro_derecha_estatal", None),
    ("07", "PARTIDO SOCIALISTA OBRERO ESPAÑOL (PSOE)"): ("socialdemocrata", None),
    ("07", "VOX (VOX)"): ("derecha_radical", None),
    ("07", "UNIÓN DEL PUEBLO LEONÉS (UPL)"): ("nacionalista_regionalista", None),
    ("07", "IZQUIERDA UNIDA-MOVIMIENTO SUMAR-VERDES EQUO (IU-MS-VQ)"): (
        "izquierda_estatal",
        None,
    ),
    ("07", "SE ACABÓ LA FIESTA (SALF)"): ("derecha_radical", None),
    ("07", "POR ÁVILA (XÁV)"): ("nacionalista_regionalista", None),
    ("07", "PODEMOS-ALIANZA VERDE CYL 2026 (PODEMOS – AV)"): ("izquierda_estatal", None),
    ("07", "SORIA ¡YA! (SY)"): ("nacionalista_regionalista", None),
    ("07", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE (PACMA)"): ("otros", None),
    ("07", "ESCAÑOS EN BLANCO PARA DEJAR ESCAÑOS VACÍOS (ESCAÑOS EN BLANCO)"): ("otros", None),
    ("07", "CIUDADANOS-PARTIDO DE LA CIUDADANÍA (Cs)"): ("centro_derecha_estatal", None),
    ("07", "NUEVE CASTILLA Y LEÓN (NUEVECYL)"): ("nacionalista_regionalista", None),
    ("07", "VÍA BURGALESA MUNICIPALISTA (VBM)"): ("nacionalista_regionalista", None),
    ("07", "PARTIDO CASTELLANO-TIERRA COMUNERA (PCAS-TC)"): ("nacionalista_regionalista", None),
    ("07", "COALICIÓN POR EL BIERZO (C. Bierzo)"): ("nacionalista_regionalista", None),
    ("07", "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA (PCTE)"): ("otros", None),
    ("07", "VAMOS PALENCIA (VP)"): ("nacionalista_regionalista", None),
    ("07", "POR UN MUNDO MÁS JUSTO (MUNDO+JUSTO)"): ("otros", None),
    ("07", "ESPAÑA VACIADA (ESPAÑA VACIADA)"): ("nacionalista_regionalista", None),
    ("07", "AHORA DECIDE-ESPAÑA VACIADA (AD-EV)"): ("nacionalista_regionalista", None),
    ("07", "MUNICIPALISTAS-ESPAÑA VACIADA (MEV)"): ("nacionalista_regionalista", None),
    (
        "07",
        "PARTIDO NACIONALISTA DE CASTILLA Y LEÓN- UNIÓN REFORMISTA CIUDADANA (PANCAL-URCI)",
    ): ("nacionalista_regionalista", None),
    ("07", "FALANGE ESPAÑOLA DE LAS J.O.N.S. (FE de las JONS)"): ("otros", None),
    ("07", "DECIDE NUEVE CYL (DECIDE-NUEVECYL)"): ("nacionalista_regionalista", None),
    ("07", "PROYECTO ALANTRE (P. ALANTRE)"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("07", "PARTIDO REGIONALISTA DEL PAÍS LEONÉS (PREPAL)"): ("nacionalista_regionalista", None),
    ("07", "SOBERANÍA ALIMENTARIA ESPAÑOLA (SAE)"): ("otros", "nombre no regional (D-032)"),
    # 08 Castilla-La Mancha
    ("08", "PSOE"): ("socialdemocrata", None),
    ("08", "PP"): ("centro_derecha_estatal", None),
    ("08", "VOX"): ("derecha_radical", None),
    ("08", "UNIDAS PODEMOS CLM"): ("izquierda_estatal", None),
    ("08", "Cs"): ("centro_derecha_estatal", None),
    ("08", "PACMA"): ("otros", None),
    ("08", "PAIS CON GESTORES"): (
        "otros",
        "se presenta también en Canarias; nombre no regional (D-030, criterio 4)",
    ),
    ("08", "+CU-EV"): (
        "nacionalista_regionalista",
        "lista de una provincia con España Vaciada (EV); siglas no desarrolladas en el boletín",
    ),
    ("08", "ESPAÑA VACIADA"): ("nacionalista_regionalista", None),
    ("08", "PCAS-TC-RC"): ("nacionalista_regionalista", None),
    ("08", "P.C.P.E."): ("otros", None),
    ("08", "AQUÍ AHORA"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("08", "TÚ patria"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("08", "FE de las J.O.N.S."): ("otros", None),
    # 09 Cataluña
    ("09", "PARTIT DELS SOCIALISTES DE CATALUNYA (PSC-PSOE) (PSC)"): (
        "socialdemocrata",
        "federación del PSOE en Cataluña",
    ),
    ("09", "JUNTS + CARLES PUIGDEMONT PER CATALUNYA-JUNTS+ (JUNTS+)"): (
        "nacionalista_regionalista",
        None,
    ),
    ("09", "ESQUERRA REPUBLICANA DE CATALUNYA (ERC)"): ("nacionalista_regionalista", None),
    ("09", "PARTIT POPULAR / PARTIDO POPULAR (PP)"): ("centro_derecha_estatal", None),
    ("09", "VOX (VOX)"): ("derecha_radical", None),
    ("09", "COMUNS SUMAR (COMUNS SUMAR)"): ("izquierda_estatal", "marca de Sumar en Cataluña"),
    ("09", "CANDIDATURA D'UNITAT POPULAR-DEFENSEM LA TERRA (CUP-DT)"): (
        "nacionalista_regionalista",
        None,
    ),
    ("09", "ALIANÇA CATALANA (ALIANÇA.CAT)"): ("nacionalista_regionalista", None),
    ("09", "PARTIT ANIMALISTA AMB EL MEDI AMBIENT (PACMA)"): ("otros", None),
    ("09", "CIUTADANS-PARTIDO DE LA CIUDADANÍA (Cs)"): ("centro_derecha_estatal", None),
    ("09", "ALHORA (ALHORA)"): ("nacionalista_regionalista", None),
    ("09", "FRENTE OBRERO (FO)"): ("otros", None),
    ("09", "PARTIT COMUNISTA DELS TREBALLADORS DE CATALUNYA (PCTC)"): (
        "otros",
        "marca territorial del PCTE",
    ),
    ("09", "RECORTES CERO (RECORTES CERO)"): ("otros", None),
    ("09", "PER UN MÓN MES JUST (PUM+J)"): ("otros", "Por un Mundo más Justo, en catalán"),
    ("09", "IZQUIERDA POR ESPAÑA (IZQP-UNIDOS-DEf)"): ("otros", "nombre no regional (D-032)"),
    ("09", "FRONT NACIONAL DE CATALUNYA (F.N.C.)"): ("nacionalista_regionalista", None),
    ("09", "CONVERGENTS (CNV)"): ("nacionalista_regionalista", None),
    # 10 Comunitat Valenciana
    ("10", "Partido Popular (PP)"): ("centro_derecha_estatal", None),
    ("10", "Partido Socialista Obrero Español (PSOE)"): ("socialdemocrata", None),
    ("10", "Compromís: Més-Iniciativa-Verdsequo (COMPROMÍS)"): (
        "nacionalista_regionalista",
        "coalición encabezada por Més-Compromís",
    ),
    ("10", "Vox (VOX)"): ("derecha_radical", None),
    ("10", "Unides Podem-Esquerra Unida (UP-EUPV)"): ("izquierda_estatal", None),
    ("10", "Ciudadanos-Partido de la Ciudadanía (Cs)"): ("centro_derecha_estatal", None),
    ("10", "Partido Animalista con el Medio Ambiente (PACMA)"): ("otros", None),
    ("10", "Los Verdes-Ecopacifistas (CENTRO MODERADO)"): (
        "otros",
        "nombre no regional (D-032); identificación no segura: las siglas no casan con el nombre",
    ),
    ("10", "Esquerra Republicana del País Valencià (ERPV)"): ("nacionalista_regionalista", None),
    ("10", "Coalició Units (UNITS)"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("10", "Partido Comunista de los Pueblos de España (PCPE)"): ("otros", None),
    ("10", "Recortes Cero (RECORTES CERO)"): ("otros", None),
    ("10", "Decidix (DECIDIX)"): ("nacionalista_regionalista", None),
    ("10", "Escaños en Blanco para Dejar Escaños Vacíos (ESCAÑOS EN BLANCO)"): ("otros", None),
    ("10", "República Valenciana / Partit Valencianiste Europeu (RVPVE)"): (
        "nacionalista_regionalista",
        None,
    ),
    ("10", "Alianza por el Comercio y la Vivienda (ALIANZA C V)"): (
        "otros",
        "nombre no regional (D-032); identificación no segura",
    ),
    ("10", "Por un Mundo Más Justo (PUM+J)"): ("otros", None),
    ("10", "Centrats en la Nostra Terra (CENTRATS)"): ("nacionalista_regionalista", None),
    ("10", "Partido Alicantino Regionalista - Esperanza Ciudadana (PAR-Es.C.)"): (
        "nacionalista_regionalista",
        None,
    ),
    # 11 Extremadura
    ("11", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("11", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("11", "VOX"): ("derecha_radical", None),
    ("11", "UNIDAS POR EXTREMADURA PODEMOS IZQUIERDA UNIDA ALIANZA VERDE"): (
        "izquierda_estatal",
        None,
    ),
    ("11", "JUNTOS POR EXTREMADURA-LEVANTA EXTREMADURA"): ("nacionalista_regionalista", None),
    ("11", "NUEVO EXTREMEÑISMO-ADELANTE EXTREMADURA"): ("nacionalista_regionalista", None),
    ("11", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("11", "EXTREMADURA UNIDA"): ("nacionalista_regionalista", None),
    ("11", "CIUDADANOS-PARTIDO DE LA CIUDADANÍA"): ("centro_derecha_estatal", None),
    ("11", "UNA EXTREMADURA DIGNA-SOBERANÍA Y TRABAJO"): ("nacionalista_regionalista", None),
    ("11", "POR UN MUNDO MÁS JUSTO"): ("otros", None),
    # 12 Galicia
    ("12", "PARTIDO POPULAR (PP)"): ("centro_derecha_estatal", None),
    ("12", "BLOQUE NACIONALISTA GALEGO (BNG)"): ("nacionalista_regionalista", None),
    ("12", "PARTIDO DOS SOCIALISTAS DE GALICIA-PSOE (PSdeG-PSOE)"): (
        "socialdemocrata",
        "federación del PSOE en Galicia",
    ),
    ("12", "VOX (VOX)"): ("derecha_radical", None),
    ("12", "SUMAR GALICIA (SUMAR GALICIA)"): ("izquierda_estatal", "marca de Sumar en Galicia"),
    ("12", "DEMOCRACIA OURENSANA (DO)"): ("nacionalista_regionalista", None),
    ("12", "PARTIDO ANIMALISTA CONTRA O MALTRATO ANIMAL (PACMA)"): ("otros", None),
    ("12", "PODEMOS GALICIA (Podemos-Alianza Verde)"): ("izquierda_estatal", None),
    ("12", "ESCANOS EN BRANCO (ESCAÑOS EN BLANCO)"): ("otros", None),
    ("12", "ESPAZO COMÚN GALEGUISTA (ECG)"): ("nacionalista_regionalista", None),
    ("12", "POR UN MUNDO MÁIS XUSTO (PUM+J)"): ("otros", None),
    # 13 Comunidad de Madrid
    ("13", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("13", "MÁS MADRID-VERDES EQUO"): ("izquierda_estatal", "marca de Más País en Madrid"),
    ("13", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("13", "VOX"): ("derecha_radical", None),
    ("13", "PODEMOS-IZQUIERDA UNIDA-ALIANZA VERDE"): ("izquierda_estatal", None),
    ("13", "CIUDADANOS-PARTIDO DE LA CIUDADANÍA"): ("centro_derecha_estatal", None),
    ("13", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("13", "POR UN MUNDO MÁS JUSTO"): ("otros", None),
    ("13", "PARTIDO FEMINISTA DE ESPAÑA"): ("otros", None),
    ("13", "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"): ("otros", None),
    ("13", "FALANGE ESPAÑOLA DE LAS J.O.N.S."): ("otros", None),
    ("13", "UNIÓN POR LEGANÉS"): ("nacionalista_regionalista", None),
    ("13", "PARTIDO HUMANISTA"): ("otros", None),
    # 14 Región de Murcia
    ("14", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("14", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("14", "VOX"): ("derecha_radical", None),
    ("14", "PODEMOS-IZQUIERDA UNIDA VERDES-ALIANZA VERDE"): ("izquierda_estatal", None),
    ("14", "MC REGIONAL"): ("nacionalista_regionalista", None),
    ("14", "CIUDADANOS-PARTIDO DE LA CIUDADANIA"): ("centro_derecha_estatal", None),
    ("14", "MAS REGION-VERDES EQUO"): (
        "izquierda_estatal",
        "marca de Más País en la Región de Murcia",
    ),
    ("14", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("14", "POR MI REGIÓN"): ("nacionalista_regionalista", None),
    ("14", "TERCERA EDAD EN ACCIÓN"): ("otros", None),
    ("14", "MURCIA LIBRE"): ("nacionalista_regionalista", None),
    ("14", "VALORES"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("14", "PARTIDO COMUNISTA DE LOS PUEBLOS DE ESPAÑA"): ("otros", None),
    ("14", "FALANGE ESPAÑOLA DE LAS J.O.N.S."): ("otros", None),
    ("14", "PARTIDO CANTONAL DE CARTAGENA"): ("nacionalista_regionalista", None),
    # 15 Comunidad Foral de Navarra
    ("15", "UNION DEL PUEBLO NAVARRO"): ("nacionalista_regionalista", None),
    ("15", "PARTIDO SOCIALISTA DE NAVARRA-PSOE"): (
        "socialdemocrata",
        "federación del PSOE en Navarra",
    ),
    ("15", "EUSKAL HERRIA BILDU"): ("nacionalista_regionalista", None),
    ("15", "GEROA BAI"): ("nacionalista_regionalista", None),
    ("15", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("15", "PODEMOS + IZQUIERDA UNIDA + BATZARRE + ALIANZA VERDE + BERDEAK EQUO"): (
        "izquierda_estatal",
        "Contigo-Zurekin: coalición de Podemos, IU y otros",
    ),
    ("15", "VOX"): ("derecha_radical", None),
    ("15", "POR UN MUNDO MÁS JUSTO/BIDEZKO MUNDURANTZ"): ("otros", None),
    ("15", "CIUDADANOS"): ("centro_derecha_estatal", None),
    ("15", "EGUZKILORE"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    ("15", "VOLUNTAD FORAL"): ("nacionalista_regionalista", None),
    # 16 País Vasco
    ("16", "Euzko Alderdi Jeltzalea-Partido Nacionalista Vasco (EAJ-PNV)"): (
        "nacionalista_regionalista",
        None,
    ),
    ("16", "Euskal Herria Bildu (EH Bildu)"): ("nacionalista_regionalista", None),
    ("16", "Partido Socialista de Euskadi-Euskadiko Ezkerra (PSOE)"): (
        "socialdemocrata",
        "federación del PSOE en el País Vasco",
    ),
    ("16", "Partido Popular (PP)"): ("centro_derecha_estatal", None),
    ("16", "Sumar"): ("izquierda_estatal", None),
    ("16", "Partido Popular"): (
        "centro_derecha_estatal",
        "mismo partido que «Partido Popular (PP)»; el boletín lo imprime sin siglas en una "
        "circunscripción",
    ),
    ("16", "Elkarrekin Podemos-Alianza Verde"): ("izquierda_estatal", None),
    ("16", "Vox (VOX)"): ("derecha_radical", None),
    ("16", "Partido Animalista Con el Medio Ambiente"): ("otros", None),
    ("16", "Escaños en Blanco para Dejar Escaños Vacíos-Aulki Zuriak Eserlekuak Hutsik Uzteko"): (
        "otros",
        None,
    ),
    ("16", "Por un Mundo Más Justo-Bidezko Mundurantz"): ("otros", None),
    ("16", "IZAN"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    (
        "16",
        "Partido Comunista de los Trabajadores de Euskadi/Euskadiko Langileen Alderdi Komunista",
    ): ("otros", "marca territorial del PCTE"),
    ("16", "Partido Humanista"): ("otros", None),
    ("16", "Ongi Etorri (OE)"): (
        "nacionalista_regionalista",
        "nombre no identificado con certeza; clasificado por su ámbito (D-030, criterio 3)",
    ),
    # 17 La Rioja
    ("17", "PARTIDO POPULAR"): ("centro_derecha_estatal", None),
    ("17", "PARTIDO SOCIALISTA OBRERO ESPAÑOL"): ("socialdemocrata", None),
    ("17", "VOX"): ("derecha_radical", None),
    ("17", "PODEMOS-IZQUIERDA UNIDA"): ("izquierda_estatal", None),
    ("17", "PARTIDO RIOJANO+ESPAÑA VACIADA"): ("nacionalista_regionalista", None),
    ("17", "POR LA RIOJA"): ("nacionalista_regionalista", None),
    ("17", "CIUDADANOS-PARTIDO DE LA CIUDADANÍA"): ("centro_derecha_estatal", None),
    ("17", "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE"): ("otros", None),
    ("17", "VINEA La Rioja"): ("nacionalista_regionalista", None),
    ("17", "ESCAÑOS EN BLANCO PARA DEJAR ESCAÑOS VACÍOS"): ("otros", None),
    # 18 Ceuta
    ("18", "PARTIDO POPULAR (PP)"): ("centro_derecha_estatal", None),
    ("18", "PARTIDO SOCIALISTA OBRERO ESPAÑOL (PSOE)"): ("socialdemocrata", None),
    ("18", "VOX (VOX)"): ("derecha_radical", None),
    ("18", "MOVIMIENTO POR LA DIGNIDAD Y LA CIUDADANÍA DE CEUTA (MDYC)"): (
        "nacionalista_regionalista",
        None,
    ),
    ("18", "CEUTA YA! (CEUTA YA!)"): ("nacionalista_regionalista", None),
    ("18", "CIUDADANOS-PARTIDO DE LA CIUDADANÍA (CS)"): ("centro_derecha_estatal", None),
    ("18", "PODEMOS (PODEMOS)"): ("izquierda_estatal", None),
    ("18", "LIBRES (LB)"): ("otros", "mismo partido que «Libres» en las generales de 2023"),
    # 19 Melilla
    ("19", "PARTIDO POPULAR (PP)"): ("centro_derecha_estatal", None),
    ("19", "COALICION POR MELILLA (CPM)"): ("nacionalista_regionalista", None),
    ("19", "PARTIDO SOCIALISTA OBRERO ESPAÑOL (PSOE)"): ("socialdemocrata", None),
    ("19", "VOX (VOX)"): ("derecha_radical", None),
    ("19", "SOMOS MELILLA (SML)"): ("nacionalista_regionalista", None),
    ("19", "PODEMOS (PODEMOS)"): ("izquierda_estatal", None),
    ("19", "ADELANTE MELILLA (ADEME)"): ("nacionalista_regionalista", None),
    ("19", "CREANDO MELILLA (CREAME)"): ("nacionalista_regionalista", None),
}


if __name__ == "__main__":
    from collections import Counter

    import polars as pl

    FAMILIAS = {
        "izquierda_estatal",
        "socialdemocrata",
        "centro_derecha_estatal",
        "derecha_radical",
        "nacionalista_regionalista",
        "otros",
    }
    votos = pl.read_parquet("data/interim/elecciones_autonomicas_votos.parquet")
    pares = set(votos.select("ccaa", "candidatura").unique().iter_rows())
    sobran = set(FAMILIAS_AUTONOMICAS) - pares
    faltan = pares - set(FAMILIAS_AUTONOMICAS)
    assert not sobran, f"claves que no están en los datos: {sorted(sobran)}"
    assert not faltan, f"candidaturas sin familia: {sorted(faltan)}"
    malas = {v[0] for v in FAMILIAS_AUTONOMICAS.values()} - FAMILIAS
    assert not malas, f"familias desconocidas: {malas}"
    print(f"{len(FAMILIAS_AUTONOMICAS)} candidaturas clasificadas")
    for familia, n in Counter(v[0] for v in FAMILIAS_AUTONOMICAS.values()).most_common():
        print(f"  {familia}: {n}")
