/* CYBERNEX 10.0V — Security Awareness
   Cuestionario educativo y ejemplos de phishing. Todos los ejemplos son
   FICTICIOS y usan dominios reservados (.example); no representan a ninguna
   empresa real. */
(function(root){
'use strict';
var NS=root.CYBERNEX=root.CYBERNEX||{};

var QUESTIONS=[
  {q:'Recibes un correo de «tu banco» que dice que tu cuenta será bloqueada hoy y trae un botón para «verificarla». ¿Qué haces?',
   o:['Pulso el botón rápido para evitar el bloqueo','Entro escribiendo yo mismo la dirección oficial o uso la app, y llamo al número oficial si tengo dudas','Respondo el correo pidiendo más información','Reenvío el correo a mis contactos para advertirles'],
   a:1,e:'Los mensajes con urgencia y enlaces son la base del phishing. Nunca uses el enlace recibido: entra por tu cuenta al sitio oficial.'},
  {q:'Además de una contraseña fuerte, ¿qué medida protege más una cuenta importante?',
   o:['Cambiar la contraseña cada semana','Activar la verificación en dos pasos','Usar el nombre de mascota como respuesta de seguridad','Cerrar el navegador al terminar'],
   a:1,e:'La verificación en dos pasos exige un segundo factor, así que una contraseña robada por sí sola no basta para entrar.'},
  {q:'¿Cuál de estas contraseñas es la mejor opción?',
   o:['Cybernex2024','P@ssw0rd!','tres-nubes-rojas-cantan-lento','12345678Aa'],
   a:2,e:'Una frase larga, única y sin relación personal es difícil de adivinar y fácil de recordar. Las otras siguen patrones muy conocidos.'},
  {q:'Un sitio muestra el candado de HTTPS en el navegador. ¿Qué significa realmente?',
   o:['Que el sitio es 100 % legítimo y seguro','Que la conexión con el sitio está cifrada, pero no garantiza que sea quien dice ser','Que el sitio no tiene virus','Que el sitio está aprobado por el gobierno'],
   a:1,e:'El candado protege la comunicación. Los sitios fraudulentos también pueden tenerlo, por eso hay que revisar el dominio.'},
  {q:'Estás en una cafetería con Wi-Fi gratuita y necesitas revisar tu banca en línea. ¿Qué es lo más prudente?',
   o:['Conectarme y entrar normalmente','Usar mis datos móviles o esperar a una red de confianza','Desactivar el antivirus para que no estorbe','Usar el modo incógnito'],
   a:1,e:'Las redes públicas pueden ser vigiladas o falsificadas. Para operaciones sensibles usa una red de confianza o tus datos móviles.'},
  {q:'Un contacto te escribe por mensajería desde un número nuevo diciendo que tuvo un problema y te pide dinero urgente. ¿Qué haces?',
   o:['Le envío el dinero y luego le pregunto','Confirmo por otro medio (llamada o su número anterior) antes de hacer nada','Le pido una foto para comprobar que es él','Lo ignoro y no hago nada más'],
   a:1,e:'La suplantación de identidad es común. Confirmar por un canal distinto es la forma más fiable de comprobarlo.'},
  {q:'¿Por qué es peligroso usar la misma contraseña en varias cuentas?',
   o:['Porque se desgasta con el uso','Porque si se filtra en un sitio, pueden probarla en todas tus otras cuentas','Porque los sitios la rechazan','No es peligroso si es larga'],
   a:1,e:'Los atacantes prueban contraseñas filtradas en otros servicios. Una contraseña distinta por cuenta limita el daño.'},
  {q:'Te llega un archivo .zip que no esperabas, supuestamente de un proveedor. ¿Qué haces?',
   o:['Lo abro para ver qué contiene','Lo descargo pero no lo abro','No lo abro y confirmo con el proveedor por otro medio','Lo reenvío a mi equipo'],
   a:2,e:'Los adjuntos inesperados son una vía habitual de malware. Confirma con el remitente antes de abrirlos.'}
];

var EXAMPLES=[
  {title:'Ejemplo 1 · Correo de «soporte»',
   body:'De: soporte@cuenta-segura-banco.example\nAsunto: URGENTE: tu cuenta será suspendida en 24 horas\n\nEstimado cliente: detectamos actividad sospechosa. Para evitar la suspensión verifica tus datos aquí: banco.com/verifica',
   flags:['Genera urgencia y amenaza con suspender la cuenta.','El remitente usa un dominio distinto al del banco real.','El texto del enlace parece oficial, pero el destino real sería otro (al pasar el cursor se vería).','Saludo genérico («Estimado cliente») en lugar de tu nombre.','Pide datos por un enlace en vez de que entres por tu cuenta.']},
  {title:'Ejemplo 2 · SMS de paquetería',
   body:'Tu paquete no pudo entregarse. Paga $18 por cargo de aduana para reprogramar: http://envio-mx.example/pago',
   flags:['Cobro pequeño e inesperado para que bajes la guardia.','Enlace a un dominio desconocido y sin HTTPS.','No menciona número de guía ni empresa concreta.','Te presiona a actuar de inmediato.']},
  {title:'Ejemplo 3 · Premio inesperado',
   body:'¡Felicidades! Ganaste una tarjeta de regalo. Responde con el número de tu tarjeta y el código de seguridad para depositarte el premio.',
   flags:['Premio de un concurso en el que no participaste.','Pide datos de tarjeta, que nunca se necesitan para recibir un premio.','Promesa demasiado buena para ser cierta.']}
];

var PRACTICES=[
  'Revisa siempre el remitente y el dominio real del enlace antes de hacer clic.',
  'Ningún servicio serio te pide contraseñas, NIP o códigos por mensaje o llamada.',
  'Ante la duda, entra por tu cuenta al sitio oficial o llama al número oficial.',
  'Activa la verificación en dos pasos y usa contraseñas únicas.',
  'Mantén tus dispositivos y aplicaciones actualizados.',
  'Reporta los mensajes sospechosos y avisa a tu equipo o a tu familia.'
];

function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e}

function renderQuiz(rootEl){
  var i=0,score=0,answered=false;
  function question(){
    var Q=QUESTIONS[i];answered=false;rootEl.textContent='';
    var meta=el('div','q-meta');meta.appendChild(el('span',null,'Pregunta '+(i+1)+' de '+QUESTIONS.length));meta.appendChild(el('span',null,'Aciertos: '+score));
    rootEl.appendChild(meta);
    var q=el('p','quiz-q',Q.q);q.id='quizQ';rootEl.appendChild(q);
    var opts=el('div','opts');opts.setAttribute('role','group');opts.setAttribute('aria-labelledby','quizQ');
    var fb=el('div');fb.setAttribute('aria-live','polite');
    var next=el('button','btn primary','Siguiente');next.type='button';next.hidden=true;
    Q.o.forEach(function(text,idx){
      var b=el('button','opt',text);b.type='button';
      b.addEventListener('click',function(){
        if(answered)return;answered=true;
        var right=idx===Q.a;if(right)score++;
        [].forEach.call(opts.children,function(c,k){c.disabled=true;if(k===Q.a)c.classList.add('right');else if(k===idx)c.classList.add('wrong')});
        fb.appendChild(el('div','explain',(right?'¡Correcto! ':'No es la mejor opción. ')+Q.e));
        next.textContent=i===QUESTIONS.length-1?'Ver resultado':'Siguiente';next.hidden=false;next.focus();
      });
      opts.appendChild(b);
    });
    rootEl.appendChild(opts);rootEl.appendChild(fb);
    var row=el('div');row.style.marginTop='16px';row.appendChild(next);rootEl.appendChild(row);
    next.addEventListener('click',function(){i++;i<QUESTIONS.length?question():result()});
  }
  function result(){
    rootEl.textContent='';
    var pct=Math.round(score/QUESTIONS.length*100);
    rootEl.appendChild(el('div','level',score+' de '+QUESTIONS.length+' respuestas correctas ('+pct+' %)'));
    rootEl.appendChild(el('p','muted',pct>=75?'Muy bien: reconoces las señales más comunes. Sigue practicando.':pct>=50?'Vas por buen camino. Repasa las explicaciones y los ejemplos de phishing.':'Repasa las buenas prácticas y los ejemplos de phishing y vuelve a intentarlo.'));
    var again=el('button','btn primary','Intentar de nuevo');again.type='button';
    again.addEventListener('click',function(){i=0;score=0;question()});
    rootEl.appendChild(again);
  }
  question();
}

function renderExamples(rootEl){
  rootEl.textContent='';
  EXAMPLES.forEach(function(ex){
    var card=el('div','card');card.style.marginBottom='14px';
    card.appendChild(el('h3',null,ex.title));
    var s=el('div','sample');s.appendChild(el('small',null,'Mensaje ficticio con fines educativos'));
    var pre=el('div',null,ex.body);pre.style.whiteSpace='pre-wrap';s.appendChild(pre);card.appendChild(s);
    var d=document.createElement('details'),sum=el('summary',null,'Ver señales de alerta'),ul=el('ul');
    ex.flags.forEach(function(f){ul.appendChild(el('li',null,f))});
    d.appendChild(sum);d.appendChild(ul);card.appendChild(d);rootEl.appendChild(card);
  });
}

function renderPractices(rootEl){
  rootEl.textContent='';var ul=el('ul','tips');
  PRACTICES.forEach(function(p){ul.appendChild(el('li',null,p))});rootEl.appendChild(ul);
}

NS.awareness={renderQuiz:renderQuiz,renderExamples:renderExamples,renderPractices:renderPractices,QUESTIONS:QUESTIONS,EXAMPLES:EXAMPLES};
})(typeof window!=='undefined'?window:globalThis);
