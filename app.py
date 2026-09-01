import streamlit.components.v1 as components
import streamlit as st
import os
import random
import time

# 1. EL DICCIONARIO (Dentro de app.py para que lo reconozca)
diccionario_paises = {
    'ad': 'Andorra', 'ae': 'Emiratos Árabes Unidos', 'af': 'Afganistán', 'ag': 'Antigua y Barbuda',
    'ai': 'Anguila', 'al': 'Albania', 'am': 'Armenia', 'ao': 'Angola', 'aq': 'Antártida',
    'ar': 'Argentina', 'as': 'Samoa Americana', 'at': 'Austria', 'au': 'Australia',
    'aw': 'Aruba', 'ax': 'Islas Åland', 'az': 'Azerbaiyán', 'ba': 'Bosnia y Herzegovina',
    'bb': 'Barbados', 'bd': 'Bangladés', 'be': 'Bélgica', 'bf': 'Burkina Faso',
    'bg': 'Bulgaria', 'bh': 'Baréin', 'bi': 'Burundi', 'bj': 'Benín', 'bl': 'San Bartolomé',
    'bm': 'Bermudas', 'bn': 'Brunéi', 'bo': 'Bolivia', 'bq': 'Caribe Neerlandés',
    'br': 'Brasil', 'bs': 'Bahamas', 'bt': 'Bután', 'bv': 'Isla Bouvet', 'bw': 'Botsuana',
    'by': 'Bielorrusia', 'bz': 'Belice', 'ca': 'Canadá', 'cc': 'Islas Cocos',
    'cd': 'Congo (RDC)', 'cf': 'República Centroafricana', 'cg': 'República del Congo',
    'ch': 'Suiza', 'ci': 'Costa de Marfil', 'ck': 'Islas Cook', 'cl': 'Chile',
    'cm': 'Camerún', 'cn': 'China', 'co': 'Colombia', 'cr': 'Costa Rica', 'cu': 'Cuba',
    'cv': 'Cabo Verde', 'cw': 'Curazao', 'cx': 'Isla de Navidad', 'cy': 'Chipre',
    'cz': 'República Checa', 'de': 'Alemania', 'dj': 'Yibuti', 'dk': 'Dinamarca',
    'dm': 'Dominica', 'do': 'República Dominicana', 'dz': 'Argelia', 'ec': 'Ecuador',
    'ee': 'Estonia', 'eg': 'Egipto', 'eh': 'Sahara Occidental', 'er': 'Eritrea',
    'es': 'España', 'et': 'Etiopía', 'fi': 'Finlandia', 'fj': 'Fiyi', 'fk': 'Islas Malvinas',
    'fm': 'Micronesia', 'fo': 'Islas Feroe', 'fr': 'Francia', 'ga': 'Gabón',
    'gb': 'Reino Unido', 'gb-eng': 'Inglaterra', 'gb-nir': 'Irlanda del Norte',
    'gb-sct': 'Escocia', 'gb-wls': 'Gales', 'gd': 'Granada', 'ge': 'Georgia',
    'gf': 'Guayana Francesa', 'gg': 'Guernsey', 'gh': 'Ghana', 'gi': 'Gibraltar',
    'gl': 'Groenlandia', 'gm': 'Gambia', 'gn': 'Guinea', 'gp': 'Guadalupe',
    'gq': 'Guinea Ecuatorial', 'gr': 'Grecia', 'gs': 'Georgias del Sur', 'gt': 'Guatemala',
    'gu': 'Guam', 'gw': 'Guinea-Bisáu', 'gy': 'Guyana', 'hk': 'Hong Kong',
    'hm': 'Islas Heard y McDonald', 'hn': 'Honduras', 'hr': 'Croacia', 'ht': 'Haití',
    'hu': 'Hungría', 'id': 'Indonesia', 'ie': 'Irlanda', 'il': 'Israel', 'im': 'Isla de Man',
    'in': 'India', 'io': 'Territorio Británico del Océano Índico', 'iq': 'Irak',
    'ir': 'Irán', 'is': 'Islandia', 'it': 'Italia', 'je': 'Jersey', 'jm': 'Jamaica',
    'jo': 'Jordania', 'jp': 'Japón', 'ke': 'Kenia', 'kg': 'Kirguistán', 'kh': 'Camboya',
    'ki': 'Kiribati', 'km': 'Comoras', 'kn': 'San Cristóbal y Nieves', 'kp': 'Corea del Norte',
    'kr': 'Corea del Sur', 'kw': 'Kuwait', 'ky': 'Islas Caimán', 'kz': 'Kazajistán',
    'la': 'Laos', 'lb': 'Líbano', 'lc': 'Santa Lucía', 'li': 'Liechtenstein',
    'lk': 'Sri Lanka', 'lr': 'Liberia', 'ls': 'Lesoto', 'lt': 'Lituania',
    'lu': 'Luxemburgo', 'lv': 'Letonia', 'ly': 'Libia', 'ma': 'Marruecos',
    'mc': 'Mónaco', 'md': 'Moldavia', 'me': 'Montenegro', 'mf': 'San Martín',
    'mg': 'Madagascar', 'mh': 'Islas Marshall', 'mk': 'Macedonia del Norte',
    'ml': 'Malí', 'mm': 'Birmania', 'mn': 'Mongolia', 'mo': 'Macao',
    'mp': 'Islas Marianas del Norte', 'mq': 'Martinica', 'mr': 'Mauritania',
    'ms': 'Montserrat', 'mt': 'Malta', 'mu': 'Mauricio', 'mv': 'Maldivas',
    'mw': 'Malaui', 'mx': 'México', 'my': 'Malasia', 'mz': 'Mozambique',
    'na': 'Namibia', 'nc': 'Nueva Caledonia', 'ne': 'Níger', 'nf': 'Isla Norfolk',
    'ng': 'Nigeria', 'ni': 'Nicaragua', 'nl': 'Países Bajos', 'no': 'Noruega',
    'np': 'Nepal', 'nr': 'Nauru', 'nu': 'Niue', 'nz': 'Nueva Zelanda', 'om': 'Omán',
    'pa': 'Panamá', 'pe': 'Perú', 'pf': 'Polinesia Francesa', 'pg': 'Papúa Nueva Guinea',
    'ph': 'Filipinas', 'pk': 'Pakistán', 'pl': 'Polonia', 'pm': 'San Pedro y Miquelón',
    'pn': 'Islas Pitcairn', 'pr': 'Puerto Rico', 'ps': 'Palestina', 'pt': 'Portugal',
    'pw': 'Palaos', 'py': 'Paraguay', 'qa': 'Catar', 're': 'Reunión', 'ro': 'Rumania',
    'rs': 'Serbia', 'ru': 'Rusia', 'rw': 'Ruanda', 'sa': 'Arabia Saudita',
    'sb': 'Islas Salomón', 'sc': 'Seychelles', 'sd': 'Sudán', 'se': 'Suecia',
    'sg': 'Singapur', 'sh': 'Santa Elena', 'si': 'Eslovenia', 'sj': 'Svalbard',
    'sk': 'Eslovaquia', 'sl': 'Sierra Leona', 'sm': 'San Marino', 'sn': 'Senegal',
    'so': 'Somalia', 'sr': 'Surinam', 'ss': 'Sudán del Sur', 'st': 'Santo Tomé y Príncipe',
    'sv': 'El Salvador', 'sx': 'Sint Maarten', 'sy': 'Siria', 'sz': 'Esuatini',
    'tc': 'Islas Turcas y Caicos', 'td': 'Chad', 'tf': 'Tierras Australes Francesas',
    'tg': 'Togo', 'th': 'Tailandia', 'tj': 'Tayikistán', 'tk': 'Tokelau',
    'tl': 'Timor Oriental', 'tm': 'Turkmenistán', 'tn': 'Túnez', 'to': 'Tonga',
    'tr': 'Turquía', 'tt': 'Trinidad y Tobago', 'tv': 'Tuvalu', 'tw': 'Taiwán',
    'tz': 'Tanzania', 'ua': 'Ucrania', 'ug': 'Uganda', 'um': 'Islas Menores de EE. UU.',
    'us': 'Estados Unidos', 'uy': 'Uruguay', 'uz': 'Uzbekistán', 'va': 'Ciudad del Vaticano',
    'vc': 'San Vicente y las Granadinas', 've': 'Venezuela', 'vg': 'Islas Vírgenes Británicas',
    'vi': 'Islas Vírgenes de EE. UU.', 'vn': 'Vietnam', 'vu': 'Vanuatu',
    'wf': 'Wallis y Futuna', 'ws': 'Samoa', 'xk': 'Kosovo', 'ye': 'Yemen',
    'yt': 'Mayotte', 'za': 'Sudáfrica', 'zm': 'Zambia', 'zw': 'Zimbabue'
}

# 2. LÓGICA DE CARGA INTEGRADA
def cargar_datos_juego(ruta="flags/country-flags-main/png250px"):
    lista_banderas = []
    if os.path.exists(ruta):
        for archivo in os.listdir(ruta):
            if archivo.endswith(".svg"):
                codigo = archivo.replace(".svg", "").lower()
                # Buscamos en el diccionario, si no está, usamos el nombre del archivo
                nombre_pais = diccionario_paises.get(codigo, codigo.title())

                lista_banderas.append({
                    "pais": nombre_pais,
                    "ruta": os.path.join(ruta, archivo)
                })
    return lista_banderas

def generar_opciones(pais_correcto, lista_completa):
    nombres_todos = [b["pais"] for b in lista_completa]
    otras_opciones = [n for n in nombres_todos if n != pais_correcto]
    falsas = random.sample(otras_opciones, min(3, len(otras_opciones)))
    opciones = falsas + [pais_correcto]
    random.shuffle(opciones)
    return opciones

def decir_nombre_pais(nombre):
    # Este pequeño código en JavaScript hace que el navegador hable
    codigo_js = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{nombre}');
        msg.lang = 'es-ES';  // Configuramos voz en español
        msg.rate = 0.9;      // Un poquito más lento para que la niña lo entienda bien
        window.speechSynthesis.speak(msg);
        </script>
    """
    # Lo insertamos de forma invisible en la app
    components.html(codigo_js, height=0)


# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Juego de Banderas", page_icon="🌍", layout="centered")

# --- DISEÑO ALEGRE PARA NIÑOS ---
st.markdown("""
    <style>
    /* 1. Fondo con degradado de colores alegres */
    .stApp {
        background: linear-gradient(135deg, #fceabb 0%, #f8b500 50%, #fceabb 100%);
        background-attachment: fixed;
    }

    /* 2. Estilo para el contenedor principal (donde está la bandera) */
    .stMainBlockContainer {
        background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semi-transparente */
        border-radius: 30px;
        padding: 40px !important;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    /* 3. Título con sombra y color divertido */
    h1 {
        color: #FF4B4B !important;
        text-shadow: 2px 2px #ffcc00;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    /* 4. Botones más coloridos */
    .stButton>button {
        background-color: #ffffff;
        color: #333;
        font-weight: bold;
        border: 3px solid #ff4b4b;
        transition: 0.3s transform ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.05); /* El botón se agranda un poquito al tocarlo */
        background-color: #ff4b4b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAR ESTADO ---
# --- LISTA DE PAÍSES FÁCILES (Asegúrate de que el nombre coincida con tu diccionario) ---
PAISES_FACILES = ["España", "México", "Argentina", "Colombia", "Chile", "Perú", "Estados Unidos", "Francia", "Italia", "Japón","Brasil","Corea del Sur","China"]

if 'lista_juego' not in st.session_state:
    datos_completos = cargar_datos_juego()
    
    # 1. Separamos las banderas en dos grupos
    faciles = [b for b in datos_completos if b["pais"] in PAISES_FACILES]
    dificiles = [b for b in datos_completos if b["pais"] not in PAISES_FACILES]
    
    # 2. Mezclamos ambos grupos por separado
    random.shuffle(faciles)
    random.shuffle(dificiles)
    
    # 3. Juntamos: Primero las fáciles, luego 10 difíciles al azar
    # Así el juego siempre empieza con caras conocidas
    st.session_state.lista_juego = faciles[:5] + dificiles[:3]
    
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.respuesta_correcta_dada = False

# --- INTERFAZ ---
st.markdown('<p class="big-title">🌍 ¡Adivina el País! 🌈</p>', unsafe_allow_html=True)
st.markdown(f'<p class="score-text">Estrellas: {"⭐" * st.session_state.puntos}</p>', unsafe_allow_html=True)

if st.session_state.indice < len(st.session_state.lista_juego):
    actual = st.session_state.lista_juego[st.session_state.indice]

    st.image(actual["ruta"], use_container_width=True)
    st.write(f"<h3 style='text-align: center;'>¿Qué bandera es?</h3>", unsafe_allow_html=True)

    # Generamos opciones para la bandera actual
    if 'opciones_actuales' not in st.session_state or st.session_state.opciones_actuales_indice != st.session_state.indice:
        st.session_state.opciones_actuales = generar_opciones(actual["pais"], st.session_state.lista_juego)
        st.session_state.opciones_actuales_indice = st.session_state.indice

    # Mostrar botones
# --- MOSTRAR BOTONES ---
    if not st.session_state.respuesta_correcta_dada:
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.opciones_actuales):
            with cols[i % 2]:
                if st.button(opcion, key=f"btn_{i}", use_container_width=True):
                    if opcion == actual["pais"]:
                        st.session_state.puntos += 1
                        st.session_state.respuesta_correcta_dada = True
                        st.balloons()
                        st.rerun() # Esto refresca para ir al bloque "else"
                    else:
                        st.error("¡Casi! Intenta otra vez 💪")
    else:
        # --- ESTE ES EL BLOQUE DE ÉXITO ---
        st.success(f"¡Sí! Es {actual['pais']} 🎉")
        
        # 📢 ¡NUEVO! El juego dice el nombre del país
        decir_nombre_pais(actual["pais"])
        
        if st.button("¡Siguiente Bandera! ➡️", use_container_width=True):
            st.session_state.indice += 1
            st.session_state.respuesta_correcta_dada = False
            # Limpiamos las opciones para que se generen nuevas en la siguiente
            st.session_state.opciones_actuales = None 
            st.rerun()

else:
    # 1. LANZAMOS TODA LA ARTILLERÍA VISUAL
    st.balloons()
    st.snow()
    
    # 2. MENSAJE GIGANTE Y COLORIDO
    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 100px;'>🏆</p>
            <h1 style='font-size: 80px; color: #FFD700; text-shadow: 3px 3px #FF4B4B;'>
                ¡FELICIDADES MARÍA!
            </h1>
            <h2 style='font-size: 50px; color: #FF69B4;'>
                ¡LO HAS LOGRADO! 🎉
            </h2>
        </div>
    """, unsafe_allow_html=True)

    # 3. EL JUEGO LE HABLA POR ÚLTIMA VEZ
    # Usamos la función de voz que ya creamos antes
    decir_nombre_pais("¡Felicidades, campeona!")

    # 4. BOTÓN DE REINICIAR GIGANTE
    st.write("---")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("✨ ¡JUGAR OTRA VEZ! ✨", use_container_width=True):
            st.session_state.clear()
            st.rerun()
