# CYBERNEX Solutions 10.0V — Renovación del ecosistema digital

Proyecto empresarial académico de CYBERNEX Solutions: ciberseguridad, soporte técnico y protección de información.
**Lema:** «Tu información, nuestra prioridad». **Frase:** «Protegemos tu mundo digital.»

Sitio estático (HTML, CSS y JavaScript puros), listo para **GitHub Pages**. Sin frameworks, sin bibliotecas externas,
sin fuentes de terceros y sin peticiones de red.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html` | **Presentación corporativa 6.1** (14 diapositivas, sonidos, controles, atajos). Sin cambios de contenido; solo se añadieron 2 enlaces al ecosistema y metadatos SEO en `<head>`. |
| `ecosistema/index.html` | Portada renovada: hero con diagrama interactivo del ecosistema, divisiones, «Disponible hoy», ética, artículos. |
| `ecosistema/divisiones.html` | Las cinco divisiones con su estado real. |
| `ecosistema/soluciones.html` | Servicios por categoría, con filtro por división. Sin cotizaciones ni tarifas. |
| `ecosistema/proyectos.html` | Portafolio clasificado en realizado / demostración / prototipo / concepto, con estado vacío preparado. |
| `ecosistema/conocimiento.html` + `articulos/*.html` | Centro de conocimiento: 9 artículos, 6 categorías, búsqueda y lectura individual. |
| `ecosistema/etica.html`, `responsabilidad.html`, `sobre.html` | Tecnología con responsabilidad; responsabilidad social y ambiental; institucional. |
| `ecosistema/connect.html` | Experiencia NEX Connect (concepto, 5 pasos). No es un portal. |
| `ecosistema/contacto.html` | Contacto y soporte: información, centro de ayuda y preguntas frecuentes. |
| `ecosistema/security.html` | **NEX Security**: Password Lab, URL Check, Security Checklist y Security Awareness (funcionales). |
| `ecosistema/privacidad.html`, `terminos.html` | Plantillas informativas (no son declaraciones de cumplimiento legal). |
| `assets/css/site.css`, `security.css` | Sistema de diseño y estilos de las herramientas. |
| `assets/js/` | `site.js` (menú, encabezado, volver arriba, contacto), `filters.js`, `site-config.js`, y la lógica de NEX Security. |
| `assets/img/` | `favicon.svg`, `og-cybernex.png` (imagen para compartir, 1200×630). |
| `backend/` | Base **preparada y no conectada** (esquema SQL de Supabase y variables de entorno de ejemplo). |
| `tools/` | Generador de páginas (`build_site.py`) y contenido (`content.py`). |
| `sitemap.xml`, `robots.txt` | SEO. |

## Ejecución local
No requiere instalación: abre `index.html` (presentación) o `ecosistema/index.html` en Chrome.
Con servidor local (opcional): `python3 -m http.server 8000` y abre `http://localhost:8000`.

## Publicar en GitHub Pages
1. Sube el contenido de esta carpeta a la raíz del repositorio (sin archivos `.env`).
2. **Settings → Pages →** rama `main`, carpeta `/ (root)`.
3. La presentación queda en `https://fercnx.github.io/CyberNex-Solutions/` y el ecosistema en `.../ecosistema/`.

Todas las rutas son relativas, así que funciona en subcarpetas de GitHub Pages. El HTML generado ya está incluido: **no hay paso de compilación**.

## Editar el contenido
Todo el texto del ecosistema vive en `tools/content.py`. Tras modificarlo, regenera las páginas:

```
python3 tools/build_site.py
```
Esto reescribe `ecosistema/*.html`, `sitemap.xml` y `robots.txt` (requiere Python 3; no usa paquetes externos).
Para añadir un artículo, agrega un elemento a `ARTICLES`; para un proyecto, a `PROJECTS`.

## Configurar el contacto
No se publican teléfonos, direcciones, correos ni redes sociales porque no existen en el proyecto original, y **no hay formulario**
para no aparentar envíos que no llegarían a nadie. Cuando exista un correo oficial, escríbelo en `assets/js/site-config.js`:

```js
window.CYBERNEX_CONFIG = { contactEmail: "correo@tudominio.com" };
```
Esto muestra automáticamente el botón «Escribir un correo» (enlace `mailto:`) y el correo en el pie de página. Nunca pongas claves ni contraseñas en ese archivo.

## Seguridad y privacidad
- Las herramientas de NEX Security procesan todo en el navegador: no envían ni guardan contraseñas ni enlaces.
- URL Check solo analiza cómo está escrita la dirección; «sin indicadores» no significa «seguro».
- El Checklist guarda solo tu avance en `localStorage`. NEX Connect no guarda información sensible.
- `backend/` documenta una futura conexión (Supabase). La clave `SUPABASE_SERVICE_ROLE_KEY` nunca debe ir en el frontend ni en el repositorio.

## Qué cambió respecto a la Entrega 1 y la versión 6.1
- **Nuevo diseño** del ecosistema: identidad propia por división (color y forma), hero con diagrama interactivo, encabezado que cambia al desplazarse, botón de volver arriba y menú móvil.
- **Nuevo:** divisiones, soluciones, proyectos, conocimiento (9 artículos), ética, responsabilidad, sobre, NEX Connect, contacto/ayuda/FAQ, páginas legales informativas, SEO (canonical, Open Graph, Twitter, JSON-LD, sitemap, robots).
- **Conservado:** presentación 6.1 intacta y las cuatro herramientas de NEX Security (lógica sin cambios).
- **Refactor:** `eco.css`/`eco.js` se sustituyen por `site.css`, `security.css` y `site.js`; las páginas se generan desde una única fuente de contenido para evitar duplicación.
- **Lema:** ahora «Tu información, nuestra prioridad» (antes «Tecnología que conecta. Seguridad que empodera.», que se conserva como descriptor interno).
- Se retiró el paso «Cotización» del proceso mostrado en el ecosistema (ahora «Acuerdo»), por la indicación de no incluir cotizaciones.

## Decisiones y supuestos a revisar
- **Servicios → divisiones:** la asignación (p. ej. Mantenimiento técnico → NEX Development) es una suposición mía; el proyecto original no la define.
- **Fecha de los artículos:** todos llevan la fecha de redacción de esta versión (18 de noviembre de 2026), firmados como «Editorial CYBERNEX», sin autores inventados.
- **Equipo:** se muestran solo los nombres de las dos personas integrantes presentes en el proyecto.
- **Precios:** el ecosistema no publica tarifas; los de la presentación siguen marcados como ilustrativos.
- **`robots.txt`:** en GitHub Pages de proyecto (`usuario.github.io/repo/`) los buscadores solo leen `robots.txt` en la raíz del dominio, por lo que este archivo no tendrá efecto allí; el `sitemap.xml` sí puede enviarse en Search Console.

## Pruebas realizadas
Automáticas en Chrome sin interfaz (Playwright):
- **Enlaces locales:** 921 revisados (incluye anclas), 0 rotos.
- **Consola:** 0 errores ni avisos en 14 páginas, en escritorio (1366 px) y móvil (390 px); sin desbordamiento horizontal.
- **Funcionalidad (28 comprobaciones):** filtros y búsqueda (con enlace directo por `#`), estados vacíos, menú móvil y Escape, encabezado al desplazar, volver arriba, canal de contacto con y sin correo configurado, pestañas de NEX Security por enlace directo, URL Check, Password Lab, generador, 24 casillas, cuestionario, salto al contenido con teclado.
- **Presentación:** entrada, inicio, recorrido con flechas por las 14 diapositivas, salida con Esc, sin errores; diferencia con la 6.1 limitada a los 2 enlaces y los metadatos.
- **Visual:** capturas revisadas en escritorio y móvil.

**No verificado:** audio real y pantalla completa, lectores de pantalla, Safari/Firefox, el esquema SQL contra una base real, el rendimiento medido con Lighthouse.

## Pendiente
Backend y autenticación reales (NEX Connect), formulario conectado a un servicio, panel administrativo, cursos de NEX Academy y productos de NEX Labs: no existen todavía y no se presentan como disponibles.
