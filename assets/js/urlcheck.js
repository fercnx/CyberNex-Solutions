/* CYBERNEX 10.0V — URL Check (lógica)
   Análisis local de indicadores en la propia dirección. NO visita el enlace,
   NO consulta servicios externos y NO puede confirmar que un sitio sea seguro. */
(function(root){
'use strict';
var NS=root.CYBERNEX=root.CYBERNEX||{};

var SHORTENERS=['bit.ly','tinyurl.com','t.co','goo.gl','ow.ly','is.gd','cutt.ly','rebrand.ly','shorturl.at','tiny.cc','buff.ly','rb.gy','t.ly'];
var RISKY_TLDS=['zip','mov','xyz','top','click','work','support','country','gq','tk','ml','cf','ga','icu','buzz','rest','cfd','sbs','monster','cyou'];
var BRANDS=['paypal','google','microsoft','apple','amazon','facebook','instagram','whatsapp','bbva','banorte','santander','hsbc','mercadolibre','mercadopago','netflix','outlook','telcel','citibanamex','banamex'];
var WORDS=['login','signin','verify','verifica','verificar','secure','seguro','segura','update','actualiza','actualizar','account','cuenta','password','contraseña','contrasena','banco','bank','wallet','confirm','confirma','pago','premio','gratis','factura','suspendida','bloqueada'];
var SLD=['com','co','org','net','gob','gov','edu','ac'];

function regDomain(host){
  var p=host.split('.');
  if(p.length<=2)return host;
  var last=p[p.length-1],second=p[p.length-2];
  if(last.length===2&&SLD.indexOf(second)!==-1&&p.length>=3)return p.slice(-3).join('.');
  return p.slice(-2).join('.');
}

function analyze(input){
  var raw=String(input==null?'':input).trim();
  if(!raw)return{valid:false,error:'Escribe o pega un enlace para analizarlo.'};
  if(raw.length>2048)return{valid:false,error:'El enlace es demasiado largo (más de 2048 caracteres).'};
  if(/\s/.test(raw))return{valid:false,error:'El enlace contiene espacios; un enlace válido no los tiene.'};
  var noScheme=!/^[a-z][a-z0-9+.\-]*:/i.test(raw)||/^[^\/?#]*:\d+([\/?#]|$)/.test(raw);
  var u;
  try{u=new URL(noScheme?'https://'+raw:raw)}catch(e){return{valid:false,error:'No tiene un formato de dirección válido.'}}

  var findings=[],proto=u.protocol.replace(':','').toLowerCase();
  var host=u.hostname.toLowerCase().replace(/\.$/,'');
  var https='unknown';
  function add(sev,title,detail){findings.push({sev:sev,title:title,detail:detail})}

  if(noScheme){add('info','No indicaste el protocolo','Se analizó la dirección suponiendo https://, pero no sabemos si el enlace original lo usa.')}
  else if(proto==='https'){https='yes';add('ok','Usa HTTPS','La conexión viaja cifrada. Esto no garantiza que el sitio sea legítimo: los sitios fraudulentos también pueden usar HTTPS.')}
  else if(proto==='http'){https='no';add('medio','No usa HTTPS','La conexión no está cifrada: lo que escribas podría ser interceptado. Evita introducir datos personales.')}
  else if(proto==='javascript'||proto==='data'||proto==='vbscript'){add('alto','Esquema peligroso («'+proto+':»)','No es una página web: ejecuta o incrusta código. No lo abras.')}
  else{add('medio','Esquema poco habitual («'+proto+':»)','Los enlaces comunes usan http o https. Confirma el origen antes de abrirlo.')}

  var isWeb=proto==='http'||proto==='https';
  if(isWeb||noScheme){
    if(u.username||u.password)add('alto','Contiene usuario o «@» antes del dominio','Es una técnica para disfrazar el destino real: lo que importa es lo que aparece después del «@».');
    if(/^\d{1,3}(\.\d{1,3}){3}$/.test(host)||host.charAt(0)==='[')add('alto','Usa una dirección IP en lugar de un nombre','Los servicios legítimos casi siempre usan un nombre de dominio.');
    else if(host.indexOf('.')===-1)add('bajo','Dominio sin extensión','Un nombre sin «.com», «.mx», etc. suele ser un equipo interno o un error de escritura.');
    if(host.indexOf('xn--')!==-1)add('medio','Dominio con codificación internacional (punycode)','Puede usarse para imitar letras de otros alfabetos (homógrafos). Revisa que sea el sitio que esperas.');
    var labels=host.split('.');
    if(labels.length>4)add('medio','Demasiados subdominios','Se usan para esconder el dominio real al final: '+regDomain(host)+'.');
    if(SHORTENERS.indexOf(host)!==-1)add('medio','Acortador de enlaces','Oculta el destino final. Si puedes, pide el enlace completo o ábrelo con precaución.');
    var tld=labels[labels.length-1];
    if(RISKY_TLDS.indexOf(tld)!==-1)add('bajo','Extensión «.'+tld+'» usada con frecuencia en campañas fraudulentas','Existen sitios legítimos con esta extensión; es solo un indicador.');
    if(u.port&&u.port!==''&&((proto==='https'&&u.port!=='443')||(proto==='http'&&u.port!=='80')))add('medio','Puerto no estándar ('+u.port+')','Los sitios públicos normalmente no lo necesitan.');
    if((host.match(/-/g)||[]).length>=3)add('bajo','Muchos guiones en el dominio','Es común en dominios creados para imitar a otros.');

    var reg=regDomain(host),regName=reg.split('.')[0],hit=null;
    BRANDS.forEach(function(b){
      if(hit)return;
      var others=labels.slice(0,-(reg.split('.').length));
      var tokens=[];others.concat([regName]).forEach(function(l){l.split('-').forEach(function(t){tokens.push(t)})});
      var found=tokens.some(function(t){return t===b||(b.length>=6&&t.indexOf(b)===0)});
      if(found&&regName!==b)hit=b;
    });
    if(hit)add('alto','Menciona «'+hit+'» pero el dominio real es «'+reg+'»','Posible suplantación: el nombre de una marca aparece en la dirección, pero el sitio pertenece a otro dominio.');

    var text=(host+' '+decodeSafe(u.pathname)).toLowerCase(),words=[];
    WORDS.forEach(function(w){if(text.indexOf(w)!==-1&&words.indexOf(w)===-1)words.push(w)});
    if(words.length)add('bajo','Palabras sensibles en la dirección: '+words.slice(0,4).join(', '),'Aparecen mucho en mensajes de phishing, pero también en páginas legítimas. No es una prueba de fraude.');
    if((raw.match(/%[0-9a-f]{2}/gi)||[]).length>5)add('bajo','Muchos caracteres codificados (%xx)','A veces se usan para ocultar el contenido real de la dirección.');
    if(raw.length>100)add('bajo','Enlace muy largo','Las direcciones muy largas pueden esconder el destino o parámetros de rastreo.');
  }

  var score=0;findings.forEach(function(f){score+=f.sev==='alto'?3:f.sev==='medio'?2:f.sev==='bajo'?1:0});
  var hasAlto=findings.some(function(f){return f.sev==='alto'});
  var verdict;
  if(hasAlto||score>=4)verdict={level:'alto',label:'Varios indicadores de riesgo',text:'No abras este enlace ni escribas datos en él sin confirmarlo por otro medio.'};
  else if(score>=1)verdict={level:'precaucion',label:'Precaución: hay indicadores a revisar',text:'Revisa los puntos marcados antes de continuar.'};
  else verdict={level:'sin',label:'No se detectaron indicadores evidentes',text:'Esto NO significa que el enlace sea seguro: este análisis solo revisa cómo está escrita la dirección.'};

  return{
    valid:true,score:score,verdict:verdict,findings:findings,https:https,
    parts:{protocolo:noScheme?'(no indicado)':proto,dominio:host,dominioPrincipal:regDomain(host),puerto:u.port||'(predeterminado)',ruta:(u.pathname||'/')+(u.search?u.search:'')}
  };
}
function decodeSafe(s){try{return decodeURIComponent(s)}catch(e){return s}}

NS.urlcheck={analyze:analyze};
})(typeof window!=='undefined'?window:globalThis);
