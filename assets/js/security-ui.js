/* CYBERNEX 10.0V — NEX Security: interfaz (pestañas, Password Lab, URL Check) */
(function(){
'use strict';
var NS=window.CYBERNEX||{};
function $(id){return document.getElementById(id)}
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e}

/* ---------- Pestañas ---------- */
var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
var panels=tabs.map(function(t){return $(t.getAttribute('aria-controls'))});
function activate(i,focus,updateHash){
  tabs.forEach(function(t,n){
    var on=n===i;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;panels[n].hidden=!on;
  });
  if(focus)tabs[i].focus();
  if(updateHash&&history.replaceState){try{history.replaceState(null,'','#'+tabs[i].getAttribute('data-tab'))}catch(e){}}
}
tabs.forEach(function(t,n){
  t.addEventListener('click',function(){activate(n,false,true)});
  t.addEventListener('keydown',function(e){
    var k=e.key,m=null;
    if(k==='ArrowRight')m=(n+1)%tabs.length;else if(k==='ArrowLeft')m=(n-1+tabs.length)%tabs.length;
    else if(k==='Home')m=0;else if(k==='End')m=tabs.length-1;
    if(m!==null){e.preventDefault();activate(m,true,true)}
  });
});
function fromHash(){
  var h=(location.hash||'').replace('#',''),i=0;
  tabs.forEach(function(t,n){if(t.getAttribute('data-tab')===h)i=n});
  activate(i,false,false);
}
window.addEventListener('hashchange',fromHash);
fromHash();

/* ---------- Password Lab ---------- */
var pw=$('pw');
if(pw&&NS.password){
  var meter=$('pwMeter'),fill=meter.firstElementChild,lvl=$('pwLevel'),stats=$('pwStats'),checks=$('pwChecks'),tips=$('pwTips'),issues=$('pwIssues');
  function renderPw(){
    var r=NS.password.analyze(pw.value);
    if(r.empty){
      fill.style.width='0';meter.removeAttribute('data-level');meter.setAttribute('aria-valuenow','0');
      lvl.textContent='Escribe una contraseña para evaluarla';stats.hidden=true;checks.textContent='';issues.textContent='';tips.textContent='';tips.appendChild(el('li',null,'Escribe una contraseña para ver recomendaciones personalizadas.'));return;
    }
    fill.style.width=r.percent+'%';meter.setAttribute('data-level',String(r.level));meter.setAttribute('aria-valuenow',String(r.percent));
    lvl.textContent=r.label;stats.hidden=false;
    $('pwLen').textContent=r.length+' caracteres';
    $('pwEnt').textContent='≈ '+r.entropy+' bits';
    $('pwTime').textContent=r.crackTime;
    checks.textContent='';r.checks.forEach(function(c){var li=el('li',c.ok?'ok':'',c.text);checks.appendChild(li)});
    issues.textContent='';r.issues.forEach(function(t){var li=el('li',null,t);issues.appendChild(li)});
    tips.textContent='';r.tips.forEach(function(t){tips.appendChild(el('li',null,t))});
  }
  pw.addEventListener('input',renderPw);
  $('pwToggle').addEventListener('click',function(){
    var show=pw.type==='password';pw.type=show?'text':'password';
    this.textContent=show?'Ocultar':'Mostrar';this.setAttribute('aria-pressed',String(show));
  });
  $('pwClear').addEventListener('click',function(){pw.value='';pw.type='password';$('pwToggle').textContent='Mostrar';$('pwToggle').setAttribute('aria-pressed','false');renderPw();pw.focus()});
  renderPw();

  var genLen=$('genLen'),genOut=$('genOut'),genMsg=$('genMsg');
  genLen.addEventListener('input',function(){$('genLenVal').textContent=genLen.value});
  $('genBtn').addEventListener('click',function(){
    try{genOut.value=NS.password.generate(genLen.value);genMsg.textContent='Contraseña generada en tu navegador. No se guardó ni se envió.'}
    catch(e){genMsg.textContent=e.message}
  });
  $('genCopy').addEventListener('click',function(){
    if(!genOut.value){genMsg.textContent='Primero genera una contraseña.';return}
    function fallback(){genOut.select();try{document.execCommand('copy');genMsg.textContent='Copiada al portapapeles.'}catch(e){genMsg.textContent='No se pudo copiar automáticamente; selecciónala y cópiala.'}}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(genOut.value).then(function(){genMsg.textContent='Copiada al portapapeles.'},fallback)}else fallback();
  });
  $('genUse').addEventListener('click',function(){if(genOut.value){pw.value=genOut.value;renderPw()}});
}

/* ---------- URL Check ---------- */
var form=$('urlForm');
if(form&&NS.urlcheck){
  var out=$('urlOut'),input=$('urlIn');
  function showUrl(){
    var r=NS.urlcheck.analyze(input.value);out.textContent='';
    if(!r.valid){
      var v=el('div','verdict error');v.appendChild(el('span','dot'));
      var b=el('div');b.appendChild(el('h3',null,'No se pudo analizar'));b.appendChild(el('p',null,r.error));v.appendChild(b);out.appendChild(v);return;
    }
    var vd=el('div','verdict '+r.verdict.level),d=el('span','dot'),bx=el('div');
    vd.setAttribute('role','status');
    bx.appendChild(el('h3',null,r.verdict.label));bx.appendChild(el('p',null,r.verdict.text));vd.appendChild(d);vd.appendChild(bx);out.appendChild(vd);
    var dl=el('dl','parts');
    [['Protocolo',r.parts.protocolo],['Dominio',r.parts.dominio],['Dominio principal',r.parts.dominioPrincipal],['Puerto',r.parts.puerto],['Ruta',r.parts.ruta]].forEach(function(p){
      dl.appendChild(el('dt',null,p[0]));dl.appendChild(el('dd',null,p[1]));
    });
    out.appendChild(dl);
    var ul=el('ul','findings');
    var order={alto:0,medio:1,bajo:2,info:3,ok:4};
    r.findings.slice().sort(function(a,b){return order[a.sev]-order[b.sev]}).forEach(function(f){
      var li=el('li'),t=el('div');
      li.appendChild(el('span','chip '+f.sev,f.sev==='ok'?'Bien':f.sev==='info'?'Nota':f.sev));
      t.appendChild(el('b',null,f.title));t.appendChild(el('span','d',f.detail));li.appendChild(t);ul.appendChild(li);
    });
    out.appendChild(ul);
  }
  form.addEventListener('submit',function(e){e.preventDefault();showUrl()});
  [].forEach.call(document.querySelectorAll('[data-example]'),function(b){
    b.addEventListener('click',function(){input.value=b.getAttribute('data-example');showUrl()});
  });
  $('urlClear').addEventListener('click',function(){input.value='';out.textContent='';input.focus()});
}

/* ---------- Checklist y Concientización ---------- */
if(NS.checklist&&$('checklistRoot'))NS.checklist.render($('checklistRoot'));
if(NS.awareness){
  if($('quizRoot'))NS.awareness.renderQuiz($('quizRoot'));
  if($('examplesRoot'))NS.awareness.renderExamples($('examplesRoot'));
  if($('practicesRoot'))NS.awareness.renderPractices($('practicesRoot'));
}
})();
