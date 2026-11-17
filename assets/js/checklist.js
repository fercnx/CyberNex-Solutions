/* CYBERNEX 10.0V — Security Checklist
   Autoevaluación orientativa de buenas prácticas. El avance se guarda solo en
   este navegador (localStorage); no se envía a ningún servidor. */
(function(root){
'use strict';
var NS=root.CYBERNEX=root.CYBERNEX||{};
var KEY='cybernex.checklist.v1';

var GROUPS=[
  {id:'cuentas',title:'Seguridad de cuentas',items:[
    ['mfa','Activar la verificación en dos pasos','En correo, redes sociales, banca y servicios importantes.'],
    ['unicas','Usar una contraseña distinta en cada cuenta','Así una filtración no compromete las demás.'],
    ['gestor','Guardar las contraseñas en un gestor','Evita notas, hojas de cálculo o el navegador compartido.'],
    ['larga','Usar contraseñas largas (14 caracteres o más)','Una frase larga y única es más fuerte que una corta con símbolos.'],
    ['recuperacion','Mantener actualizados el correo y teléfono de recuperación','Te permiten recuperar la cuenta si pierdes el acceso.'],
    ['actividad','Revisar de vez en cuando los accesos recientes','Cierra sesiones que no reconozcas.']
  ]},
  {id:'dispositivos',title:'Protección de dispositivos',items:[
    ['updates','Mantener el sistema y las aplicaciones actualizados','Activa las actualizaciones automáticas.'],
    ['antimalware','Tener una solución antimalware activa','Por ejemplo, la que incluye tu sistema operativo.'],
    ['bloqueo','Bloquear la pantalla con PIN, contraseña o biometría',''],
    ['cifrado','Cifrar el almacenamiento del equipo','Protege tus datos si el dispositivo se pierde o es robado.'],
    ['respaldos','Hacer respaldos periódicos (regla 3-2-1)','3 copias, en 2 tipos de medio, 1 fuera de tu casa u oficina.'],
    ['software','Instalar solo software de fuentes oficiales','Evita programas pirata o de origen desconocido.']
  ]},
  {id:'navegacion',title:'Navegación segura',items:[
    ['https','Comprobar la dirección y el candado antes de iniciar sesión','El candado indica conexión cifrada, no que el sitio sea legítimo.'],
    ['adjuntos','No abrir adjuntos ni enlaces inesperados','Confirma por otro medio con quien te los envía.'],
    ['urgencia','Desconfiar de mensajes con urgencia o premios','Son señales típicas de phishing.'],
    ['wifi','Evitar operaciones sensibles en redes Wi-Fi públicas','Usa datos móviles o una VPN de confianza.'],
    ['oficial','Entrar a bancos y servicios escribiendo la dirección oficial','No desde enlaces recibidos en mensajes.'],
    ['extensiones','Revisar las extensiones del navegador','Elimina las que no uses o no conozcas.']
  ]},
  {id:'empresas',title:'Recomendaciones para empresas',items:[
    ['politica','Definir una política de contraseñas y doble verificación',''],
    ['privilegios','Dar a cada persona solo los accesos que necesita','Principio de mínimo privilegio.'],
    ['respaldoprob','Probar periódicamente la restauración de respaldos','Un respaldo que no se ha probado puede no servir.'],
    ['capacitacion','Capacitar al personal en seguridad de forma periódica',''],
    ['inventario','Mantener un inventario de equipos y cuentas',''],
    ['incidentes','Tener definido cómo reportar y responder a incidentes','Quién avisa a quién y qué se hace primero.']
  ]}
];

function load(){try{var v=JSON.parse(localStorage.getItem(KEY)||'{}');return v&&typeof v==='object'?v:{}}catch(e){return{}}}
function save(s){try{localStorage.setItem(KEY,JSON.stringify(s))}catch(e){}}
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e}

function render(rootEl){
  var state=load(),groupBars={},groupCounts={};
  var total=GROUPS.reduce(function(n,g){return n+g.items.length},0);
  var wrap=el('div'),top=el('div','cl-total'),totalTxt=el('b'),totalBar=el('div','cl-bar'),totalFill=el('i'),reset=el('button','btn small','Reiniciar lista');
  totalBar.style.flex='1';totalBar.style.minWidth='160px';totalBar.style.margin='0';totalBar.appendChild(totalFill);
  reset.type='button';
  top.appendChild(totalTxt);top.appendChild(totalBar);top.appendChild(reset);wrap.appendChild(top);

  function update(){
    var done=0;
    GROUPS.forEach(function(g){
      var d=g.items.filter(function(it){return state[g.id+'.'+it[0]]}).length;done+=d;
      groupCounts[g.id].textContent=d+' de '+g.items.length;
      groupBars[g.id].style.width=(d/g.items.length*100)+'%';
    });
    totalTxt.textContent=done+' de '+total+' prácticas aplicadas';
    totalFill.style.width=(done/total*100)+'%';
    totalBar.setAttribute('role','progressbar');totalBar.setAttribute('aria-valuemin','0');totalBar.setAttribute('aria-valuemax','100');totalBar.setAttribute('aria-valuenow',String(Math.round(done/total*100)));totalBar.setAttribute('aria-label','Avance total de la lista');
  }

  GROUPS.forEach(function(g){
    var box=el('div','cl-group'),head=el('div','cl-head'),h=el('h3',null,g.title),cnt=el('span','muted small'),bar=el('div','cl-bar'),fill=el('i');
    groupCounts[g.id]=cnt;groupBars[g.id]=fill;bar.appendChild(fill);
    head.appendChild(h);head.appendChild(cnt);box.appendChild(head);box.appendChild(bar);
    g.items.forEach(function(it){
      var id=g.id+'.'+it[0],lab=el('label','cl-item'),cb=document.createElement('input'),txt=el('span');
      cb.type='checkbox';cb.checked=!!state[id];cb.setAttribute('data-id',id);
      txt.appendChild(document.createTextNode(it[1]));
      if(it[2])txt.appendChild(el('small',null,it[2]));
      cb.addEventListener('change',function(){if(cb.checked)state[id]=1;else delete state[id];save(state);update()});
      lab.appendChild(cb);lab.appendChild(txt);box.appendChild(lab);
    });
    wrap.appendChild(box);
  });
  reset.addEventListener('click',function(){
    state={};save(state);
    [].forEach.call(wrap.querySelectorAll('input[type=checkbox]'),function(c){c.checked=false});
    update();
  });
  wrap.appendChild(el('p','muted small','Esta lista es una autoevaluación orientativa. No sustituye una auditoría de seguridad profesional.'));
  rootEl.textContent='';rootEl.appendChild(wrap);update();
}

NS.checklist={render:render,GROUPS:GROUPS,KEY:KEY};
})(typeof window!=='undefined'?window:globalThis);
