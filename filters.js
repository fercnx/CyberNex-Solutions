/* CYBERNEX 10.0V — filtros y búsqueda de listas (soluciones, proyectos, conocimiento).
   Marcado: [data-filter-root data-filter-key="cat"] con botones [data-value],
   elementos [data-item data-cat="..."], [data-group], [data-count], [data-empty], [data-search]. */
(function () {
  'use strict';
  var root = document.querySelector('[data-filter-root]');
  if (!root) return;
  var key = root.getAttribute('data-filter-key');
  var items = [].slice.call(root.querySelectorAll('[data-item]'));
  var groups = [].slice.call(root.querySelectorAll('[data-group]'));
  var chips = [].slice.call(root.querySelectorAll('.chip-btn[data-value]'));
  var search = root.querySelector('[data-search]');
  var count = root.querySelector('[data-count]');
  var empty = root.querySelector('[data-empty]');
  var noun = root.getAttribute('data-noun') || 'resultados';
  var values = chips.map(function (c) { return c.getAttribute('data-value'); });
  var state = { v: 'all', q: '' };

  function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }

  function apply() {
    var shown = 0;
    items.forEach(function (it) {
      var okV = state.v === 'all' || it.getAttribute('data-' + key) === state.v;
      var okQ = !state.q || norm(it.textContent).indexOf(state.q) > -1;
      var vis = okV && okQ;
      it.hidden = !vis;
      if (vis) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('[data-item]:not([hidden])'); });
    chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-value') === state.v)); });
    if (count) count.textContent = shown + ' ' + (shown === 1 ? (root.getAttribute('data-noun-one') || 'resultado') : noun);
    if (empty) empty.hidden = shown !== 0;
  }

  function setHash() {
    try {
      var h = state.v === 'all' ? location.pathname + location.search : '#' + key + '=' + state.v;
      history.replaceState(null, '', h);
    } catch (e) { /* file:// u otros entornos: no es esencial */ }
  }

  function fromHash() {
    var m = (location.hash || '').match(new RegExp('[#&]' + key + '=([a-z0-9-]+)'));
    if (m && values.indexOf(m[1]) > -1) state.v = m[1];
  }

  chips.forEach(function (c) {
    c.addEventListener('click', function () { state.v = c.getAttribute('data-value'); apply(); setHash(); });
  });
  if (search) search.addEventListener('input', function () { state.q = norm(search.value.trim()); apply(); });
  window.addEventListener('hashchange', function () { state.v = 'all'; fromHash(); apply(); });
  fromHash();
  apply();
})();
