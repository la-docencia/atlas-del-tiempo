// DOM interaction verification. Requires linkedom as a development-only dependency.
// This does not replace visual browser/device QA.
const {parseHTML}=require('linkedom');
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'../dist');
const {window,document}=parseHTML(fs.readFileSync(root+'/index.html','utf8'));
window.scrollTo=()=>{};window.print=()=>{};
window.HTMLElement.prototype.scrollIntoView=()=>{};
window.HTMLElement.prototype.focus=function(){this.focusCalled=true};
window.HTMLElement.prototype.showModal=function(){this.setAttribute('open','')};
window.HTMLElement.prototype.close=function(){this.removeAttribute('open');this.dispatchEvent(new window.Event('close'))};
Object.defineProperty(window.HTMLSelectElement.prototype,'value',{configurable:true,get(){return this._value??this.querySelector('option[selected]')?.getAttribute('value')??this.querySelector('option')?.getAttribute('value')??''},set(v){this._value=v}});
const location={hash:''};
const ctx=vm.createContext({document,window,Event:window.Event,location,console,fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(root+url,'utf8'))}),setTimeout,clearTimeout});
for(const f of ['explorations.js','mesoamerica.js','projection.js','learning.js','app.js'])vm.runInContext(fs.readFileSync(root+'/'+f,'utf8'),ctx);
const wait=()=>new Promise(r=>setTimeout(r,5));
(async()=>{await wait();
assert.equal(document.querySelectorAll('#topicGrid article').length,6);
const go=hash=>{location.hash=hash;window.dispatchEvent(new window.Event('hashchange'));};
const select=(id,value)=>{const el=document.querySelector(id);Object.defineProperty(el,'value',{configurable:true,get(){return this._value??''},set(v){this._value=v}});el.value=value;el.onchange();};
go('#historietas');assert(!document.querySelector('#historietas').hidden);
assert.equal(document.querySelector('#comicCount').textContent,'Episodio 1 de 10');
document.querySelector('#comicNext').onclick();assert.equal(document.querySelector('#comicCount').textContent,'Episodio 2 de 10');
document.querySelector('#comicNext').onclick();assert.equal(document.querySelector('#comicCount').textContent,'Episodio 3 de 10');
document.querySelector('#comicPrev').onclick();assert.equal(document.querySelector('#comicCount').textContent,'Episodio 2 de 10');
document.querySelector('[data-scene="0"]').onclick();
document.querySelector('#comicPlay').onclick();assert.equal(document.querySelector('#comicPlay').getAttribute('aria-pressed'),'true');
document.querySelector('#comicPlay').onclick();assert.equal(document.querySelector('#comicPlay').getAttribute('aria-pressed'),'false');
document.querySelector('#comicPlay').onclick();go('#patrimonio');assert.equal(document.querySelector('#comicPlay').getAttribute('aria-pressed'),'false');
assert.equal(document.querySelectorAll('.heritage-card').length,47);assert.equal(document.querySelectorAll('[data-guide-state]').length,32);
select('#heritageState','8');assert.equal(document.querySelectorAll('.heritage-card').length,9);assert(document.querySelector('#heritageCards').textContent.includes('Paquimé'));
document.querySelector('#heritageReset').onclick();assert.equal(document.querySelectorAll('.heritage-card').length,47);
document.querySelector('#heritageSearch').value='queretaro';document.querySelector('#heritageSearch').oninput();assert.equal(document.querySelectorAll('.heritage-card').length,1);
document.querySelector('#heritageSearch').value='zzznomatch';document.querySelector('#heritageSearch').oninput();assert.equal(document.querySelectorAll('.heritage-card').length,0);
document.querySelector('#heritageReset').onclick();
select('#heritageType','Sitio arqueológico');assert(document.querySelectorAll('.heritage-card').length>0);assert(document.querySelectorAll('.heritage-card').length<47);
const heritage=JSON.parse(fs.readFileSync(root+'/data/heritage.json','utf8'));assert.equal(new Set(heritage.map(p=>p.stateCode)).size,32);
for(const p of heritage){go('#patrimonio/'+p.id);assert(!document.querySelector('#patrimonio').hidden);assert.equal(document.querySelector('.heritage-detail h2').textContent,p.name);assert(document.querySelector('.heritage-reference a').href.startsWith('https://'));}
for(const year of [1910,1911,1917])assert(fs.existsSync(root+'/assets/revolucion-'+year+'.webp'));
console.log('PASS: comic controls, pause on exit; 32-state map, 47 heritage details, 9 Chihuahua places and filters.');

location.hash='#ruta/mesoamerica';vm.runInContext('navigate()',ctx);await wait();
assert.equal(document.querySelectorAll('[data-route-map] [data-place]').length,3);
const p=document.querySelector('[data-route-map] [data-place="2"]');p.onclick();assert(document.querySelector('.place-reading').textContent.includes('Palenque'));
const opener=document.querySelector('#presentMeso');opener.onclick({currentTarget:opener});
assert(document.querySelector('#mesoPresenter[open]'));assert.equal(document.querySelector('[data-count]').textContent,'1 de 6');
document.querySelector('[data-next]').onclick();await wait();assert.equal(document.querySelectorAll('[data-lesson-map] [data-place]').length,3);
for(let n=0;n<3;n++)document.querySelector('[data-next]').onclick();
assert.equal(document.querySelector('[data-count]').textContent,'5 de 6');
assert(document.querySelector('.lesson-answer').hidden);document.querySelector('[data-reveal]').dispatchEvent(new window.Event('click'));assert(!document.querySelector('.lesson-answer').hidden);
document.querySelector('[data-prev]').onclick();assert.equal(document.querySelector('[data-count]').textContent,'4 de 6');
for(let n=0;n<3;n++)document.querySelector('[data-next]').onclick();assert(!document.querySelector('#mesoPresenter'));assert(!document.body.classList.contains('presenting'));assert(opener.focusCalled);
for(const id of ['mesoamerica','independencia','revolucion','antigua','nacion','segunda-guerra-mundial']){location.hash='#ruta/'+id;vm.runInContext('navigate()',ctx);assert.equal(document.querySelectorAll('[data-panel]').length,5);if(id!=='mesoamerica'){const opener=document.querySelector('#presentRoute');opener.onclick();assert(document.querySelector('#routePresenter[open]'));assert.equal(document.querySelector('#routePresenter [data-prev]').disabled,true);let count=0;while(document.querySelector('#routePresenter')&&count++<30)document.querySelector('#routePresenter [data-next]').onclick();assert(!document.querySelector('#routePresenter'));assert(opener.focusCalled);}const q=document.querySelector('#routeQuiz');for(let n=0;n<JSON.parse(fs.readFileSync(root+'/data/topics.json')).find(t=>t.id===id).quiz.length;n++){q.querySelector('[data-option]').onclick();assert(q.querySelector('[data-option]').disabled);q.querySelector('.next').onclick()}assert(q.textContent.includes('Reto completado'));assert(fs.existsSync(root+'/downloads/'+id+'.pdf'))}
location.hash='#mapa';vm.runInContext('navigate()',ctx);assert.equal(document.querySelectorAll('[data-state]').length,32);document.querySelector('#stateSelect').value='8';document.querySelector('#stateSelect').onchange();document.querySelector('#localSearch').value='Delicias';document.querySelector('#localSearch').oninput();assert.equal(document.querySelectorAll('[data-mun]').length,1);
vm.runInContext('projector()',ctx);assert(document.body.classList.contains('projector-mode'));assert(!document.querySelector('#projectionTools').hidden);document.querySelector('#projectionSize').onclick();assert(document.body.classList.contains('projection-large'));assert(document.querySelector('#projectorBtn').getAttribute('aria-label').includes('Salir'));vm.runInContext('projector()',ctx);assert(!document.body.classList.contains('projector-mode'));assert(document.querySelector('#projectionTools').hidden);assert(!document.body.classList.contains('projection-large'));
document.querySelector('#sidebarToggle').onclick();assert(document.body.classList.contains('menu-open'));document.querySelector('#sidebarClose').onclick();assert(!document.body.classList.contains('menu-open'));
location.hash='#%invalid';vm.runInContext('navigate()',ctx);assert(!document.querySelector('#explorar').hidden);

const chapters=JSON.parse(fs.readFileSync(root+'/data/chapters.json','utf8'));
assert.equal(chapters.length,57);assert.equal(new Set(chapters.map(c=>c.id)).size,57);
for(const c of chapters){assert(fs.existsSync(root+c.image));assert(c.source[1].startsWith('https://'));assert(c.activity.length>20);assert.equal(c.distractors.length,2);}
go('#patrimonio');assert.equal(document.querySelectorAll('#heritageState option').length,33);
for(const id of ['mesoamerica','independencia','revolucion','antigua','nacion','segunda-guerra-mundial']){
 go('#historietas/'+id);const expected=chapters.filter(c=>c.route===id).length;
 assert(document.querySelector('#comicCount').textContent.endsWith('de '+expected));
 go('#historietas/'+id+'/3');assert(document.querySelector('#comicCount').textContent.startsWith('Episodio 3'));
 go('#ruta/'+id);assert.equal(document.querySelectorAll('.dossier-chapter').length,expected);
}
go('#linea');assert.equal(document.querySelectorAll('#timelineEvents article').length,55);
select('#timeRoute','revolucion');assert.equal(document.querySelectorAll('#timelineEvents article').length,10);
select('#timeTheme','Derechos');assert.equal(document.querySelectorAll('#timelineEvents article').length,2);
const comparisons=document.querySelectorAll('[data-compare]');comparisons[0].onclick();document.querySelectorAll('[data-compare]')[1].onclick();assert.equal(document.querySelectorAll('#timelineCompare article').length,2);
select('#timePeriod','antiguo');assert.equal(document.querySelectorAll('#timelineEvents article').length,0);
document.querySelector('#timeReset').onclick();assert.equal(document.querySelectorAll('#timelineEvents article').length,55);assert.equal(document.querySelectorAll('#timelineCompare article').length,0);
go('#juegos');select('#gameTopic','segunda-guerra-mundial');
for(const kind of ['knowledge','places','people','sources','sequence']){
 selectValue('#arenaKind',kind);selectValue('#arenaLevel','secundaria');selectValue('#arenaTeams','2');document.querySelector('#startArena').onclick();
 let count=0;
 while(document.querySelector('[data-arena-answer]')&&count++<30){
  document.querySelector('#arenaHint').onclick();assert(document.querySelector('#hintText').textContent.length>0);
  const answer=document.querySelector('[data-arena-answer]');answer.onclick();
  const score=document.querySelector('.scoreboard').textContent;answer.onclick();assert.equal(document.querySelector('.scoreboard').textContent,score,'answer cannot score twice');
  assert(document.querySelector('#arenaFeedback').textContent.includes('evidencia')||document.querySelector('#arenaFeedback').textContent.includes('acertada'));
  document.querySelector('#arenaNext').onclick();
 }
 assert(count>0&&count<30);assert(document.querySelector('.arena-result'));assert(document.querySelector('#replayArena'));
 document.querySelector('#replayArena').onclick();assert(document.querySelector('[data-arena-answer]'));
}
function selectValue(id,value){const el=document.querySelector(id);Object.defineProperty(el,'value',{configurable:true,get(){return this._value??''},set(v){this._value=v}});el.value=value;}
// Initial visit directly to an illustrated episode and a safe fallback for invalid ids.
go('#historietas/not-found');assert(document.querySelector('#comicFrame'));go('#mapa');assert(!document.querySelector('#mapa').hidden);
console.log('PASS: 57 episodes, deep links and dossiers; 55 chronology items with filters/comparison; all five arena modes, hints, locked scoring, teams, results and replay.');
console.log('PASS: integrated map, six presentation steps, reveal and replay navigation, close/focus, all six routes and quiz completion, PDF files, municipality search, projector, sidebar, malformed link.');
})().catch(e=>{console.error(e);process.exitCode=1});
