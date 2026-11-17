/* CYBERNEX 10.0V — comportamiento común de las páginas del ecosistema
   (menú móvil, año del pie de página y aparición al desplazarse). */
(function(){
'use strict';
var menu=document.getElementById('menuBtn'),nav=document.getElementById('navLinks');
if(menu&&nav){
  menu.addEventListener('click',function(){
    var open=nav.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(open));
    menu.textContent=open?'×':'☰';
    menu.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');
  });
}
var y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();
var items=document.querySelectorAll('.reveal');
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}})},{threshold:.1});
  [].forEach.call(items,function(el){io.observe(el)});
}else{[].forEach.call(items,function(el){el.classList.add('visible')})}
})();
