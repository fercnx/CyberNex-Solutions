/* CYBERNEX 10.0V — Password Lab (lógica)
   Todo se procesa localmente en el navegador: la contraseña nunca se envía,
   guarda ni registra. */
(function(root){
'use strict';
var NS=root.CYBERNEX=root.CYBERNEX||{};

/* Lista breve incorporada de contraseñas muy comunes (no es exhaustiva). */
var COMMON=('123456 password 12345678 qwerty 123456789 12345 1234 111111 1234567 dragon 123123 baseball abc123 football monkey letmein shadow master '+
'666666 qwertyuiop 123321 mustang 1234567890 michael 654321 superman 1qaz2wsx 7777777 121212 000000 qazwsx 123qwe killer trustno1 jordan jennifer '+
'zxcvbnm asdfgh hunter buster soccer harley batman andrew tigger sunshine iloveyou 2000 charlie robert thomas hockey ranger daniel starwars 112233 '+
'george computer michelle jessica pepper 1111 zxcvbn 555555 11111111 131313 freedom 777777 pass maggie 159753 aaaaaa ginger princess joshua cheese '+
'amanda summer love ashley nicole chelsea biteme matthew access yankees 987654321 dallas austin thunder taylor matrix contrasena admin administrador '+
'bienvenido bienvenida hola123 cybernex passw0rd welcome login qwerty123 admin123 password1 123456a a123456 11223344 1q2w3e4r 1q2w3e futbol '+
'barcelona chivas america mexico teamo tequiero amorcito carlos alejandro contraseña').split(' ');
var COMMON_SET={};COMMON.forEach(function(w){COMMON_SET[w]=1});

var LEET={'0':'o','1':'i','3':'e','4':'a','5':'s','7':'t','@':'a','$':'s','!':'i'};
var ROWS=['qwertyuiop','asdfghjkl','zxcvbnm','1234567890','qazwsxedc'];

function normalize(s){return s.toLowerCase().replace(/[013457@$!]/g,function(c){return LEET[c]})}

function classes(pw){
  return{
    lower:/[a-z]/.test(pw),upper:/[A-Z]/.test(pw),digit:/[0-9]/.test(pw),
    symbol:/[\x20-\x2f\x3a-\x40\x5b-\x60\x7b-\x7e]/.test(pw),other:/[^\x00-\x7f]/.test(pw)
  };
}
function poolSize(c){return(c.lower?26:0)+(c.upper?26:0)+(c.digit?10:0)+(c.symbol?33:0)+(c.other?64:0)}

/* Caracteres que forman parte de repeticiones (aaa), secuencias (abc, 321) o filas del teclado */
function patternChars(pw){
  var low=pw.toLowerCase(),n=low.length,i,mark=new Array(n),found={repeat:false,sequence:false,keyboard:false};
  for(i=0;i<n;i++)mark[i]=false;
  i=0;
  while(i<n){var j=i;while(j+1<n&&low[j+1]===low[i])j++;if(j-i>=2){found.repeat=true;for(var k=i+1;k<=j;k++)mark[k]=true}i=j+1}
  i=0;
  while(i<n-2){
    var d=low.charCodeAt(i+1)-low.charCodeAt(i);
    if(Math.abs(d)===1){
      var j2=i+1;while(j2+1<n&&low.charCodeAt(j2+1)-low.charCodeAt(j2)===d)j2++;
      if(j2-i>=2){found.sequence=true;for(var k2=i+1;k2<=j2;k2++)mark[k2]=true}
      i=j2;
    }else i++;
  }
  ROWS.forEach(function(row){
    var rev=row.split('').reverse().join('');
    [row,rev].forEach(function(r){
      for(var len=Math.min(r.length,n);len>=4;len--){
        for(var s=0;s+len<=r.length;s++){
          var sub=r.substr(s,len),at=low.indexOf(sub);
          while(at!==-1){found.keyboard=true;for(var m=at;m<at+len;m++)mark[m]=true;at=low.indexOf(sub,at+1)}
        }
      }
    });
  });
  var c=0;for(i=0;i<n;i++)if(mark[i])c++;
  return{count:c,found:found};
}

function formatTime(sec){
  if(!isFinite(sec))return 'prácticamente infinito';
  if(sec<1)return 'menos de un segundo';
  if(sec<60)return Math.round(sec)+' segundos';
  var m=sec/60;if(m<60)return Math.round(m)+' minutos';
  var h=m/60;if(h<24)return Math.round(h)+' horas';
  var d=h/24;if(d<365)return Math.round(d)+' días';
  var y=d/365;
  if(y<1000)return Math.round(y).toLocaleString('es-MX')+' años';
  if(y<1e6)return 'miles de años';
  if(y<1e9)return 'millones de años';
  return 'miles de millones de años';
}

var LABELS=['Muy débil','Débil','Aceptable','Fuerte','Muy fuerte'];

function analyze(pw){
  pw=String(pw==null?'':pw);
  var len=pw.length;
  if(!len)return{empty:true,length:0};
  var c=classes(pw),pool=poolSize(c),norm=normalize(pw);
  var issues=[],tips=[];
  var pat=patternChars(pw);
  var eff=len-pat.count*0.8;
  var exactCommon=!!COMMON_SET[norm]||!!COMMON_SET[pw.toLowerCase()];
  var containsCommon=null;
  if(!exactCommon){
    for(var i=0;i<COMMON.length;i++){var w=COMMON[i];if(w.length>=5&&norm.indexOf(w)!==-1){if(!containsCommon||w.length>containsCommon.length)containsCommon=w}}
    if(containsCommon){eff-=containsCommon.length*0.8;issues.push('Contiene una palabra o patrón muy común («'+containsCommon+'»).')}
  }
  if(/(19|20)\d{2}/.test(pw)){eff-=3;issues.push('Incluye un año; son fáciles de adivinar.')}
  if(pat.found.repeat)issues.push('Tiene caracteres repetidos seguidos.');
  if(pat.found.sequence)issues.push('Contiene secuencias (abc, 123, 987…).');
  if(pat.found.keyboard)issues.push('Sigue una fila del teclado (qwerty, asdf…).');
  var unique=new Set(pw.split('')).size;
  if(unique<len*0.5&&len>=6){eff-=2;issues.push('Usa pocos caracteres distintos.')}
  if(eff<0)eff=0;
  var entropy=eff*Math.log(pool||1)/Math.LN2;
  if(exactCommon){entropy=Math.min(entropy,8);issues.unshift('Es una de las contraseñas más usadas: se prueba primero en cualquier ataque.')}
  var level=entropy<28?0:entropy<40?1:entropy<60?2:entropy<80?3:4;
  if(len<8)level=Math.min(level,1);else if(len<12)level=Math.min(level,2);
  if(exactCommon)level=0;
  var guesses=Math.pow(2,entropy)/2,seconds=guesses/1e10;
  var checks=[
    {ok:len>=12,text:'Al menos 12 caracteres'},
    {ok:c.lower,text:'Minúsculas'},{ok:c.upper,text:'Mayúsculas'},
    {ok:c.digit,text:'Números'},{ok:c.symbol,text:'Símbolos'},
    {ok:!pat.found.repeat&&!pat.found.sequence&&!pat.found.keyboard,text:'Sin repeticiones ni secuencias'},
    {ok:!exactCommon&&!containsCommon,text:'No es una contraseña común'}
  ];
  if(len<12)tips.push('Alárgala: lo ideal son 14 caracteres o más. La longitud pesa más que los símbolos.');
  if(!(c.lower&&c.upper&&c.digit&&c.symbol))tips.push('Combina minúsculas, mayúsculas, números y símbolos, o usa una frase larga.');
  if(issues.length)tips.push('Evita nombres, fechas, palabras comunes y patrones del teclado.');
  tips.push('Usa una contraseña distinta en cada cuenta y guárdalas en un gestor de contraseñas.');
  tips.push('Activa la verificación en dos pasos siempre que sea posible.');
  if(level>=3&&!issues.length)tips.unshift('Buen resultado. Recuerda no reutilizarla en otros sitios.');
  return{
    empty:false,length:len,classes:c,pool:pool,entropy:Math.round(entropy),
    level:level,label:LABELS[level],percent:[12,32,55,80,100][level],
    crackTime:formatTime(seconds),checks:checks,issues:issues,tips:tips
  };
}

/* Generador con criptografía del navegador (rechazo para evitar sesgo) */
function randInt(max){
  var cr=root.crypto||(root.msCrypto);
  if(!cr||!cr.getRandomValues)throw new Error('Este navegador no ofrece generación aleatoria segura.');
  var limit=Math.floor(4294967296/max)*max,a=new Uint32Array(1);
  do{cr.getRandomValues(a)}while(a[0]>=limit);
  return a[0]%max;
}
function generate(len){
  len=Math.max(12,Math.min(64,parseInt(len,10)||18));
  var sets=['abcdefghijkmnopqrstuvwxyz','ABCDEFGHJKLMNPQRSTUVWXYZ','23456789','!@#$%^&*()-_=+?'];
  var all=sets.join(''),out=[],i;
  for(i=0;i<sets.length;i++)out.push(sets[i][randInt(sets[i].length)]);
  while(out.length<len)out.push(all[randInt(all.length)]);
  for(i=out.length-1;i>0;i--){var j=randInt(i+1),t=out[i];out[i]=out[j];out[j]=t}
  return out.join('');
}

NS.password={analyze:analyze,generate:generate,formatTime:formatTime};
})(typeof window!=='undefined'?window:globalThis);
