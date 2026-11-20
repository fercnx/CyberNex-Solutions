# -*- coding: utf-8 -*-
"""Contenido del sitio CYBERNEX 11.0 (única fuente de verdad).

Reglas del proyecto:
- Solo se publica lo que existe en el material original o es contenido editorial propio.
- No se inventan clientes, cifras, certificaciones, tarifas ni datos de contacto.
- Textos de misión, visión, valores, reglas y principios: tomados tal cual de la presentación.
"""

LEMA = "Tu información, nuestra prioridad"
FRASE = "Protegemos tu mundo digital."
CONCEPTO = "Tecnología que conecta. Seguridad que empodera."

# --------------------------------------------------------------------------------------
# Divisiones del ecosistema
# --------------------------------------------------------------------------------------
DIVISIONS = [
    dict(
        id="development", name="NEX Development", short="Development", icon="code", cls="d-dev",
        acc="#5b9bff", rgb="91,155,255", status="Línea de trabajo", kind="linea",
        lead="Desarrollo tecnológico para personas y organizaciones.",
        summary="Páginas web, sistemas administrativos, aplicaciones y diseño de interfaces.",
        items=[
            "Desarrollo de páginas web",
            "Sistemas administrativos",
            "Aplicaciones y software",
            "Diseño UI/UX",
            "Mantenimiento y optimización",
        ],
        note="Todavía no hay proyectos de desarrollo publicados. El portafolio está preparado para incorporarlos cuando existan.",
        links=[("Ver soluciones de NEX Development", "soluciones.html#division=development"),
               ("Ver el portafolio", "proyectos.html")],
        big=True,
    ),
    dict(
        id="security", name="NEX Security", short="Security", icon="shield", cls="d-sec",
        acc="#72e6ff", rgb="114,230,255", status="Herramientas disponibles", kind="disponible",
        lead="Seguridad informática, prevención y educación digital.",
        summary="Protección de información, evaluación de riesgos y buenas prácticas, con herramientas educativas que ya funcionan.",
        items=[
            "Protección de información",
            "Evaluación de riesgos",
            "Prevención de vulnerabilidades",
            "Asesoría en ciberseguridad",
            "Educación y buenas prácticas digitales",
            "Análisis de seguridad únicamente con autorización",
        ],
        note="Las herramientas educativas de NEX Security funcionan en tu navegador, sin enviar datos. Toda evaluación de seguridad se realiza únicamente con autorización expresa y alcance acordado.",
        links=[("Abrir NEX Security", "security.html"),
               ("Ver soluciones de NEX Security", "soluciones.html#division=security")],
        big=True,
    ),
    dict(
        id="academy", name="NEX Academy", short="Academy", icon="academy", cls="d-aca",
        acc="#9d86ff", rgb="157,134,255", status="En desarrollo", kind="desarrollo",
        lead="Iniciativa de formación tecnológica.",
        summary="Una iniciativa en desarrollo orientada a la capacitación tecnológica.",
        items=[
            "Programación",
            "Redes",
            "Ciberseguridad",
            "Herramientas digitales",
            "Capacitación tecnológica",
        ],
        note="Todavía no hay cursos, certificaciones ni programas oficiales. Mientras tanto, los artículos educativos de Conocimiento y el cuestionario de NEX Security ofrecen material de aprendizaje.",
        links=[("Leer artículos educativos", "conocimiento.html#cat=educacion-tecnologica"),
               ("Hacer el cuestionario", "security.html#conciencia")],
        big=False,
    ),
    dict(
        id="labs", name="NEX Labs", short="Labs", icon="labs", cls="d-lab",
        acc="#8fa6ff", rgb="143,166,255", status="En desarrollo", kind="desarrollo",
        lead="Investigación e innovación tecnológica.",
        summary="Un área en desarrollo para experimentar con nuevas tecnologías.",
        items=[
            "Inteligencia artificial",
            "Automatización",
            "Internet de las cosas (IoT)",
            "Experimentación tecnológica",
            "Desarrollo de prototipos",
            "Integraciones digitales",
        ],
        note="No hay productos terminados. Cuando existan, los prototipos y conceptos se identificarán claramente como tales en Proyectos.",
        links=[("Ver cómo clasificamos los proyectos", "proyectos.html")],
        big=False,
    ),
    dict(
        id="connect", name="NEX Connect", short="Connect", icon="connect", cls="d-con",
        acc="#62c3ff", rgb="98,195,255", status="Concepto", kind="concepto",
        lead="Experiencia de relación con clientes.",
        summary="Una visión para dar seguimiento a solicitudes y mantener la comunicación con cada cliente.",
        items=[
            "Seguimiento de solicitudes",
            "Comunicación con CYBERNEX",
            "Historial de proyectos",
            "Centro de asistencia",
            "Acceso a información relevante",
        ],
        note="Todavía no existe un portal ni cuentas de usuario: aquí solo se explica cómo funcionará la experiencia.",
        links=[("Conocer la experiencia NEX Connect", "connect.html")],
        big=False,
    ),
]

# --------------------------------------------------------------------------------------
# Servicios (los seis de la presentación; el texto de "desc" es el original)
# --------------------------------------------------------------------------------------
SERVICE_GROUPS = [
    ("Seguridad y protección", "seguridad"),
    ("Soporte y asesoría", "soporte"),
    ("Formación", "formacion"),
]

SERVICES = [
    dict(group="seguridad", division="security", name="Seguridad informática",
         desc="Revisión de configuraciones, identificación de riesgos y recomendaciones para reducir vulnerabilidades.",
         problem="Equipos y cuentas con configuraciones débiles que pasan desapercibidas.",
         benefit="Una visión clara de los riesgos y de los pasos para reducirlos."),
    dict(group="seguridad", division="security", name="Seguridad de redes",
         desc="Configuración segura de redes y dispositivos, contraseñas robustas y recomendaciones de acceso.",
         problem="Redes y dispositivos con contraseñas débiles o accesos sin control.",
         benefit="Un acceso más ordenado y más difícil de vulnerar."),
    dict(group="seguridad", division="security", name="Protección de datos",
         desc="Configuración de respaldos, organización de archivos y orientación para recuperar información.",
         problem="Riesgo de perder información por una falla, un error o un incidente.",
         benefit="Respaldos configurados y orientación para recuperar lo importante."),
    dict(group="soporte", division="development", name="Mantenimiento técnico",
         desc="Diagnóstico, limpieza y mantenimiento preventivo y correctivo de equipos de cómputo.",
         problem="Equipos lentos, con fallas o sin mantenimiento.",
         benefit="Equipos en mejor estado de funcionamiento y con mayor vida útil."),
    dict(group="soporte", division="development", name="Asesoría tecnológica",
         desc="Orientación para elegir, configurar y utilizar herramientas y soluciones digitales.",
         problem="Dudas al elegir, configurar o usar herramientas digitales.",
         benefit="Decisiones tecnológicas mejor informadas."),
    dict(group="formacion", division="security", name="Capacitación digital",
         desc="Talleres básicos sobre contraseñas, phishing, privacidad, respaldos y navegación segura.",
         problem="Personas que no reconocen fraudes, phishing o malas prácticas digitales.",
         benefit="Hábitos digitales más seguros en el día a día."),
]

SERVICES_NOTE = ("Las evaluaciones y pruebas de seguridad se realizan únicamente con autorización expresa y alcance acordado. "
                 "Este sitio no publica tarifas: los valores que aparecen en la presentación son ilustrativos del proyecto académico.")

# --------------------------------------------------------------------------------------
# Ética y valores (textos originales de la presentación)
# --------------------------------------------------------------------------------------
PRINCIPLES = [
    ("Privacidad", "Proteger los datos personales y empresariales tratados durante cada servicio."),
    ("Confidencialidad", "Resguardar la información privada de clientes y colaboradores."),
    ("Honestidad", "Actuar con transparencia y verdad."),
    ("Integridad", "Actuar con honestidad y no alterar resultados, registros ni diagnósticos."),
    ("Legalidad", "Respetar las leyes, licencias y normas aplicables a la actividad."),
    ("Consentimiento", "Obtener autorización antes de intervenir o probar cualquier sistema."),
    ("Transparencia", "Explicar costos, alcance, riesgos y limitaciones del servicio."),
    ("Uso responsable", "No utilizar herramientas tecnológicas para dañar, espiar o perjudicar a terceros."),
    ("Protección de datos", "Resguardar la información de los clientes con medidas adecuadas y recomendar respaldos y buenas prácticas."),
    ("Respeto a los usuarios", "Trato digno a clientes y colaboradores."),
]

RULES = [
    "Respetar los horarios y jornadas laborales establecidos.",
    "Mantener la confidencialidad de los datos de los clientes.",
    "Usar los recursos de la empresa de manera responsable.",
    "Tratar con respeto a compañeros, proveedores y clientes.",
    "Cumplir las responsabilidades asignadas.",
    "Actualizar los conocimientos técnicos continuamente.",
    "No acceder a dispositivos, redes o información sin autorización.",
    "Reportar incidentes o posibles vulneraciones de seguridad.",
    "Mantener ordenadas las instalaciones y herramientas.",
    "Evitar conflictos de interés que puedan afectar al cliente.",
]

VALUES = [
    ("Responsabilidad", "Cumplir compromisos y cuidar los recursos."),
    ("Honestidad", "Actuar con transparencia y verdad."),
    ("Confidencialidad", "Resguardar la información privada."),
    ("Innovación", "Buscar mejores soluciones tecnológicas."),
    ("Respeto", "Trato digno a clientes y colaboradores."),
    ("Compromiso", "Trabajar para alcanzar objetivos."),
    ("Profesionalismo", "Actuar con preparación y calidad."),
    ("Colaboración", "Compartir conocimientos y trabajar en equipo."),
]

MISSION = ("Proporcionar soluciones tecnológicas y servicios de ciberseguridad que permitan a nuestros clientes proteger su información, "
           "optimizar sus recursos tecnológicos y desarrollar sus actividades digitales de manera segura y eficiente, "
           "mediante la innovación, la responsabilidad y la atención de calidad.")
VISION = ("Ser una empresa tecnológica reconocida a nivel regional por la calidad de sus servicios, su compromiso con la seguridad informática "
          "y su capacidad de innovación, convirtiéndonos en un aliado estratégico para personas y organizaciones.")

ORG = [
    ("Dirección general", "Planeación, coordinación y toma de decisiones."),
    ("Área tecnológica", "Soporte técnico, mantenimiento y prestación de servicios de ciberseguridad."),
    ("Marketing y ventas", "Publicidad, promoción, captación de clientes y comercialización de servicios."),
    ("Atención al cliente", "Recepción de solicitudes, asesoría, comunicación y seguimiento."),
]

PROCESS = [
    ("Solicitud", "El cliente comunica su necesidad o problema."),
    ("Diagnóstico", "Se analiza la situación y se identifica el alcance."),
    ("Acuerdo", "Se informan alcance, tiempo y condiciones antes de comenzar."),
    ("Autorización", "El cliente aprueba el trabajo antes de comenzar."),
    ("Ejecución", "Se realiza el trabajo de forma segura y documentada."),
    ("Entrega", "Se explican resultados y se ofrece seguimiento."),
]

TEAM = ["María Fernanda Merino Canela", "Gael Vidal Rojas"]

# Responsabilidad social y ambiental (basada en la sección original, ampliada con los temas del prompt)
RESPONSIBILITY = [
    ("Educación digital",
     "Compartimos recomendaciones para reconocer fraudes, proteger cuentas y navegar con seguridad. Los artículos y el cuestionario de este sitio son parte de ese compromiso."),
    ("Uso responsable de la tecnología",
     "Impulsamos el uso ético e inclusivo de la tecnología y el respeto a la privacidad. No usamos herramientas para dañar, espiar o perjudicar a terceros."),
    ("Protección de la información",
     "Tratamos la información de las personas como lo que es: algo que se cuida. Por eso las herramientas de este sitio procesan los datos en tu navegador."),
    ("Accesibilidad",
     "Buscamos que el sitio pueda usarse con teclado, con buen contraste y respetando la preferencia de reducir el movimiento. Es una práctica en mejora continua, no una certificación."),
    ("Eficiencia tecnológica",
     "Preferimos soluciones sencillas y ligeras: este sitio no usa bibliotecas externas ni carga recursos de terceros, lo que reduce el consumo de datos y energía."),
    ("Reducción del desperdicio electrónico",
     "Promovemos la reparación de equipos, el mantenimiento preventivo, el reciclaje electrónico y el consumo eficiente de energía."),
    ("Prácticas digitales responsables",
     "Animamos a usar contraseñas únicas, activar la verificación en dos pasos, hacer respaldos y verificar antes de compartir."),
]

# --------------------------------------------------------------------------------------
# Portafolio: solo trabajos que realmente existen
# --------------------------------------------------------------------------------------
PROJECT_STATUS = [
    ("realizado", "Realizado", "Terminado y en uso."),
    ("demo", "Demostración", "Funciona y puede probarse, con alcance educativo."),
    ("prototipo", "Prototipo", "Versión de prueba, todavía incompleta."),
    ("concepto", "Concepto", "Idea o diseño en desarrollo, sin implementación funcional."),
]

PROJECTS = [
    dict(status="realizado", kind="Proyecto académico",
         name="Presentación corporativa de CYBERNEX",
         desc="Presentación interactiva de 14 diapositivas para exponer el proyecto empresarial, con controles, atajos de teclado, pantalla completa y efectos de sonido.",
         goal="Presentar la empresa de forma clara, profesional y fácil de explicar en una exposición escolar.",
         tech="HTML, CSS, JavaScript y Web Audio API",
         state="Terminada. Se mantiene sin cambios en esta versión.",
         href="../index.html", cta="Abrir la presentación"),
    dict(status="demo", kind="Proyecto académico",
         name="NEX Security: centro de herramientas",
         desc="Cuatro herramientas educativas de ciberseguridad: Password Lab, URL Check, Security Checklist y Security Awareness.",
         goal="Enseñar buenas prácticas de seguridad con herramientas que funcionan sin enviar datos a ningún servidor.",
         tech="HTML, CSS y JavaScript (procesamiento local en el navegador)",
         state="Funcional con alcance educativo. No sustituye una auditoría profesional.",
         href="security.html", cta="Probar las herramientas"),
    dict(status="realizado", kind="Proyecto académico",
         name="Sitio web del ecosistema CYBERNEX",
         desc="Este sitio: divisiones, soluciones, conocimiento, ética y responsabilidad de CYBERNEX Solutions.",
         goal="Reunir en un solo lugar la identidad, los servicios y los compromisos de la empresa.",
         tech="HTML, CSS y JavaScript sin dependencias externas, alojado en GitHub Pages",
         state="Publicado. Se amplía por etapas.",
         href="index.html", cta="Ir al inicio"),
    dict(status="concepto", kind="Concepto en desarrollo",
         name="NEX Connect: experiencia de clientes",
         desc="Diseño de la experiencia de seguimiento y comunicación con clientes.",
         goal="Definir cómo se darán seguimiento a solicitudes y se mantendrá la comunicación con cada cliente.",
         tech="Por definir. La estructura de base de datos está preparada en la carpeta backend del proyecto, sin conexión.",
         state="Concepto. No existe un portal funcional ni cuentas de usuario.",
         href="connect.html", cta="Ver la propuesta"),
]

# --------------------------------------------------------------------------------------
# Preguntas frecuentes
# --------------------------------------------------------------------------------------
FAQ = [
    ("¿Qué es CYBERNEX Solutions?",
     "Es un proyecto empresarial académico de servicios tecnológicos especializados: ciberseguridad, soporte técnico y protección de información. Es una marca nueva, en etapa inicial."),
    ("¿Qué servicios ofrece?",
     "Seguridad informática, seguridad de redes, protección de datos, mantenimiento técnico, asesoría tecnológica y capacitación digital. Los detalles están en la sección Soluciones."),
    ("¿Hacen pruebas de seguridad en cualquier sistema?",
     "No. Las evaluaciones y pruebas de seguridad se realizan únicamente con autorización expresa y alcance acordado. Acceder a sistemas sin permiso va contra nuestras reglas y contra la ley."),
    ("¿Password Lab guarda mi contraseña?",
     "No. El análisis ocurre en tu navegador: la contraseña no se envía, no se guarda y no se registra. Aun así, te recomendamos probar con ejemplos y no con contraseñas que uses hoy."),
    ("¿URL Check confirma que un enlace es seguro?",
     "No. Solo revisa cómo está escrita la dirección y señala indicadores frecuentes de fraude. No abre el enlace ni consulta servicios externos, así que «sin indicadores» no significa «seguro»."),
    ("¿Existe un portal para clientes?",
     "Todavía no. NEX Connect es un concepto en desarrollo: no hay registro, inicio de sesión ni cuentas de usuario."),
    ("¿Ofrecen cursos o certificaciones?",
     "No por ahora. NEX Academy es una iniciativa en desarrollo y no existen cursos, certificaciones ni programas oficiales."),
    ("¿Cuánto cuestan los servicios?",
     "Este sitio no publica tarifas. Los valores que aparecen en la presentación son ilustrativos del proyecto académico."),
]

# --------------------------------------------------------------------------------------
# Artículos (contenido editorial de CYBERNEX; sin autores individuales)
# Bloques: ("p", texto) ("h2", texto) ("ul", [..]) ("ol", [..]) ("callout", texto, (href, etiqueta) | None)
# --------------------------------------------------------------------------------------
ARTICLE_DATE = "2026-11-18"
ARTICLE_DATE_LABEL = "18 de noviembre de 2026"

CATEGORIES = [
    ("ciberseguridad", "Ciberseguridad"),
    ("tecnologia", "Tecnología"),
    ("desarrollo-web", "Desarrollo web"),
    ("inteligencia-artificial", "Inteligencia artificial"),
    ("privacidad-digital", "Privacidad digital"),
    ("educacion-tecnologica", "Educación tecnológica"),
]

ARTICLES = [
    dict(slug="reconocer-correo-phishing", cat="ciberseguridad",
         title="Cómo reconocer un correo de phishing",
         excerpt="Las señales que se repiten en la mayoría de los mensajes fraudulentos y qué hacer cuando dudas.",
         body=[
             ("p", "El phishing es un intento de engañarte para que entregues contraseñas, datos bancarios o dinero haciéndote pasar por una persona o una empresa de confianza. Casi siempre llega por correo, mensaje de texto o redes sociales."),
             ("h2", "Señales que conviene revisar"),
             ("ul", [
                 "Urgencia o amenaza: «tu cuenta será bloqueada hoy», «último aviso».",
                 "Remitente extraño: el nombre parece correcto, pero la dirección de correo pertenece a otro dominio.",
                 "Enlaces que no coinciden: al pasar el cursor, la dirección real es distinta a la que aparece escrita.",
                 "Saludos genéricos y errores de redacción poco habituales en una empresa seria.",
                 "Peticiones de datos sensibles: contraseñas, códigos de verificación, NIP o el número completo de tu tarjeta.",
                 "Adjuntos inesperados, sobre todo archivos comprimidos.",
             ]),
             ("h2", "Qué hacer si dudas"),
             ("ul", [
                 "No hagas clic ni descargues nada del mensaje.",
                 "Entra por tu cuenta al sitio oficial escribiendo la dirección, o usa la aplicación oficial.",
                 "Confirma por otro medio con la persona o empresa que supuestamente lo envió.",
                 "Reporta el mensaje como phishing en tu servicio de correo y elimínalo.",
             ]),
             ("h2", "Si ya hiciste clic"),
             ("p", "Cambia de inmediato la contraseña de la cuenta afectada y de cualquier otra donde la repitas, activa la verificación en dos pasos y revisa los movimientos recientes. Si compartiste datos bancarios, avisa a tu banco."),
             ("callout", "Practica con mensajes ficticios y un cuestionario en NEX Security.", ("security.html#conciencia", "Abrir Security Awareness")),
         ]),
    dict(slug="verificacion-en-dos-pasos", cat="ciberseguridad",
         title="Verificación en dos pasos: qué es y por qué activarla",
         excerpt="Una segunda comprobación al iniciar sesión evita que una contraseña robada sea suficiente para entrar a tu cuenta.",
         body=[
             ("p", "La verificación en dos pasos (también llamada autenticación de dos factores o 2FA) añade una segunda comprobación al iniciar sesión, además de la contraseña. Así, aunque alguien consiga tu contraseña, todavía le falta ese segundo elemento."),
             ("h2", "Tipos de segundo factor"),
             ("ul", [
                 "Aplicación de autenticación: genera códigos que cambian cada pocos segundos. Es una opción equilibrada entre seguridad y comodidad.",
                 "Llave de seguridad física: es la opción más resistente al phishing.",
                 "Mensaje de texto (SMS): es mejor que no tener nada, pero es más fácil de interceptar o de redirigir, por ejemplo mediante el cambio de SIM.",
                 "Códigos de respaldo: se guardan en un lugar seguro por si pierdes el teléfono.",
             ]),
             ("h2", "Dónde activarla primero"),
             ("p", "Empieza por el correo electrónico, porque suele servir para recuperar todas las demás cuentas. Después sigue con la banca, las redes sociales, el almacenamiento en la nube y las cuentas de trabajo."),
             ("h2", "Buenas prácticas"),
             ("ul", [
                 "Guarda los códigos de respaldo fuera del teléfono.",
                 "No compartas nunca un código de verificación, ni siquiera con alguien que diga ser de soporte.",
                 "Revisa de vez en cuando los dispositivos con sesión abierta y cierra los que no reconozcas.",
             ]),
         ]),
    dict(slug="proteger-datos-personales", cat="privacidad-digital",
         title="Guía básica para proteger tus datos personales en línea",
         excerpt="Hábitos sencillos para compartir menos, controlar quién ve tu información y limpiar lo que ya no usas.",
         body=[
             ("p", "Cada registro, formulario y aplicación recoge información sobre ti. Proteger tus datos personales empieza por decidir qué compartes, con quién y durante cuánto tiempo."),
             ("h2", "Antes de compartir"),
             ("ul", [
                 "Pregúntate si el servicio realmente necesita ese dato.",
                 "Lee qué permisos pide una aplicación y desactiva los que no necesite, como ubicación, contactos o micrófono.",
                 "Usa alias o correos distintos para registros poco importantes.",
             ]),
             ("h2", "En tus cuentas"),
             ("ul", [
                 "Configura la privacidad de tus redes sociales: quién ve tus publicaciones y tu lista de contactos.",
                 "Revisa periódicamente qué aplicaciones tienen acceso a tu cuenta y elimina las que no uses.",
                 "Cierra las cuentas que ya no utilizas.",
             ]),
             ("h2", "Al navegar"),
             ("ul", [
                 "Mantén el navegador actualizado.",
                 "Evita iniciar sesión en equipos compartidos; si es inevitable, cierra sesión al terminar.",
                 "Desconfía de formularios que piden más datos de los necesarios.",
             ]),
             ("callout", "Lo que publicas hoy puede ser difícil de borrar mañana. Compartir menos es la forma más sencilla de proteger tu privacidad.", None),
         ]),
    dict(slug="respaldos-regla-3-2-1", cat="tecnologia",
         title="La regla 3-2-1 para tus respaldos",
         excerpt="Una guía simple para organizar copias de seguridad que sí te sirvan cuando las necesites.",
         body=[
             ("p", "Un respaldo es una copia de tu información que puedes usar si pierdes el original por una falla, un robo, un error o un ataque. La regla 3-2-1 es una guía sencilla para organizarlos."),
             ("h2", "En qué consiste"),
             ("ul", [
                 "3 copias de tus datos: el original y dos respaldos.",
                 "2 tipos de medio distintos, por ejemplo un disco externo y almacenamiento en la nube.",
                 "1 copia fuera del lugar donde trabajas, para protegerte de robo, incendio o inundación.",
             ]),
             ("h2", "Para que funcione"),
             ("ul", [
                 "Automatiza los respaldos: los manuales se olvidan.",
                 "Prueba restaurar un archivo de vez en cuando; un respaldo que no se ha probado puede no servir.",
                 "Protege con contraseña o cifrado los respaldos que contengan información sensible.",
                 "Mantén al menos una copia desconectada del equipo, porque algunos programas maliciosos también cifran los discos conectados.",
             ]),
             ("p", "No existe una frecuencia universal: depende de cuánto trabajo estarías dispuesto a perder. Si perder el trabajo de un día es demasiado, respalda a diario."),
         ]),
    dict(slug="https-candado-navegador", cat="desarrollo-web",
         title="HTTPS y el candado del navegador: qué garantiza y qué no",
         excerpt="El candado indica una conexión cifrada, no que el sitio sea confiable. Cómo interpretarlo bien.",
         body=[
             ("p", "HTTPS cifra la comunicación entre tu navegador y un sitio web. Esto evita que otras personas en la misma red lean o modifiquen lo que envías, como una contraseña."),
             ("h2", "Lo que sí garantiza"),
             ("ul", [
                 "Que los datos viajan cifrados.",
                 "Que la conexión es con el dominio que aparece en la barra de direcciones y no con un intermediario.",
             ]),
             ("h2", "Lo que no garantiza"),
             ("ul", [
                 "Que el sitio sea honesto: cualquier persona puede obtener un certificado para su propio dominio, incluso un sitio fraudulento.",
                 "Que el dominio sea el que esperas: un sitio con una dirección parecida también puede mostrar el candado.",
                 "Que el sitio proteja bien tus datos una vez que los recibe.",
             ]),
             ("h2", "Qué revisar además"),
             ("ul", [
                 "Lee con atención el dominio completo, no solo el principio.",
                 "Desconfía de enlaces recibidos por mensaje; escribe la dirección o usa tus marcadores.",
                 "Si desarrollas sitios: sirve todo por HTTPS, redirige desde HTTP y evita cargar recursos mixtos.",
             ]),
             ("callout", "Mira cómo se analiza la escritura de una dirección con URL Check.", ("security.html#url", "Abrir URL Check")),
         ]),
    dict(slug="accesibilidad-web-basica", cat="desarrollo-web",
         title="Accesibilidad web: cinco comprobaciones básicas",
         excerpt="Revisiones rápidas para que un sitio pueda usarse con teclado, lector de pantalla y poca visibilidad.",
         body=[
             ("p", "Un sitio accesible puede usarse con teclado, lector de pantalla, zoom o en condiciones de poca visibilidad. Además de ser lo correcto, suele mejorar la experiencia de todas las personas."),
             ("h2", "Cinco comprobaciones"),
             ("ol", [
                 "Contraste: el texto normal necesita una relación de contraste de al menos 4.5:1 con el fondo (nivel AA de WCAG 2.1).",
                 "Teclado: puedes llegar a cada enlace, botón y campo con la tecla Tab, y siempre ves dónde está el foco.",
                 "Textos alternativos: las imágenes que aportan información tienen una descripción breve; las decorativas, no.",
                 "Etiquetas en formularios: cada campo tiene una etiqueta visible asociada, no solo un texto de ayuda dentro del campo.",
                 "Estructura: una jerarquía de títulos lógica (un h1, luego h2 y h3) y regiones como cabecera, navegación y contenido principal.",
             ]),
             ("p", "Estas comprobaciones no sustituyen una auditoría completa, pero detectan muchos problemas frecuentes. También conviene respetar la preferencia del sistema de reducir el movimiento."),
         ]),
    dict(slug="ia-uso-responsable", cat="inteligencia-artificial",
         title="Usar herramientas de inteligencia artificial con responsabilidad",
         excerpt="Qué no compartir, cómo verificar las respuestas y quién sigue siendo responsable del resultado.",
         body=[
             ("p", "Los asistentes de inteligencia artificial pueden ahorrar tiempo, pero introducen riesgos si se usan sin criterio."),
             ("h2", "Antes de escribir un mensaje"),
             ("ul", [
                 "No pegues contraseñas, datos personales de terceros, información confidencial de una empresa ni documentos que no tengas permiso de compartir.",
                 "Revisa la política de privacidad del servicio: algunos pueden conservar las conversaciones o usarlas para mejorar el servicio.",
             ]),
             ("h2", "Al usar las respuestas"),
             ("ul", [
                 "Verifica los datos importantes en fuentes confiables: estas herramientas pueden dar información incorrecta con mucha seguridad.",
                 "No copies código, textos o imágenes sin revisarlos ni sin respetar licencias y derechos de autor.",
                 "Indica cuando un contenido fue elaborado con ayuda de IA si el contexto lo requiere, por ejemplo en trabajos escolares o publicaciones.",
             ]),
             ("h2", "Una regla práctica"),
             ("p", "Trata a un asistente de IA como a un colaborador rápido pero no infalible: puede ayudarte a empezar, pero tú sigues siendo responsable del resultado."),
         ]),
    dict(slug="contrasenas-largas-recordables", cat="educacion-tecnologica",
         title="Cómo crear una contraseña larga que sí puedas recordar",
         excerpt="La longitud aporta más seguridad que los símbolos. Cómo armar una frase de contraseña y qué evitar.",
         body=[
             ("p", "La longitud aporta más seguridad que añadir símbolos a una palabra corta. Por eso se recomiendan las frases de contraseña: varias palabras sin relación entre sí."),
             ("h2", "Cómo crearla"),
             ("ol", [
                 "Elige cuatro o más palabras al azar, sin relación personal: evita nombres, fechas o frases famosas.",
                 "Únelas con un separador, como guiones.",
                 "Si el sitio lo exige, añade números o símbolos, sin convertir la frase en algo predecible.",
                 "Úsala solo en una cuenta.",
             ]),
             ("h2", "Qué evitar"),
             ("ul", [
                 "Nombres de mascotas, familiares, equipos o fechas de nacimiento.",
                 "Sustituciones previsibles, como una @ en lugar de una a o un 0 en lugar de una o.",
                 "Reutilizar la misma contraseña con pequeños cambios.",
             ]),
             ("h2", "Y para todo lo demás"),
             ("p", "Nadie puede recordar docenas de contraseñas largas y distintas. Un gestor de contraseñas las guarda por ti: solo necesitas recordar una contraseña maestra fuerte y activar la verificación en dos pasos."),
             ("callout", "Evalúa una contraseña de prueba (no una que uses) con Password Lab.", ("security.html#password", "Abrir Password Lab")),
         ]),
    dict(slug="alargar-vida-equipos", cat="tecnologia",
         title="Cómo alargar la vida útil de tus equipos y reducir residuos electrónicos",
         excerpt="Mantenimiento básico, qué revisar antes de reemplazar un equipo y qué hacer cuando ya no sirve.",
         body=[
             ("p", "Fabricar un equipo nuevo consume materiales y energía, y los aparatos desechados generan residuos electrónicos que requieren un manejo especial. Cuidar los que ya tienes es la medida más simple."),
             ("h2", "Mantenimiento básico"),
             ("ul", [
                 "Limpia el polvo de ventiladores y rejillas con regularidad para evitar el sobrecalentamiento.",
                 "Mantén actualizados el sistema y los programas: también mejora la seguridad.",
                 "Libera espacio y desinstala lo que no uses.",
                 "Cuida las baterías: evita temperaturas extremas.",
             ]),
             ("h2", "Antes de reemplazar"),
             ("ul", [
                 "Consulta si basta con ampliar la memoria o cambiar el disco por uno de estado sólido.",
                 "Pide un diagnóstico: muchas fallas se pueden reparar.",
             ]),
             ("h2", "Cuando ya no sirve"),
             ("ul", [
                 "Respalda tu información y borra el equipo de forma segura antes de entregarlo.",
                 "No lo tires a la basura común: busca centros de acopio o programas de reciclaje electrónico de tu localidad.",
                 "Si aún funciona, considera donarlo o venderlo.",
             ]),
         ]),
]

# --------------------------------------------------------------------------------------
# Páginas legales (plantillas informativas, no verificadas legalmente)
# --------------------------------------------------------------------------------------
LEGAL_NOTICE = ("Este documento es una plantilla informativa y adaptable. Describe cómo funciona este sitio hoy, "
                "pero no ha sido revisado por un profesional jurídico ni declara cumplimiento de ninguna ley. "
                "Antes de un uso comercial real debe adaptarse y validarse con asesoría legal.")

PRIVACY = [
    ("Quién publica este sitio",
     ["CYBERNEX Solutions es un proyecto empresarial académico. Los datos de contacto del responsable todavía no están publicados."]),
    ("Qué información recopila este sitio",
     ["Ninguna. Este sitio es estático: no tiene formularios que envíen datos, cuentas de usuario, cookies propias, estadísticas ni publicidad.",
      "No carga fuentes, scripts ni recursos de terceros."]),
    ("Qué ocurre en las herramientas de NEX Security",
     ["Password Lab: la contraseña se analiza en tu navegador. No se envía, no se guarda y no se registra.",
      "URL Check: analiza el texto del enlace en tu navegador. No abre el enlace ni lo envía a ningún servicio.",
      "Security Checklist: tu avance se guarda únicamente en el almacenamiento local de tu propio navegador. Puedes borrarlo con el botón «Reiniciar lista» o limpiando los datos del sitio."]),
    ("Alojamiento",
     ["El sitio se publica en GitHub Pages. El proveedor puede registrar datos técnicos de conexión, como la dirección IP, conforme a su propia política de privacidad."]),
    ("Correo electrónico",
     ["Si en el futuro se publica un correo de contacto, al pulsarlo se abrirá tu programa de correo. El mensaje no se envía hasta que tú lo envíes."]),
    ("Cambios en este aviso",
     ["Si el sitio cambia y comienza a tratar datos personales, este aviso deberá actualizarse antes de publicar el cambio."]),
]

TERMS = [
    ("Naturaleza del sitio",
     ["Este sitio presenta un proyecto empresarial académico. La información tiene fines informativos y educativos."]),
    ("Herramientas educativas",
     ["Las herramientas de NEX Security son orientativas. No detectan todas las amenazas ni sustituyen una auditoría de seguridad profesional.",
      "«Sin indicadores» en URL Check no significa que un enlace sea seguro, y una puntuación alta en Password Lab no garantiza que una contraseña no haya sido filtrada."]),
    ("Uso responsable",
     ["Te pedimos usar el contenido y las herramientas de forma lícita y ética. No utilices la información de este sitio para dañar, espiar o perjudicar a terceros ni para acceder a sistemas sin autorización."]),
    ("Servicios y disponibilidad",
     ["Algunas divisiones del ecosistema están en desarrollo o son conceptos. Su descripción no constituye una oferta ni una promesa de disponibilidad.",
      "Este sitio no publica tarifas."]),
    ("Propiedad intelectual",
     ["El nombre, el logotipo y los textos de CYBERNEX Solutions pertenecen al proyecto. Las marcas de terceros mencionadas en ejemplos pertenecen a sus propietarios y se usan solo como referencia educativa."]),
    ("Enlaces",
     ["Este sitio puede enlazar a páginas externas sobre las que no tenemos control ni responsabilidad."]),
    ("Cambios",
     ["Estos términos pueden modificarse. La versión vigente es la publicada en esta página."]),
]
