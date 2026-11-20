/* CYBERNEX 10.0V — comportamiento común: menú móvil, encabezado con scroll,
   botón de volver arriba y canal de contacto configurable. Sin dependencias. */
(function () {
  'use strict';
  var header = document.querySelector('.header');
  var menu = document.getElementById('menuBtn');
  var nav = document.getElementById('navLinks');
  var totop = document.getElementById('toTop');

  function setMenu(open) {
    if (!menu || !nav) return;
    nav.classList.toggle('open', open);
    menu.setAttribute('aria-expanded', String(open));
    menu.textContent = open ? '×' : '☰';
    menu.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }
  if (menu && nav) {
    menu.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { setMenu(false); menu.focus(); }
    });
  }

  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    if (header) header.classList.toggle('scrolled', y > 12);
    if (totop) totop.classList.toggle('show', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (totop) totop.addEventListener('click', function () {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    try { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } catch (e) { window.scrollTo(0, 0); }
  });

  /* Canal de contacto: solo se muestra si hay un correo válido en site-config.js */
  var cfg = window.CYBERNEX_CONFIG || {};
  var mail = typeof cfg.contactEmail === 'string' ? cfg.contactEmail.trim() : '';
  var ok = /^[^\s@<>"']+@[^\s@<>"']+\.[^\s@<>"']+$/.test(mail);
  [].forEach.call(document.querySelectorAll('[data-contact-mail]'), function (a) {
    if (ok) {
      a.setAttribute('href', 'mailto:' + mail + (a.getAttribute('data-subject') ? '?subject=' + encodeURIComponent(a.getAttribute('data-subject')) : ''));
      if (a.hasAttribute('data-show-address')) a.textContent = mail;
      a.hidden = false;
    } else { a.hidden = true; }
  });
  [].forEach.call(document.querySelectorAll('[data-contact-pending]'), function (el) { el.hidden = ok; });
})();
