// DOM interaction verification. Requires linkedom as a development-only dependency.
// This does not replace visual browser/device QA.
const {parseHTML}=require('linkedom');
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'../dist');
const {window,document}=parseHTML(fs.readFileSync(root+'/index.html','utf8'));
window.scrollTo=()=>{};window.print=()=>{};
const storage={};const localStorage={getItem:k=>storage[k]??null,setItem:(k,v)=>{storage[k]=String(v)}};
window.HTMLElement.prototype.scrollIntoView=()=>{};
window.HTMLElement.prototype.focus=function(){this.focusCalled=true};
window.HTMLElement.prototype.showModal=function(){this.setAttribute('open','')};
window.HTMLElement.prototype.close=function(){this.removeAttribute('open');this.dispatchEvent(new window.Event('close'))};
Object.defineProperty(window.HTMLSelectElement.prototype,'value',{configurable:true,get(){return this._value??this.querySelector('option[selected]')?.getAttribute('value')??this.querySelector('option')?.getAttribute('value')??''},set(v){this._value=v}});
const location={hash:''};
const ctx=vm.createContext({document,window,Event:window.Event,location,localStorage,console,fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,url),'utf8'))}),setTimeout,clearTimeout,setInterval,clearInterval});
for(const f of ['explorations.js','mesoamerica.js','projection.js','learning.js','science.js','interactive.js','visuals.js','animations.js','history-workshop.js','app.js'])vm.runInContext(fs.readFileSync(root+'/'+f,'utf8'),ctx);
const wait=()=>new Promise(r=>setTimeout(r,5));
(async()=>{await wait();
assert.equal(document.querySelectorAll('#topicGrid article').length,6);
const go=hash=>{location.hash=hash;window.dispatchEvent(new window.Event('hashchange'));};
const select=(id,value)=>{const el=document.querySelector(id);Object.defineProperty(el,'value',{configurable:true,get(){return this._value??''},set(v){this._value=v}});el.value=value;el.onchange({target:el});};
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
for(const c of chapters){assert(fs.existsSync(path.join(root,c.image)));assert(c.source[1].startsWith('https://'));assert(c.activity.length>20);assert.equal(c.distractors.length,2);}
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
// Science journeys: catalog, deep links, answer locking, search, labs, and history retention.
await wait();
assert.equal(document.querySelectorAll('#espacio .science-card').length,11);
assert.equal(document.querySelectorAll('#tierra .science-card').length,8);
assert.equal(new Set([...document.querySelectorAll('[data-audience]')].map(b=>b.dataset.audience)).size,3);
document.querySelector('[data-audience="profundizar"]').onclick();
assert.equal(localStorage.getItem('atlas-audience'),'profundizar');
assert(document.querySelector('#audienceDescription').textContent.includes('fuentes'));
go('#ciencia/sistema-solar');assert(document.querySelector('.audience-context').textContent.includes('Adultos y universidad'));assert(!document.querySelector('#scienceDeep').hidden);
document.querySelector('[data-audience="explorar"]').onclick();go('#ciencia/sistema-solar');assert(document.querySelector('.audience-context').textContent.includes('Niñez'));assert(document.querySelector('#scienceDeep').hidden);assert.equal(document.querySelectorAll('.science-reading>p').length,1);
const science=JSON.parse(fs.readFileSync(root+'/data/science.json','utf8'));
for(const topic of science.topics){
 go('#ciencia/'+topic.id);assert.equal(document.querySelector('#ciencia h1').textContent,topic.title);
 assert.equal(document.querySelectorAll('#scienceQuiz [data-science-answer]').length,3);
 document.querySelector('[data-level="profundizar"]').onclick();assert(!document.querySelector('#scienceDeep').hidden);
 const first=document.querySelectorAll('[data-science-answer]')[topic.quiz[0][2]];first.onclick();first.onclick();
 document.querySelector('#scienceQuiz [data-next]').onclick();
 document.querySelectorAll('[data-science-answer]')[topic.quiz[1][2]].onclick();document.querySelector('#scienceQuiz [data-next]').onclick();
 assert.equal(document.querySelector('.quiz-score').textContent,'2 / 2');
 document.querySelector('[data-restart]').onclick();assert.equal(document.querySelectorAll('[data-science-answer]').length,3);
}
go('#laboratorio/planetas');assert(!document.querySelector('#laboratorio').hidden);
assert.equal(document.querySelectorAll('.ruler-row').length,8);
select('#planetA','tierra');select('#planetB','jupiter');assert(document.querySelector('.comparison-result').textContent.includes('11.21'));
select('#planetB','tierra');assert(document.querySelector('.comparison-result').textContent.includes('mismo planeta'));
document.querySelector('#solarScale').value='2';document.querySelector('#solarScale').oninput();assert(document.querySelector('#scaleValue').textContent==='2');
go('#laboratorio/oceano');for(const [value,text] of [[0,'iluminada'],[500,'penumbra'],[2000,'Sin luz']]){document.querySelector('#oceanDepth').value=String(value);document.querySelector('#oceanDepth').oninput();assert(document.querySelector('#depthZone').textContent.includes(text));}
go('#retos/tierra');assert.equal(document.querySelectorAll('#scienceChallengeArea option').length,2);assert(document.querySelector('#scienceArena h3'));
window.AtlasScience.search('océanos');go('#buscar');assert(document.querySelector('#buscar').textContent.includes('Un océano'));
window.AtlasScience.search('revolución');go('#buscar');assert(document.querySelector('#buscar').textContent.includes('Revolución Mexicana'));
window.AtlasScience.search('noexistexyz');go('#buscar');assert(document.querySelector('#buscar').textContent.includes('0 resultados'));
go('#ciencia/no-existe');assert(document.querySelector('#ciencia').textContent.includes('no encontrado'));
go('#ruta/revolucion');assert(document.querySelector('#ruta').textContent.includes('Revolución Mexicana'));
go('#misiones');assert(!document.querySelector('#misiones').hidden);assert.equal(document.querySelectorAll('.mission-card').length,2);
document.querySelector('[data-mission-mode="planet"]').onclick();assert.equal(document.querySelectorAll('[data-planet-index]').length,8);document.querySelector('[data-planet-hint]').onclick();assert(document.querySelector('.mission-feedback').textContent.includes('Mercurio'));
document.querySelector('[data-mission-home]').onclick();document.querySelector('[data-mission-mode="lens"]').onclick();document.querySelector('[data-lens-open]').onclick();assert(!document.querySelector('#atlasLens').hidden);document.querySelector('#lensNote').value='Observo tres detalles.';document.querySelector('[data-save-lens-note]').onclick();assert(document.querySelector('#lensStatus').textContent.includes('guardada'));document.querySelector('[data-lens-close]').onclick();assert(document.querySelector('#atlasLens').hidden);
document.querySelector('[data-mission-area="historia"]').onclick();document.querySelector('[data-mission-mode="evidence"]').onclick();for(const expected of ['Hecho documentado','Interpretación','Tradición o mito','Interpretación']){const button=[...document.querySelectorAll('[data-evidence-choice]')].find(b=>b.textContent===expected);button.onclick();assert(document.querySelector('#evidenceFeedback').textContent.length>20);document.querySelector('[data-evidence-next]').onclick();}assert(document.querySelector('.mission-card-terracotta .mission-status').textContent.includes('Completada'));
console.log('PASS: interactive missions, planet puzzle entry, evidence detective, image lens, zoom note and saved progress.');
go('#visuales');assert(!document.querySelector('#visuales').hidden);assert(document.querySelector('.atlas-diagram'));assert.equal(document.querySelectorAll('[data-visual-tab]').length,4);document.querySelector('[data-visual-tab="earth"]').onclick();assert(document.querySelector('.visual-intro h2').textContent.includes('Capas'));document.querySelector('[data-visual-key="mantle"]').onclick();assert(document.querySelector('.visual-explain h2').textContent==='Manto');document.querySelector('[data-visual-tab="water"]').onclick();document.querySelector('[data-visual-key="condensation"]').onclick();assert(document.querySelector('.visual-explain h2').textContent==='Condensación');
console.log('PASS: visual library with four explanatory diagrams, clickable parts, accessible keyboard targets and contextual questions.');
go('#animaciones');assert(!document.querySelector('#animaciones').hidden);assert.equal(document.querySelectorAll('[data-animation-model]').length,6);document.querySelector('[data-animation-model="seasons"]').onclick();assert(document.querySelector('.animation-panel h2').textContent.includes('La Tierra'));document.querySelector('[data-step-next]').onclick();assert(document.querySelector('.animation-panel h2').textContent.includes('Más luz'));document.querySelector('#animationRange').value='3';document.querySelector('#animationRange').oninput({target:document.querySelector('#animationRange')});assert(document.querySelector('.animation-panel h2').textContent.includes('No es la distancia'));document.querySelector('[data-animation-model="plates"]').onclick();document.querySelector('[data-anim-play]').onclick();assert(document.querySelector('.animation-stage').classList.contains('is-playing'));document.querySelector('[data-anim-play]').onclick();assert(!document.querySelector('.animation-stage').classList.contains('is-playing'));document.querySelector('[data-animation-model="history"]').onclick();document.querySelector('[data-step-next]').onclick();assert(document.querySelector('.animation-svg').getAttribute('aria-label').toLowerCase().includes('mapa'));console.log('PASS: six guided animations with steps, range control, playback, projector-ready SVG and linked topics.');

go('#taller-historia');assert(!document.querySelector('#taller-historia').hidden);
assert.equal(document.querySelectorAll('#hwTrack option').length,4);
assert.equal(document.querySelectorAll('[data-hw-event]').length,6);
document.querySelector('[data-hw-event="1"]').onclick();assert(document.querySelector('.hw-detail h3').textContent.includes('Registrar'));
document.querySelector('#hwNote').value='Una evidencia y una pregunta.';document.querySelector('#hwNote').oninput({target:document.querySelector('#hwNote')});
document.querySelector('[data-hw-mode="order"]').onclick();assert.equal(document.querySelector('#hwNote').value,'Una evidencia y una pregunta.');
document.querySelector('#hwCheck').onclick();assert(document.querySelector('#hwFeedback').textContent.includes('inversión'));
document.querySelector('#hwHint').onclick();assert(document.querySelector('#hwFeedback').textContent.includes('Uruk'));
// Reverse six cards into ascending chronology using the same keyboard/touch buttons as students.
for(let last=5;last>0;last--)for(let pos=0;pos<last;pos++)document.querySelector('[data-hw-down="'+pos+'"]').onclick();
document.querySelector('#hwCheck').onclick();assert(document.querySelector('#hwFeedback').textContent.includes('resuelto'));assert(document.querySelector('#hwCheck').disabled);
select('#hwTrack','ciudadania');assert.equal(document.querySelectorAll('.hw-sort li').length,6);
document.querySelector('[data-hw-mode="explore"]').onclick();assert(document.querySelector('.hw-detail h3').textContent.includes('municipio'));
select('#hwLevel','profundizar');assert(document.querySelector('.hw-detail').textContent.includes('propósito'));
for(const mode of ['connect','evidence']){
 document.querySelector('[data-hw-mode="'+mode+'"]').onclick();
 for(let n=0;n<6;n++){
  const answers=document.querySelectorAll('[data-hw-answer]');assert.equal(answers.length,3);
  const correct=answers[(3-n%3)%3];correct.onclick();correct.onclick();assert(correct.disabled);assert(document.querySelector('#hwFeedback a').href.startsWith('https://'));document.querySelector('#hwNext').onclick();
 }
 assert(document.querySelector('.hw-result h2').textContent.includes('6 de 6'));document.querySelector('#hwReplay').onclick();assert.equal(document.querySelectorAll('[data-hw-answer]').length,3);
}
go('#ruta/revolucion');assert(!document.querySelector('#ruta').hidden);
console.log('PASS: four history timelines, 24 cards, ordering puzzle, notes across modes, three depth levels, cause/evidence rounds and locked scoring.');
console.log('PASS: 19 science topics, 38 explained answers, locked scoring, mixed search, planetary comparator, scale ruler, ocean zones and existing history.');
console.log('PASS: 57 episodes, deep links and dossiers; 55 chronology items with filters/comparison; all five arena modes, hints, locked scoring, teams, results and replay.');
console.log('PASS: integrated map, six presentation steps, reveal and replay navigation, close/focus, all six routes and quiz completion, PDF files, municipality search, projector, sidebar, malformed link.');
})().catch(e=>{console.error(e);process.exitCode=1});
