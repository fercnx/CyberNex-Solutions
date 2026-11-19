#!/usr/bin/env python3
"""CYBERNEX 10.0V — generador del sitio estático del ecosistema.

Lee el contenido de tools/content.py y escribe las páginas HTML en ecosistema/,
sitemap.xml y robots.txt. El HTML generado se versiona, así que GitHub Pages
no necesita ningún paso de compilación.

Uso:  python3 tools/build_site.py
"""
import html
import json
import math
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

BASE = "https://fercnx.github.io/CyberNex-Solutions/"
SITE = "CYBERNEX Solutions"
OUT = os.path.join(ROOT, "ecosistema")
OG_IMAGE = BASE + "assets/img/og-cybernex.png"
e = html.escape

DIV = {d["id"]: d for d in C.DIVISIONS}
CAT = dict(C.CATEGORIES)

# ---------------------------------------------------------------- iconos
_ICONS = {
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/><path d="m14 4-4 16"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "academy": '<path d="m2 9 10-5 10 5-10 5-10-5Z"/><path d="M6 11.5V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.5"/>',
    "labs": '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7.5 15h9"/>',
    "connect": '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="m8.2 10.8 7.6-3.6M8.2 13.2l7.6 3.6"/>',
    "up": '<path d="m6 15 6-6 6 6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % _ICONS[name])


def logo(gid):
    return ('<svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="%s" x1="10" y1="4" x2="54" y2="60" '
            'gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2f7bff"/><stop offset="1" stop-color="#8f6cff"/>'
            '</linearGradient></defs><path d="M32 6 51 13.5V29c0 13-8 22.5-19 28C21 51.5 13 42 13 29V13.5L32 6Z" fill="url(#%s)"/>'
            '<path d="M32 12 45 17.5V29c0 9.5-5.5 16.5-13 21-7.5-4.5-13-11.5-13-21V17.5L32 12Z" fill="#03060d" fill-opacity=".35"/>'
            '<path d="m23.5 31 6.5 6.5L41.5 24" fill="none" stroke="#72e6ff" stroke-width="5" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>' % (gid, gid))


# Formas propias de cada división (viewBox 0 0 200 200)
_SHAPES = {
    "development": '<rect x="28" y="28" width="144" height="144" rx="30"/><rect x="62" y="62" width="76" height="76" rx="14" stroke-dasharray="3 7"/>',
    "security": '<path d="M100 18 172 46v52c0 42-29 68-72 84-43-16-72-42-72-84V46Z"/><path d="M100 46 146 64v36c0 26-18 44-46 55-28-11-46-29-46-55V64Z" stroke-dasharray="3 7"/>',
    "academy": '<path d="M100 18 172 59v82l-72 41-72-41V59Z"/><path d="M100 50 146 76v52l-46 26-46-26V76Z" stroke-dasharray="3 7"/>',
    "labs": '<circle cx="100" cy="100" r="76"/><ellipse cx="100" cy="100" rx="76" ry="30" transform="rotate(-30 100 100)" stroke-dasharray="3 7"/><circle cx="154" cy="69" r="7"/>',
    "connect": '<circle cx="46" cy="100" r="20"/><circle cx="150" cy="46" r="20"/><circle cx="150" cy="154" r="20"/><path d="M64 91 132 55M64 109l68 36" stroke-dasharray="3 7"/>',
}


def shape(did):
    return ('<svg class="shape" viewBox="0 0 200 200" fill="rgba(var(--acc-rgb),.07)" stroke="var(--acc)" '
            'stroke-width="1.6" stroke-linejoin="round" aria-hidden="true">%s</svg>' % _SHAPES[did])


# ---------------------------------------------------------------- navegación
NAV = [
    ("divisiones.html", "Divisiones"),
    ("soluciones.html", "Soluciones"),
    ("proyectos.html", "Proyectos"),
    ("conocimiento.html", "Conocimiento"),
    ("etica.html", "Ética"),
    ("sobre.html", "Sobre CYBERNEX"),
]
LEGAL = [("privacidad.html", "Aviso de privacidad"), ("terminos.html", "Términos y condiciones")]


def pagehead(name, title, desc, depth, current, ld=None, og_type="website"):
    pre = "../" * (depth + 1)          # hacia la raíz del proyecto
    here = "../" * depth               # hacia ecosistema/
    url = BASE + "ecosistema/" + name
    full_title = title if title.startswith(SITE) else "%s — %s" % (title, SITE)
    ld_tags = "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in (ld or []))
    return pre, here, """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#03060d">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/svg+xml" href="{pre}assets/img/favicon.svg">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{site}">
<meta property="og:locale" content="es_MX">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="CYBERNEX Solutions — Tu información, nuestra prioridad">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og}">
<link rel="stylesheet" href="{pre}assets/css/site.css">
{{extra_css}}{ld}</head>
""".format(title=e(full_title), desc=e(desc), url=url, pre=pre, site=SITE, og=OG_IMAGE, og_type=og_type, ld=ld_tags)


def header(here, pre, current):
    links = "".join(
        '<a href="%s%s"%s>%s</a>' % (here, h, ' aria-current="page"' if h == current else "", t) for h, t in NAV)
    cta_cur = ' aria-current="page"' if current == "contacto.html" else ""
    return """<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="header">
  <div class="container nav">
    <a class="brand" href="{here}index.html" aria-label="CYBERNEX Solutions, inicio del ecosistema"><span class="brand-icon">{logo}</span><span>CYBERNEX<small>S O L U T I O N S</small></span></a>
    <nav class="navlinks" id="navLinks" aria-label="Navegación principal">
      {links}<a class="nav-cta" href="{here}contacto.html"{cta_cur}>Contacto</a>
    </nav>
    <button class="menu" id="menuBtn" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="navLinks">☰</button>
  </div>
</header>
""".format(here=here, logo=logo("gH"), links=links, cta_cur=cta_cur)


def footer(here, pre):
    divs = "".join('<li><a href="%s%s">%s</a></li>' % (here, "security.html" if d["id"] == "security" else "divisiones.html#" + d["id"], d["name"]) for d in C.DIVISIONS)
    nav = "".join('<li><a href="%s%s">%s</a></li>' % (here, h, t) for h, t in NAV)
    nav += '<li><a href="%sresponsabilidad.html">Responsabilidad social y ambiental</a></li>' % here
    nav += '<li><a href="%sindex.html">Inicio del ecosistema</a></li>' % here
    nav += '<li><a href="%sindex.html">Presentación corporativa</a></li>' % pre
    legal = "".join('<a href="%s%s">%s</a>' % (here, h, t) for h, t in LEGAL)
    return """<footer>
  <div class="container">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="brand" href="{here}index.html" aria-label="CYBERNEX Solutions"><span class="brand-icon">{logo}</span><span>CYBERNEX<small>S O L U T I O N S</small></span></a>
        <p>Proyecto empresarial académico de servicios tecnológicos: ciberseguridad, soporte técnico y protección de información.</p>
        <span class="lemaf">{lema}</span>
      </div>
      <div><h4>Navegar</h4><ul>{nav}</ul></div>
      <div><h4>Ecosistema</h4><ul>{divs}<li><a href="{here}connect.html">Experiencia NEX Connect</a></li></ul></div>
      <div><h4>Contacto</h4><ul>
        <li><a href="{here}contacto.html">Contacto y soporte</a></li>
        <li><a href="{here}contacto.html#ayuda">Centro de ayuda</a></li>
        <li><a href="{here}contacto.html#faq">Preguntas frecuentes</a></li>
        <li><span data-contact-pending class="muted small">Correo oficial: en preparación</span><a data-contact-mail data-show-address hidden href="#"></a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>© {year} CYBERNEX Solutions. Derechos reservados.</span>
      <nav aria-label="Legal">{legal}</nav>
    </div>
  </div>
</footer>
<button class="totop" id="toTop" type="button" aria-label="Volver arriba">{up}</button>
""".format(here=here, logo=logo("gF"), lema=C.LEMA, nav=nav, divs=divs, legal=legal, year=date.today().year, up=icon("up"))


PAGES = []  # (nombre, prioridad)


def write(name, title, desc, body, depth=0, current=None, ld=None, og_type="website",
          css=(), scripts=(), priority="0.6"):
    pre, here, head = pagehead(name, title, desc, depth, current or name, ld, og_type)
    extra_css = "".join('<link rel="stylesheet" href="%sassets/css/%s">\n' % (pre, f) for f in css)
    head = head.replace("{extra_css}", extra_css)
    js = '<script src="%sassets/js/site-config.js"></script>\n<script src="%sassets/js/site.js"></script>\n' % (pre, pre)
    js += "".join('<script src="%sassets/js/%s"></script>\n' % (pre, s) for s in scripts)
    page = head + "<body>\n" + header(here, pre, current or name) + '<main id="contenido">\n' + body + "\n</main>\n" + footer(here, pre) + js + "</body>\n</html>\n"
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    PAGES.append((name, priority))


def crumbs(items):
    out = []
    for i, (label, href) in enumerate(items):
        if href:
            out.append('<a href="%s">%s</a><span aria-hidden="true">/</span>' % (href, e(label)))
        else:
            out.append('<span aria-current="page">%s</span>' % e(label))
    return '<nav class="crumbs" aria-label="Ruta de navegación">%s</nav>' % "".join(out)


def pagehero(title, lead, crumb=None, extra=""):
    return '<section class="page-head"><div class="container">%s<h1>%s</h1><p class="lead">%s</p>%s</div></section>' % (
        crumb or "", title, e(lead), extra)


def state_html(d):
    return '<span class="state %s">%s</span>' % (d["kind"], e(d["status"]))


def cta_band(title=None, text=None, here=""):
    title = title or "¿Quieres conocer CYBERNEX con más detalle?"
    text = text or "Revisa cómo trabajamos o escríbenos. Los canales de contacto se publican en cuanto estén disponibles."
    return """<section class="section tight"><div class="container"><div class="cta-band">
  <div><h2>%s</h2><p>%s</p></div>
  <div class="cta-actions"><a class="btn primary" href="%ssobre.html">Conocer CYBERNEX</a><a class="btn" href="%scontacto.html">Contacto y soporte</a></div>
</div></div></section>""" % (e(title), e(text), here, here)


def post_row(a, featured=False, filt=True):
    attrs = ' data-item data-cat="%s"' % a["cat"] if filt else ""
    return """<article class="post%s"%s>
  <div class="post-meta"><span class="cat">%s</span><time datetime="%s">%s</time><span>Editorial CYBERNEX</span></div>
  <h3><a href="articulos/%s.html">%s</a></h3>
  <p>%s</p>
</article>""" % (" featured" if featured else "", attrs, e(CAT[a["cat"]]), C.ARTICLE_DATE, C.ARTICLE_DATE_LABEL,
               a["slug"], e(a["title"]), e(a["excerpt"]))


# ---------------------------------------------------------------- INICIO
def eco_diagram():
    r = 37.5
    nodes, lines = [], []
    for i, d in enumerate(C.DIVISIONS):
        ang = math.radians(-90 + i * 72)
        x, y = 50 + r * math.cos(ang), 50 + r * math.sin(ang)
        href = "security.html" if d["id"] == "security" else "divisiones.html#" + d["id"]
        nodes.append(
            '<a class="eco-node %s" style="--x:%.1f%%;--y:%.1f%%;--i:%d" href="%s" aria-label="%s: %s">'
            '<span class="eco-ico">%s</span><span class="eco-lab">%s<small>%s</small></span></a>'
            % (d["cls"], x, y, i, href, d["name"], e(d["status"]), icon(d["icon"]), d["name"], e(d["status"])))
        lines.append('<line x1="50" y1="50" x2="%.1f" y2="%.1f" pathLength="1" style="--i:%d"/>' % (x, y, i))
    return ('<div class="eco" role="group" aria-label="Las cinco divisiones del ecosistema CYBERNEX">'
            '<div class="eco-glow"></div><div class="eco-ring r1"></div><div class="eco-ring r2"></div><div class="eco-ring r3"></div>'
            '<svg class="eco-lines" viewBox="0 0 100 100" aria-hidden="true">%s</svg>'
            '<div class="eco-core">%s</div>%s</div>') % ("".join(lines), logo("gC"), "".join(nodes))


def page_index():
    cards = ""
    for d in C.DIVISIONS:
        href = "security.html" if d["id"] == "security" else "divisiones.html#" + d["id"]
        cards += """<a class="div-card %s%s" href="%s">
  <span class="ico">%s</span>
  %s
  <h3>%s</h3>
  <p>%s</p>
  <span class="more">%s</span>
</a>""" % (d["cls"], " big" if d["big"] else "", href, icon(d["icon"]), state_html(d), d["name"], e(d["summary"]),
           "Abrir herramientas" if d["id"] == "security" else "Conocer la división")
    today = """<div class="help-grid">
  <a class="help" href="security.html"><b>Herramientas de NEX Security</b><span>Password Lab, URL Check, lista de verificación y cuestionario. Funcionan en tu navegador, sin enviar datos.</span></a>
  <a class="help" href="conocimiento.html"><b>Artículos educativos</b><span>Guías breves sobre phishing, contraseñas, respaldos, privacidad y uso responsable de la IA.</span></a>
  <a class="help" href="../index.html"><b>Presentación corporativa</b><span>La presentación de 14 diapositivas con la que se expone el proyecto.</span></a>
</div>"""
    principles = "".join("<li><b>%s</b><span>%s</span></li>" % (e(a), e(b)) for a, b in C.PRINCIPLES)
    latest = "".join(post_row(a, filt=False) for a in C.ARTICLES[:3])
    body = """
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="lema">%(lema)s</span>
      <h1>Protegemos tu <span class="gradient-text">mundo digital.</span></h1>
      <p class="lead">CYBERNEX Solutions es un proyecto empresarial de servicios tecnológicos: ciberseguridad, soporte técnico y protección de información, organizado como un ecosistema de cinco divisiones.</p>
      <div class="hero-actions">
        <a class="btn primary" href="soluciones.html">Explorar soluciones</a>
        <a class="btn" href="sobre.html">Conocer CYBERNEX</a>
      </div>
      <p class="hero-foot"><b>Etapa inicial.</b> Hoy puedes usar las herramientas de NEX Security y leer los artículos. Lo demás está claramente marcado como en desarrollo.</p>
    </div>
    %(eco)s
  </div>
  <a class="cue" href="#ecosistema" aria-label="Ir al ecosistema">Ecosistema %(down)s</a>
</section>

<section class="section" id="ecosistema">
  <div class="container">
    <div class="section-head"><h2>Cinco divisiones, una misma prioridad</h2>
    <p>Cada división tiene su propio color y su propia forma, y todas comparten un mismo compromiso con la información de las personas. El estado de cada una se indica con claridad.</p></div>
    <div class="div-grid">%(cards)s</div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="section-head"><h2>Disponible hoy</h2><p>Lo que ya funciona en este sitio, sin registro y sin enviar tus datos.</p></div>
    %(today)s
  </div>
</section>

<section class="section">
  <div class="container ethics-band">
    <div>
      <h2>Tecnología con responsabilidad.</h2>
      <p class="statement-xl" style="margin-top:20px">Los servicios de seguridad se realizan con autorización, alcance definido y respeto por la información de cada cliente.</p>
      <p class="lead">No es un adorno: es la regla con la que decidimos qué hacemos y qué no.</p>
      <div class="hero-actions"><a class="btn primary" href="etica.html">Leer nuestros principios</a></div>
    </div>
    <ul class="principles">%(pr)s</ul>
  </div>
</section>

<section class="section tight">
  <div class="container">
    <div class="section-head"><h2>Centro de conocimiento</h2><p>Contenido editorial de CYBERNEX para entender y practicar la seguridad digital.</p></div>
    <div class="posts">%(latest)s</div>
    <p style="margin-top:26px"><a class="textlink" href="conocimiento.html">Ver todos los artículos</a></p>
  </div>
</section>
%(cta)s""" % dict(lema=C.LEMA, eco=eco_diagram(), down=icon("down"), cards=cards, today=today, pr=principles, latest=latest, cta=cta_band())
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": SITE, "url": BASE,
           "logo": BASE + "assets/img/favicon.svg", "slogan": C.LEMA,
           "description": "Proyecto empresarial académico de servicios tecnológicos: ciberseguridad, soporte técnico y protección de información."}]
    write("index.html", "CYBERNEX Solutions — " + C.LEMA,
          "CYBERNEX Solutions: ecosistema tecnológico con cinco divisiones — NEX Development, Security, Academy, Labs y Connect. Ciberseguridad, soporte y educación digital.",
          body, current="index.html", ld=ld, priority="1.0")


# ---------------------------------------------------------------- DIVISIONES
def page_divisiones():
    nav = "".join('<a class="%s" href="#%s">%s</a>' % (d["cls"], d["id"], d["name"]) for d in C.DIVISIONS)
    chapters = ""
    for d in C.DIVISIONS:
        items = "".join("<li>%s</li>" % e(i) for i in d["items"])
        links = "".join('<a class="btn small%s" href="%s">%s</a>' % (" primary" if i == 0 else "", h, e(t)) for i, (t, h) in enumerate(d["links"]))
        chapters += """<section class="chapter %s" id="%s">
  <div class="ch-mark">%s<span class="glyph">%s</span></div>
  <div>
    %s
    <h2>%s</h2>
    <p class="lead">%s</p>
    <ul class="ch-list">%s</ul>
    <p class="ch-note">%s</p>
    <div class="ch-links">%s</div>
  </div>
</section>""" % (d["cls"], d["id"], shape(d["id"]), icon(d["icon"]), state_html(d), d["name"], e(d["lead"]), items, e(d["note"]), links)
    body = pagehero("Las cinco divisiones de CYBERNEX",
                    "Un ecosistema organizado por áreas de trabajo. Algunas ya ofrecen herramientas; otras están en desarrollo y así se indican.",
                    crumbs([("Ecosistema", "index.html"), ("Divisiones", None)]),
                    '<div class="chapter-nav">%s</div>' % nav) + '<div class="container">%s</div>' % chapters + cta_band(here="")
    write("divisiones.html", "Divisiones del ecosistema",
          "NEX Development, NEX Security, NEX Academy, NEX Labs y NEX Connect: qué hace cada división de CYBERNEX y en qué estado se encuentra.",
          body, priority="0.8")


# ---------------------------------------------------------------- SOLUCIONES
def page_soluciones():
    chips = '<button class="chip-btn" type="button" data-value="all" aria-pressed="true">Todas</button>' + "".join(
        '<button class="chip-btn" type="button" data-value="%s" aria-pressed="false">%s</button>' % (d["id"], d["name"]) for d in C.DIVISIONS)
    groups = ""
    for label, gid in C.SERVICE_GROUPS:
        rows = ""
        for s in [x for x in C.SERVICES if x["group"] == gid]:
            d = DIV[s["division"]]
            rows += """<article class="svc %s" data-item data-division="%s">
  <div class="svc-head"><span class="tag">%s</span><h3>%s</h3><p class="svc-desc">%s</p></div>
  <dl class="svc-cols"><div><dt>Problema que resuelve</dt><dd>%s</dd></div><div><dt>Beneficio para el cliente</dt><dd>%s</dd></div></dl>
  <div class="svc-actions"><a class="btn small" href="divisiones.html#%s">Conocer más</a><a class="btn small" href="contacto.html">Contactar</a></div>
</article>""" % (d["cls"], d["id"], d["name"], e(s["name"]), e(s["desc"]), e(s["problem"]), e(s["benefit"]), d["id"])
        groups += '<div data-group><h2 class="group-title">%s</h2>%s</div>' % (e(label), rows)
    body = pagehero("Soluciones por categoría",
                    "Los servicios de CYBERNEX organizados por tipo de necesidad. Cada uno indica qué problema atiende y qué beneficio aporta.",
                    crumbs([("Ecosistema", "index.html"), ("Soluciones", None)])) + """
<section class="section tight"><div class="container" data-filter-root data-filter-key="division" data-noun="servicios" data-noun-one="servicio">
  <div class="filters" role="group" aria-label="Filtrar por división">%s</div>
  <p class="result-count" data-count aria-live="polite"></p>
  %s
  <div class="empty" data-empty hidden><b>Esta división todavía no ofrece servicios.</b>Está en desarrollo. Cuando existan, aparecerán aquí con su descripción.</div>
  <p class="notice info" style="margin-top:34px">%s</p>
</div></section>""" % (chips, groups, e(C.SERVICES_NOTE)) + cta_band("¿Tienes una necesidad concreta?", "Cuéntanos qué necesitas y te orientamos. Los canales de contacto se publican en cuanto estén disponibles.")
    write("soluciones.html", "Soluciones y servicios",
          "Servicios de CYBERNEX por categoría: seguridad informática, soporte técnico, protección de información y capacitación, con el problema que resuelve cada uno.",
          body, scripts=("filters.js",), priority="0.8")


# ---------------------------------------------------------------- PROYECTOS
def page_proyectos():
    legend = "".join('<div><b><span class="st st-%s"></span>%s</b>%s</div>' % (k, e(n), e(d)) for k, n, d in C.PROJECT_STATUS)
    chips = '<button class="chip-btn" type="button" data-value="all" aria-pressed="true">Todos</button>' + "".join(
        '<button class="chip-btn" type="button" data-value="%s" aria-pressed="false">%s</button>' % (k, e(n)) for k, n, d in C.PROJECT_STATUS)
    sn = {k: n for k, n, d in C.PROJECT_STATUS}
    cards = ""
    for p in C.PROJECTS:
        cards += """<article class="proj" data-item data-status="%s">
  <div class="proj-top"><span class="status"><span class="st st-%s"></span>%s</span><span class="muted small">%s</span></div>
  <h3>%s</h3><p>%s</p>
  <dl><div><dt>Objetivo</dt><dd>%s</dd></div><div><dt>Tecnología</dt><dd>%s</dd></div><div><dt>Estado</dt><dd>%s</dd></div></dl>
  <a class="btn small" href="%s">%s</a>
</article>""" % (p["status"], p["status"], e(sn[p["status"]]), e(p["kind"]), e(p["name"]), e(p["desc"]), e(p["goal"]), e(p["tech"]), e(p["state"]), p["href"], e(p["cta"]))
    body = pagehero("Proyectos",
                    "Aquí se publica el trabajo de CYBERNEX, separado según su madurez. Solo aparecen proyectos reales: no hay clientes, contratos ni resultados inventados.",
                    crumbs([("Ecosistema", "index.html"), ("Proyectos", None)])) + """
<section class="section tight"><div class="container" data-filter-root data-filter-key="status" data-noun="proyectos" data-noun-one="proyecto">
  <div class="legend">%s</div>
  <div class="filters" role="group" aria-label="Filtrar por estado">%s</div>
  <p class="result-count" data-count aria-live="polite"></p>
  <div class="proj-grid">%s
    <div class="proj-empty"><b>Espacio para trabajos futuros</b>Aquí se incorporarán desarrollo web, sistemas, interfaces, prototipos y experimentos de NEX Development y NEX Labs cuando existan. Cada uno se clasificará como realizado, demostración, prototipo o concepto.</div>
  </div>
  <div class="empty" data-empty hidden><b>Todavía no hay proyectos en esta categoría.</b>Cuando existan, se publicarán aquí con su estado real.</div>
</div></section>""" % (legend, chips, cards) + cta_band(here="")
    write("proyectos.html", "Proyectos y portafolio",
          "Proyectos de CYBERNEX clasificados como realizados, demostraciones, prototipos y conceptos. Sin clientes ni resultados inventados.",
          body, scripts=("filters.js",), priority="0.7")


# ---------------------------------------------------------------- CONOCIMIENTO
def page_conocimiento():
    chips = '<button class="chip-btn" type="button" data-value="all" aria-pressed="true">Todas</button>' + "".join(
        '<button class="chip-btn" type="button" data-value="%s" aria-pressed="false">%s</button>' % (k, e(n)) for k, n in C.CATEGORIES)
    posts = "".join(post_row(a, featured=(i == 0)) for i, a in enumerate(C.ARTICLES))
    body = pagehero("Centro de conocimiento",
                    "Artículos editoriales de CYBERNEX sobre ciberseguridad, privacidad y uso responsable de la tecnología. Pensados para leerse en pocos minutos.",
                    crumbs([("Ecosistema", "index.html"), ("Conocimiento", None)])) + """
<section class="section tight"><div class="container" data-filter-root data-filter-key="cat" data-noun="artículos" data-noun-one="artículo">
  <div class="filters" role="group" aria-label="Filtrar por categoría">%s
    <input class="search" type="search" data-search placeholder="Buscar un artículo" aria-label="Buscar un artículo"></div>
  <p class="result-count" data-count aria-live="polite"></p>
  <div class="posts">%s</div>
  <div class="empty" data-empty hidden><b>No hay artículos que coincidan.</b>Prueba con otra categoría o con una palabra distinta. Algunas categorías todavía no tienen contenido.</div>
  <p class="notice info" style="margin-top:34px">Los artículos son contenido editorial de CYBERNEX con fines educativos. No sustituyen la asesoría profesional. La fecha indicada es la de redacción de esta versión del sitio.</p>
</div></section>""" % (chips, posts) + cta_band("Practica lo que lees", "El cuestionario y los ejemplos de phishing de NEX Security convierten estos consejos en práctica.", here="")
    write("conocimiento.html", "Centro de conocimiento",
          "Artículos de CYBERNEX sobre ciberseguridad, privacidad digital, desarrollo web, inteligencia artificial y educación tecnológica.",
          body, scripts=("filters.js",), priority="0.8")


def render_block(b, pre=""):
    t = b[0]
    if t == "p":
        return "<p>%s</p>" % e(b[1])
    if t == "h2":
        return "<h2>%s</h2>" % e(b[1])
    if t == "ul":
        return "<ul>%s</ul>" % "".join("<li>%s</li>" % e(x) for x in b[1])
    if t == "ol":
        return "<ol>%s</ol>" % "".join("<li>%s</li>" % e(x) for x in b[1])
    if t == "callout":
        link = ""
        if len(b) > 2 and b[2]:
            link = '<br><a class="textlink" href="%s%s">%s</a>' % (pre, b[2][0], e(b[2][1]))
        return '<div class="callout">%s%s</div>' % (e(b[1]), link)
    raise ValueError(t)


def page_article(a):
    others = [x for x in C.ARTICLES if x["slug"] != a["slug"]]
    same = [x for x in others if x["cat"] == a["cat"]]
    more = (same + [x for x in others if x not in same])[:3]
    more_html = "".join(
        '<article class="post"><div class="post-meta"><span class="cat">%s</span></div><h3><a href="%s.html">%s</a></h3></article>'
        % (e(CAT[x["cat"]]), x["slug"], e(x["title"])) for x in more)
    body = """<div class="container">
<header class="article-head">%s
  <h1>%s</h1>
  <p class="lead">%s</p>
  <div class="byline"><span class="cat">%s</span><span>Editorial CYBERNEX</span><time datetime="%s">%s</time></div>
</header>
<article class="prose" style="padding:30px 0 20px">%s</article>
<aside class="more-posts" aria-label="Más artículos"><h2 style="font-size:1.3rem">Sigue leyendo</h2><div class="posts">%s</div>
<p style="margin-top:22px"><a class="textlink" href="../conocimiento.html">Volver al centro de conocimiento</a></p></aside>
</div>""" % (crumbs([("Ecosistema", "../index.html"), ("Conocimiento", "../conocimiento.html"), (a["title"], None)]),
             e(a["title"]), e(a["excerpt"]), e(CAT[a["cat"]]), C.ARTICLE_DATE, C.ARTICLE_DATE_LABEL,
             "".join(render_block(b, "../") for b in a["body"]), more_html)
    url = BASE + "ecosistema/articulos/%s.html" % a["slug"]
    org = {"@type": "Organization", "name": SITE, "url": BASE}
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["excerpt"],
           "datePublished": C.ARTICLE_DATE, "inLanguage": "es", "author": org, "publisher": org, "mainEntityOfPage": url,
           "image": OG_IMAGE}]
    write("articulos/%s.html" % a["slug"], a["title"], a["excerpt"], body, depth=1, current="conocimiento.html",
          ld=ld, og_type="article", priority="0.6")


# ---------------------------------------------------------------- ÉTICA
def page_etica():
    pr = "".join("<li><b>%s</b><span>%s</span></li>" % (e(a), e(b)) for a, b in C.PRINCIPLES)
    rules = "".join("<li>%s</li>" % e(r) for r in C.RULES)
    body = """<section class="page-head"><div class="container">%s
  <h1>Tecnología con responsabilidad.</h1>
  <p class="statement-xl" style="margin-top:22px">Primero decidimos qué no haremos. Después construimos todo lo demás.</p>
  <p class="lead">En CYBERNEX la ética no es un anexo: define cómo aceptamos un trabajo, cómo tratamos la información y cómo explicamos lo que hacemos.</p>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><h2>Nuestro compromiso</h2></div>
  <div class="card" style="max-width:820px;padding:34px"><p class="statement-xl" style="font-size:1.45rem;max-width:none">Los servicios de seguridad de CYBERNEX se realizan únicamente con autorización expresa, con un alcance definido por escrito y con respeto a la información de cada cliente. Si falta alguna de esas tres condiciones, no intervenimos.</p></div>
</div></section>
<section class="section band"><div class="container">
  <div class="section-head"><h2>Diez principios</h2><p>Cada principio responde a una decisión concreta del trabajo diario.</p></div>
  <ul class="principles">%s</ul>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><h2>Reglas internas</h2><p>Cómo se traducen los principios en la práctica del equipo.</p></div>
  <ol class="rules">%s</ol>
</div></section>
<section class="section tight"><div class="container"><div class="notice info"><b>Límites honestos.</b> CYBERNEX es una marca nueva y un proyecto académico en etapa inicial. Estos principios describen cómo queremos trabajar; no constituyen una certificación ni una auditoría externa.</div></div></section>
%s""" % (crumbs([("Ecosistema", "index.html"), ("Ética", None)]), pr, rules, cta_band(here=""))
    write("etica.html", "Tecnología con responsabilidad",
          "Principios éticos de CYBERNEX: privacidad, confidencialidad, consentimiento, legalidad y uso responsable de la tecnología.",
          body, priority="0.7")


# ---------------------------------------------------------------- RESPONSABILIDAD
def page_responsabilidad():
    cards = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in C.RESPONSIBILITY)
    body = pagehero("Responsabilidad social y ambiental",
                    "Qué hacemos, a escala de un proyecto académico, para que la tecnología sea más segura, más accesible y menos desperdiciada.",
                    crumbs([("Ecosistema", "index.html"), ("Responsabilidad", None)])) + """
<section class="section tight"><div class="container"><div class="rsc">%s</div>
<p class="notice info" style="margin-top:30px">Son compromisos de práctica y de diseño de este sitio, no resultados medidos. No publicamos cifras de impacto porque todavía no existen.</p></div></section>%s""" % (cards, cta_band(here=""))
    write("responsabilidad.html", "Responsabilidad social y ambiental",
          "Educación digital, accesibilidad, eficiencia tecnológica y reducción del desperdicio electrónico en CYBERNEX.",
          body, priority="0.5")


# ---------------------------------------------------------------- SOBRE
def page_sobre():
    values = "".join('<div class="value"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in C.VALUES)
    org = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in C.ORG)
    steps = "".join("<li class='tl'><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in C.PROCESS)
    team = "".join("<li>%s</li>" % e(n) for n in C.TEAM)
    body = pagehero("Sobre CYBERNEX",
                    "Un proyecto empresarial académico que quiere crecer como una empresa tecnológica seria, cuidadosa con la información de las personas.",
                    crumbs([("Ecosistema", "index.html"), ("Sobre CYBERNEX", None)])) + """
<section class="section tight"><div class="container"><div class="grid g2">
  <div class="card"><h3>Quiénes somos</h3><p style="margin-top:10px">%s</p><p style="margin-top:10px">CYBERNEX nace como proyecto empresarial de Administración y Finanzas: además de la parte tecnológica, trabaja la organización, la planeación y la operación de una empresa. Es una iniciativa en crecimiento; no le atribuimos trayectoria, tamaño ni experiencia que no se hayan acreditado.</p></div>
  <div class="card"><h3>Qué hacemos</h3><p style="margin-top:10px">Ofrecemos servicios de ciberseguridad, soporte técnico y protección de información, y desarrollamos herramientas y contenido de educación digital. El ecosistema se organiza en cinco divisiones, de las cuales NEX Security es la que hoy tiene herramientas funcionando.</p><p style="margin-top:12px"><a class="textlink" href="divisiones.html">Ver las divisiones</a></p></div>
</div></div></section>
<section class="section band"><div class="container">
  <div class="mv"><div class="card"><h3>Nuestra misión</h3><p>%s</p></div><div class="card"><h3>Nuestra visión</h3><p>%s</p></div></div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><h2>Nuestros valores</h2></div><div class="values">%s</div>
</div></section>
<section class="section band"><div class="container">
  <div class="section-head"><h2>Filosofía de trabajo</h2><p>Primero entender, después acordar, luego actuar con autorización y explicar lo hecho. Esta es la secuencia con la que atendemos cualquier servicio.</p></div>
  <ol class="timeline steps-6">%s</ol>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><h2>Cómo se organiza el equipo</h2></div><div class="org">%s</div>
  <div class="card" style="margin-top:22px"><h3>Integrantes del proyecto</h3><ul style="margin-top:10px">%s</ul></div>
</div></section>%s""" % (e(C.FAQ[0][1]), e(C.MISSION), e(C.VISION), values, steps, org, team, cta_band(here=""))
    write("sobre.html", "Sobre CYBERNEX",
          "Quiénes somos, misión, visión, valores y filosofía de trabajo de CYBERNEX Solutions, proyecto empresarial académico de Administración y Finanzas.",
          body, priority="0.7")


# ---------------------------------------------------------------- CONNECT
def page_connect():
    d = DIV["connect"]
    steps = [
        ("Contacto inicial", "La persona o la organización se comunica con CYBERNEX por un canal oficial."),
        ("Recepción de solicitud", "Se registra la necesidad y se confirma qué se entendió."),
        ("Comunicación con CYBERNEX", "Se aclaran dudas, alcance y condiciones antes de comenzar."),
        ("Desarrollo o atención del servicio", "Se realiza el trabajo con autorización y con avances informados."),
        ("Seguimiento y soporte", "Se entregan resultados y se acompaña con soporte posterior."),
    ]
    tl = "".join("<li class='tl'><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in steps)
    body = """<div class="%s">%s
<section class="section tight"><div class="container"><div class="chapter" style="border-top:0;padding-top:0;grid-template-columns:minmax(160px,.5fr) 1.6fr">
  <div class="ch-mark">%s<span class="glyph">%s</span></div>
  <div>%s<p class="notice" style="margin-top:18px"><b>No existe un portal.</b> NEX Connect es un concepto. No hay cuentas de usuario ni inicio de sesión, y este sitio no guarda información personal en tu navegador. Esta página solo explica cómo funcionará la experiencia.</p></div>
</div></div></section>
<section class="section band"><div class="container">
  <div class="section-head"><h2>Cómo funcionará la experiencia</h2><p>Cinco pasos, de la primera conversación al soporte posterior.</p></div>
  <ol class="timeline">%s</ol>
</div></section>
<section class="section"><div class="container"><div class="grid g2">
  <div class="card"><h3>Qué ofrecerá</h3><ul>%s</ul></div>
  <div class="card"><h3>Preparado para crecer</h3><p>La arquitectura está pensada para incorporar autenticación y una base de datos en otra etapa. En la carpeta <code>backend/</code> hay un esquema de ejemplo y las variables de entorno documentadas; no está conectado a este sitio.</p><p style="margin-top:10px">Cuando se conecte, las claves privadas vivirán en el servidor, nunca en el código público.</p></div>
</div></div></section></div>%s""" % (
        d["cls"],
        pagehero("Experiencia NEX Connect", d["lead"] + " Una visión de cómo será la relación con cada cliente.",
                 crumbs([("Ecosistema", "index.html"), ("NEX Connect", None)]), state_html(d)),
        shape("connect"), icon("connect"), state_html(d), tl,
        "".join("<li>%s</li>" % e(i) for i in d["items"]), cta_band(here=""))
    write("connect.html", "NEX Connect: experiencia de cliente",
          "NEX Connect es el concepto de CYBERNEX para dar seguimiento a solicitudes y mantener la comunicación con clientes. Aún no existe como portal.",
          body, current="divisiones.html", priority="0.6")


# ---------------------------------------------------------------- CONTACTO
def page_contacto():
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in C.FAQ)
    body = pagehero("Contacto y soporte",
                    "Información clara sobre cómo comunicarte con CYBERNEX y dónde resolver dudas mientras los canales oficiales se terminan de preparar.",
                    crumbs([("Ecosistema", "index.html"), ("Contacto", None)])) + """
<section class="section tight"><div class="container"><div class="grid g2">
  <div class="contact-box">
    <h2 style="font-size:1.5rem">Escríbenos</h2>
    <div data-contact-pending><p class="muted" style="margin-top:12px">El canal oficial de contacto de CYBERNEX todavía está en preparación, por eso no publicamos teléfonos, direcciones, correos ni redes sociales. No hay formulario: no queremos aparentar un envío que no llegaría a nadie.</p>
    <p class="muted" style="margin-top:12px">Si formas parte de la clase o del equipo evaluador, el contacto es a través de los integrantes del proyecto.</p></div>
    <a class="btn primary mailbtn" data-contact-mail data-subject="Consulta desde el sitio de CYBERNEX" hidden href="#">Escribir un correo</a>
  </div>
  <div class="card"><h3>Qué conviene incluir cuando escribas</h3><ul style="margin-top:10px"><li>Qué necesitas o qué problema tienes.</li><li>Qué equipo, cuenta o sistema está involucrado.</li><li>Desde cuándo ocurre y qué intentaste.</li><li>No envíes contraseñas, códigos de verificación ni datos bancarios.</li></ul></div>
</div></div></section>
<section class="section band" id="ayuda"><div class="container">
  <div class="section-head"><h2>Centro de ayuda</h2><p>Recursos que puedes usar ahora mismo, sin contactar a nadie.</p></div>
  <div class="help-grid">
    <a class="help" href="security.html#password"><b>Revisar una contraseña</b><span>Password Lab: evalúa fortaleza y genera una nueva.</span></a>
    <a class="help" href="security.html#url"><b>Revisar un enlace sospechoso</b><span>URL Check analiza cómo está escrita la dirección, sin abrirla.</span></a>
    <a class="help" href="security.html#checklist"><b>Mejorar tus hábitos</b><span>Lista de 24 buenas prácticas con avance guardado en tu navegador.</span></a>
    <a class="help" href="articulos/reconocer-correo-phishing.html"><b>Recibí un correo extraño</b><span>Señales de phishing y qué hacer si ya hiciste clic.</span></a>
    <a class="help" href="articulos/verificacion-en-dos-pasos.html"><b>Proteger mis cuentas</b><span>Cómo activar la verificación en dos pasos.</span></a>
    <a class="help" href="articulos/respaldos-regla-3-2-1.html"><b>Respaldar mi información</b><span>La regla 3-2-1 explicada con calma.</span></a>
  </div>
</div></section>
<section class="section" id="faq"><div class="container">
  <div class="section-head"><h2>Preguntas frecuentes</h2></div>
  <div class="faq">%s</div>
</div></section>""" % faq
    write("contacto.html", "Contacto y soporte",
          "Cómo comunicarte con CYBERNEX, centro de ayuda y preguntas frecuentes. Los canales oficiales están en preparación.",
          body, priority="0.7")


# ---------------------------------------------------------------- LEGALES
def legal_page(name, title, desc, sections):
    parts = "".join("<h2>%s</h2>%s" % (e(t), "".join("<p>%s</p>" % e(p) for p in ps)) for t, ps in sections)
    body = pagehero(title, desc, crumbs([("Ecosistema", "index.html"), (title, None)])) + """
<section class="section tight"><div class="container"><div class="notice" style="margin-bottom:30px;max-width:760px">%s</div>
<div class="legal prose">%s<p class="muted small" style="margin-top:30px">Versión de noviembre de 2026.</p></div></div></section>""" % (e(C.LEGAL_NOTICE), parts)
    write(name, title, desc, body, current=name, priority="0.3")


# ---------------------------------------------------------------- SECURITY
def page_security():
    with open(os.path.join(HERE, "partials", "security_tools.html"), encoding="utf-8") as f:
        tools = f.read()
    d = DIV["security"]
    body = """<div class="%s">""" % d["cls"] + pagehero(
        "Herramientas de NEX Security",
        "Evalúa contraseñas, revisa enlaces sospechosos, comprueba tus buenas prácticas y aprende a reconocer el phishing. Todo se procesa en tu navegador: no enviamos tus datos a ningún servidor.",
        crumbs([("Ecosistema", "index.html"), ("NEX Security", None)]), state_html(d)) + '<section class="section tight"><div class="container">' + tools + "</div></section></div>"
    write("security.html", "NEX Security: herramientas de ciberseguridad",
          "Password Lab, URL Check, lista de verificación y cuestionario de concientización de NEX Security. Todo se procesa en tu navegador.",
          body, current="divisiones.html", css=("security.css",),
          scripts=("password.js", "urlcheck.js", "checklist.js", "awareness.js", "security-ui.js"), priority="0.9")


# ---------------------------------------------------------------- SITEMAP / ROBOTS
def write_sitemap():
    today = date.today().isoformat()
    urls = [(BASE, "1.0")] + [(BASE + "ecosistema/" + n, p) for n, p in PAGES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, p in urls:
        xml += "  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n" % (u, today, p)
    xml += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % BASE)


def main():
    page_index()
    page_divisiones()
    page_soluciones()
    page_proyectos()
    page_conocimiento()
    for a in C.ARTICLES:
        page_article(a)
    page_etica()
    page_responsabilidad()
    page_sobre()
    page_connect()
    page_contacto()
    legal_page("privacidad.html", "Aviso de privacidad", "Plantilla informativa sobre el tratamiento de datos en este sitio.", C.PRIVACY)
    legal_page("terminos.html", "Términos y condiciones", "Plantilla informativa sobre el uso de este sitio.", C.TERMS)
    page_security()
    write_sitemap()
    print("Generadas %d páginas." % len(PAGES))


if __name__ == "__main__":
    main()
