# CYBERNEX Solutions 10.0V — Ecosistema (Entrega 1)

Proyecto académico de CYBERNEX Solutions: ciberseguridad, soporte tecnológico y servicios digitales.
**Lema:** Tecnología que conecta. Seguridad que empodera.

> **Estado:** esta es la **Entrega 1** de la versión 10.0V. Incluye la estructura del ecosistema y la división
> **NEX Security** completamente funcional. Las demás divisiones (Development, Academy, Labs, Connect), el blog,
> el portafolio, el contacto y el panel administrativo **todavía no están construidos** (ver «Pendiente»).

## Qué contiene

| Ruta | Descripción |
|---|---|
| `index.html` | **Presentación CYBERNEX 6.1** (14 diapositivas, sonidos, controles y atajos). Intacta salvo 2 enlaces nuevos al ecosistema. |
| `ecosistema/index.html` | Portada del ecosistema con las cinco divisiones y su estado real. |
| `ecosistema/security.html` | **NEX Security**: Password Lab, URL Check, Security Checklist y Security Awareness. |
| `assets/css/eco.css` | Estilos compartidos del ecosistema (misma identidad visual). |
| `assets/js/*.js` | Lógica modular: `password.js`, `urlcheck.js`, `checklist.js`, `awareness.js`, `security-ui.js`, `eco.js`. |
| `backend/` | Base **preparada y no conectada** para NEX Connect (esquema de Supabase, variables de entorno). |

Tecnologías: HTML, CSS y JavaScript puros. Sin frameworks, sin bibliotecas externas, sin peticiones de red.

## Ejecución local
No requiere instalación. Abre `index.html` con doble clic en Google Chrome (la presentación) o entra al ecosistema
con el botón **«Explorar el ecosistema»** / el enlace **Ecosistema** del menú.
Opcional, con servidor local: `python3 -m http.server 8000` y abre `http://localhost:8000`.

## Despliegue en GitHub Pages
1. Sube el contenido de esta carpeta a la raíz de un repositorio de GitHub (sin `.env`).
2. En **Settings → Pages**, elige la rama `main` y la carpeta `/ (root)`.
3. La presentación queda en `https://TU-USUARIO.github.io/TU-REPO/` y el ecosistema en `.../ecosistema/`.
Todas las rutas son relativas, por lo que funciona en subcarpetas de GitHub Pages.

## Variables de entorno
El sitio actual **no usa variables de entorno** (es estático). Las variables del futuro backend están documentadas
en `backend/.env.example`. La clave `SUPABASE_SERVICE_ROLE_KEY` nunca debe ir en el frontend ni en el repositorio.

## Funcionalidades de NEX Security
- **Password Lab:** evalúa longitud, variedad de caracteres, repeticiones, secuencias, filas del teclado y contraseñas
  comunes (lista breve incorporada). Muestra criterios, recomendaciones, entropía estimada y un tiempo de ataque
  **orientativo**. Incluye un generador con `crypto.getRandomValues`. **Procesamiento 100 % local: no se envía, guarda ni registra la contraseña.**
- **URL Check:** analiza cómo está escrita una dirección: HTTPS, IP en lugar de dominio, «@», punycode, subdominios excesivos,
  acortadores, extensiones frecuentes en fraude, suplantación de marcas, palabras sensibles, puerto, longitud y codificación.
  **No abre el enlace ni consulta servicios externos.** «Sin indicadores» nunca se presenta como «seguro».
  La comprobación con fuentes de reputación (p. ej. Google Safe Browsing) requiere clave de API y servidor: está documentada, no implementada.
- **Security Checklist:** 24 buenas prácticas en cuatro grupos (cuentas, dispositivos, navegación, empresas) con avance guardado
  solo en el navegador (`localStorage`).
- **Security Awareness:** cuestionario de 8 preguntas con explicaciones, 3 ejemplos de phishing **ficticios** con señales de alerta
  y 6 buenas prácticas.

Estas herramientas son educativas y orientativas. No sustituyen una auditoría profesional ni detectan todas las amenazas.

## Registro de cambios respecto a la versión 6.1
- **Presentación:** sin cambios de contenido, diapositivas, sonidos, animaciones ni controles. Solo se añadieron
  el enlace «Ecosistema» en el menú y el botón «Explorar el ecosistema» en la bienvenida (2 líneas).
- **Nuevo:** `ecosistema/` (portada y NEX Security), `assets/` (CSS y JS modulares), `backend/` (base preparada) y este README.
- **Idioma:** todo en español, incluido el lema («Tecnología que conecta. Seguridad que empodera.»). Se conservan los nombres de
  producto (NEX Security, Password Lab, URL Check, etc.).
- Se mantiene la nota ya existente de la 6.1 sobre precios ilustrativos del proyecto académico.

## Pruebas realizadas (resultados)
Automáticas, en Node/jsdom y Chrome sin interfaz:
- **Lógica (26 comprobaciones): correcto.** Contraseñas comunes/débiles/fuertes, generador (longitud, 4 clases, sin repetición, límites),
  URL (inválidas, IP, «@», acortador, punycode, suplantación, sitios conocidos sin falsos positivos).
- **Interfaz de NEX Security (todas correctas):** pestañas con teclado, Password Lab, URL Check, 24 casillas del checklist con guardado y reinicio,
  cuestionario completo, sin inyección de HTML y sin llamadas de red en las herramientas.
- **Presentación:** misma batería que la 6.1 (navegación, 14 diapositivas, atajos, salir, Finalizar): correcta.
- **Enlaces locales:** 34 revisados, 0 rotos. **Consola de Chrome:** 0 errores en las 3 páginas.
- **Visual:** capturas revisadas en escritorio (1366 px) y móvil (390 px).

**No verificado:** audio y pantalla completa reales, lectores de pantalla, Safari/Firefox, proyector, el esquema SQL contra una base real
y la auditoría de dependencias (no hay dependencias externas).

## Pendiente (siguientes entregas)
NEX Development (servicios y solicitudes), NEX Academy, NEX Labs (distinguiendo terminado/prototipo/concepto), NEX Connect e interfaz del panel
administrativo, portafolio, artículos con buscador, formulario de contacto validado y conexión real con el backend.
No se incluyen proyectos, clientes, estadísticas ni certificaciones: no existen en el material original y no se inventan.
Los datos de contacto corporativos no se publican porque no figuran en el proyecto original.
