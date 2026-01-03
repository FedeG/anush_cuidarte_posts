# ruff: noqa
# fmt: off
"""
Constants - Configuración centralizada del proyecto
"""

# Configuración de Instagram
INSTAGRAM_USERNAME = "anush.cuidarte"
LOGIN_USERNAME = "anush.cuidarte"
LOGIN_PASSWORD = "XXXXXXXXXXX"

# Rutas de archivos
RECIPES_FILE = "src/data/recipes.json"
IMAGES_DIR = "public/images"

# ruff: noqa
# fmt: off

# Tags que son ruido, métricas sociales o demasiado genéricos para salud
TAGS_TO_SKIP = [
    "anushcuidarte", "laenfermerapueri", "laenfermerapueriresponde", "laenfermerpueri",
    "anush", "lauritapuericultora", "sobremi", "lifestyle", "nursestyle",
    "amor", "love", "agradecer", "solidaridad", "frases", "poesia", "humor", "comedia",
    "unallama", "sorteo", "sorteoargentina", "sorteolactancia", "5k", "reels",
    "reelsdematernidad", "ideas", "ideasderegalos", "regalos", "datazo", "pingpong",
    "karolg", "mañanaserabonito", "2022", "2023", "2025", "rewind", "verano", "invierno",
    "calor", "playa", "mar", "travel", "navidad", "christmas", "añonuevo", "diadelamadre",
    "diadelpadre", "valentineday", "diadelamor", "buenosaires", "argentina", "jujuy",
    "bahiablanca", "caballito", "1", "2", "3", "4", "5", "6", "7", "26", "19demayo",
    "ohwear", "pausa", "elaternauta", "memoriaverdadyjusticia", "masmujeresmasdemocracia"
]

# Diccionario de estandarización para Salud y Puericultura
TAG_SYNONYMS = {
    "lactancia": [
        "lactanciamaterna", "lactanciahumana", "lactanciareal", "lactanciainformada",
        "lactanciamaternaexclusiva", "lactanciaexclusiva", "lactanciarespetuosa", 
        "lactanciarespetada", "lactanciamitos", "lactanciaconevidencia", "apoyoalalactancia",
        "lactanciarespeto", "lactanciafeliz", "lactanciaconamor", "lactanciaenpeligro",
        "lactanciadiferida", "lactanciamixta", "lactanciaprenatal", "lactancianatural",
        "lactanciaprolongada", "lactanciainniñosmayores", "lactanciaconrespeto",
        "lactanciasreales", "consultapuericultura", "consultoríaenlactancia", "darlateta"
    ],
    "puericultura": [
        "puericultora", "puericulturaprofesional", "puericulturaconevidencia", 
        "puericulture", "pueri", "puericulturaconhumor"
    ],
    "enfermeria": [
        "enfermería", "nurse", "enfermerapueri", "diadelaenfermeria", 
        "diainternacionaldelaenfermeria", "enfermeriacomunica", "enfermeríacomunica",
        "dataenfermera", "sanitarios", "care", "healthcare", "medicine"
    ],
    "vacunacion": [
        "vacunas", "vacunación", "vacunacionrespetuosa", "vacunaciónrespetuosa",
        "inmunización", "inmunizacion", "vacunaciónconamor", "vacunassinmiedo",
        "campañadevacunacion", "calendariodevacion", "vᴀᴄᴜɴᴀcᴏᴠɪᴅ19", "vaccine",
        "vaccineday", "vᴀᴄᴜɴᴀanticᴏᴠɪᴅ19", "astrazeneca", "sinopharm", "sputnikv",
        "bexsero", "bcg", "vacunate", "vacunafiebreamarilla", "vacunacionembarazo"
    ],
    "recien nacido": [
        "bebe", "bebes", "bebés", "reciennacido", "reciennacidos", "nacimiento",
        "cuidadosdelreciennacido", "controlreciennacido", "cadabebéesúnico",
        "llegadadelbebe", "mamásybebés", "reciénnacido"
    ],
    "embarazo": [
        "maternidad", "maternidadreal", "maternidadconsciente", "mapaternidad", 
        "embarazada", "diadelaembarazada", "preparandolalactancia", "tallerprenatal",
        "cambiosenelembarazo", "cuerpogestante", "educaciónperinatal", "bebeencamino",
        "preparativos", "síndromedelnido", "tercertrimestre", "2dotrimestre", "puerperio"
    ],
    "alimentacion complementaria": [
        "blw", "bliss", "alimentacionreal", "alimentaciónreal", "alimentacioncomplementaria",
        "alimentacioncomolementaria", "alimentacion", "alimentación", "tallerac", 
        "señalesdehambre", "alimentacióndelbebé", "papillas", "hierroenbebes", 
        "alimentacaosaudavel", "alimentacionsaludable", "comidareal"
    ],
    "primeros auxilios": [
        "urgencias", "urgencia", "emergencia", "emergency", "sos", "primerosauxilios",
        "accidentes", "accidente", "incidentes", "quemaduras", "botiquin", 
        "botiquindeprimerosauxilios", "triage", "seguridadvial"
    ],
    "lesiones": [
        "grietas", "mastitis", "grietasenelpezón", "grietasypezón", "heridasenlactancia",
        "lesionesdelpezón", "masterclassgrietas", "cuidadodelpecho", "pezoneras", "pezonera"
    ],
    "extraccion_leche": [
        "bancodeleche", "bancosdeleche", "lechehumana", "lechedemadre", "lechematerna",
        "donacióndelechehumana", "donaciondeleche", "extraccióndeleche", "conservacióndeleche",
        "sacaleches", "breastpump", "extraccionmanual", "bajadadeleche"
    ],
    "pediatria": [
        "pediatría", "saludinfantil", "controlespediatricos", "niñosano", "niños",
        "infancia", "infancias", "niñes", "niño", "percentil"
    ],
    "patologias_respiratorias": [
        "asma", "broncoespasmo", "bronquiolitis", "bronquitis", "bronquite", 
        "catarro", "mocos", "resfriado", "aerocamara", "inhalador", "vsr"
    ],
    "crianza": [
        "crianzarespetuosa", "crianzaconamor", "cuidadorespetuoso", "apego",
        "tribu", "tribuvirtual", "tribudeamigas", "exterogestacion", "porteoergonomico",
        "crianzaenbrazos", "deschupete", "pacifier", "chupete"
    ],
    "heridas": [
        "herida", "heridas", "cuidadodeheridas", "curaavanzada", "heridologíaperinatal",
        "heridadecesárea", "cicatrizaciónsaludable", "expertaenheridas", "curación", 
        "curahumeda", "botiquindeheridas"
    ]
}

EASY_TAG = "facil"

# Marcadores de fin de sección al parsear ingredientes
SECTION_END_MARKERS = ["👣", "🔪", "👨‍🍳", "📝", "🍽️", "⏰", "💡", "pasos", "Pasos"]

# Post pineados
PINNED_MEDIAIDS = []
