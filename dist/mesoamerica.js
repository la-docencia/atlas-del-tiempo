/* Ruta modelo: contenido derivado de la ficha y sus fuentes, sin dependencias externas. */
(() => {
  const safe = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  let geographicData;
  const loadMap = () => geographicData ??= fetch('/data/states.geojson').then(r => {if (!r.ok) throw Error('map'); return r.json();}).catch(e => {geographicData=null;throw e;});
  const point = ([lon,lat]) => [(lon+118.5)*23,(33.5-lat)*25];
  function outline(geometry) {
    const polygons=geometry.type==='Polygon'?[geometry.coordinates]:geometry.coordinates;
    return polygons.map(p=>p.map(r=>r.map((c,i)=>{const [x,y]=point(c);return `${i?'L':'M'}${x.toFixed(2)},${y.toFixed(2)}`;}).join('')+'Z').join('')).join('');
  }
  async function fillMap(host,topic) {
    if (!host) return;
    host.innerHTML='<p role="status">Cargando mapa de los tres sitios…</p>';
    try {
      const geo=await loadMap();if (!host.isConnected) return;
      host.innerHTML=`<div class="lesson-map-layout"><svg viewBox="330 260 355 245" class="lesson-map" role="img" aria-label="Teotihuacan, Monte Albán y Palenque en el centro y sureste del México actual"><title>Tres ciudades mesoamericanas</title>${geo.features.map(f=>`<path d="${outline(f.geometry)}" fill="#dfcdb0" stroke="#fffaf1" stroke-width="0.7"/>`).join('')}${topic.places.map((p,i)=>{const [x,y]=point([p.lon,p.lat]);return `<g class="lesson-marker" data-marker="${i}"><circle cx="${x}" cy="${y}" r="8" fill="#162b2f"/><text x="${x}" y="${y+3}" text-anchor="middle" fill="white" font-size="9" font-family="sans-serif">${i+1}</text></g>`;}).join('')}</svg><div><div class="place-controls" aria-label="Selecciona un lugar">${topic.places.map((p,i)=>`<button type="button" data-place="${i}" aria-pressed="${i===0}"><span>${i+1}</span>${safe(p.name)}</button>`).join('')}</div><div class="place-reading" aria-live="polite"></div></div></div><p class="map-caption">Límites actuales simplificados para orientarnos. Mesoamérica también abarcó territorios fuera del México actual; este mapa no delimita la región cultural. <a href="https://github.com/strotgen/mexico-leaflet" target="_blank" rel="noopener">Cartografía de referencia</a>.</p>`;
      function select(i) {const p=topic.places[i];host.querySelectorAll('[data-place]').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.place===i)));host.querySelectorAll('[data-marker]').forEach(g=>g.classList.toggle('selected',+g.dataset.marker===i));host.querySelector('.place-reading').innerHTML=`<h3>${safe(p.name)}</h3><p>${safe(p.note)}</p><p class="muted">${safe(p.state)} · ubicación actual</p><a href="https://www.openstreetmap.org/?mlat=${p.lat}&mlon=${p.lon}#map=11/${p.lat}/${p.lon}" target="_blank" rel="noopener">Ampliar ubicación en OpenStreetMap</a>`;}
      host.querySelectorAll('[data-place]').forEach(b=>b.onclick=()=>select(+b.dataset.place));select(0);
    } catch {host.innerHTML='<p>No se pudo cargar el mapa.</p><button type="button" class="ghost-btn">Volver a intentar</button>';host.querySelector('button').onclick=()=>fillMap(host,topic);}
  }
  function illustration() {return '<figure class="meso-illustration"><img src="/assets/mesoamerica-classroom.webp" width="1536" height="1024" alt="Interpretación artística de ciudades mesoamericanas en tres escenas a lápiz" loading="lazy"><figcaption>Ilustración generada con IA, inspirada en Teotihuacan, Monte Albán y Palenque. No es una reconstrucción arqueológica ni una fuente histórica.</figcaption></figure>';}
  const promptNotes=[
    'Antes de leer, pide que separen lo que observan de lo que imaginan. La ilustración permite iniciar preguntas; no sirve para comprobar cómo era una ciudad.',
    'Pide localizar el centro y el sureste. Recuerda que los límites estatales del mapa no existían en estas épocas.',
    'Pregunta: ¿una semejanza en los edificios demuestra que todas las personas hablaban la misma lengua? ¿Qué otra evidencia necesitaríamos?',
    'Lee “c.” como aproximadamente. Explica que esta secuencia reúne momentos distintos y no muestra intervalos a escala.',
    'Da tiempo para responder antes de revelar la explicación. Pide justificar con una fuente, no solamente elegir una opción.',
    'Revisa si la comparación usa un lugar y una evidencia. La pregunta abierta puede ser parte de una buena respuesta.'
  ];
  function present(topic,opener) {
    document.querySelector('#mesoPresenter')?.remove();
    const dialog=document.createElement('dialog');dialog.id='mesoPresenter';dialog.className='lesson-presenter';dialog.setAttribute('aria-labelledby','lessonTitle');
    dialog.innerHTML='<div class="lesson-toolbar"><span>Mesoamérica · para el aula</span><button type="button" class="ghost-btn" data-close>Cerrar presentación</button></div><div class="lesson-stage" tabindex="-1"></div><div class="lesson-bottom"><button type="button" class="ghost-btn" data-prev>Anterior</button><span data-count aria-live="polite"></span><button type="button" class="btn btn-primary" data-next>Siguiente</button></div>';
    document.body.append(dialog);let index=0;const stage=dialog.querySelector('.lesson-stage');
    const slides=[
      {title:'Observa antes de explicar',body:`<div class="observation-layout">${illustration()}<div><p class="lesson-big">¿Qué puedes observar? ¿Qué tendrías que investigar?</p><p>Separa una descripción de una suposición.</p></div></div>`},
      {title:'Tres lugares, historias distintas',body:'<p class="lesson-big">Ubica Teotihuacan, Monte Albán y Palenque.</p><div data-lesson-map></div>'},
      {title:'Una región cultural diversa',body:`<p class="lesson-big">Compartir prácticas no significa ser una sola sociedad.</p><div class="lesson-comparison">${topic.people.map(([n,d])=>`<article><h3>${safe(n)}</h3><p>${safe(d)}</p></article>`).join('')}</div><p>¿Qué evidencia nos ayudaría a comparar dos ciudades?</p>`},
      {title:'No todo ocurrió al mismo tiempo',body:`<ol class="lesson-dates">${topic.dates.map(([date,description])=>`<li><strong>${safe(date)}</strong><span>${safe(description)}</span></li>`).join('')}</ol><p class="muted">Secuencia de referencia, sin escala proporcional. “c.” significa aproximadamente.</p>`},
      {title:'El nombre también tiene historia',body:`<p class="lesson-big">¿Los mexicas construyeron Teotihuacan?</p><button type="button" class="btn btn-primary" data-reveal>Mostrar explicación</button><div class="lesson-answer" hidden><p>No. Su nombre conocido es de origen náhuatl y fue usado por los mexicas después del apogeo de la ciudad.</p><p>El nombre actual de un lugar no identifica necesariamente a sus constructores.</p><a href="${safe(topic.sources[0][1])}" target="_blank" rel="noopener">Consultar la explicación del INAH</a></div>`},
      {title:'Compara, explica y pregunta',body:'<ol class="lesson-task"><li>Elige dos ciudades y ubícalas.</li><li>Describe una semejanza o diferencia apoyada en una fuente.</li><li>Escribe una pregunta que todavía no puedas responder.</li></ol><p class="lesson-big">Para cerrar: ¿por qué Mesoamérica no fue una sola civilización?</p><a class="text-link" href="/downloads/mesoamerica.pdf" download>Descargar la guía y la hoja de trabajo</a>'}
    ];
    function draw() {const s=slides[index];stage.innerHTML=`<p class="eyebrow">RECORRIDO PARA CLASE</p><h2 id="lessonTitle">${s.title}</h2>${s.body}<details class="teacher-note"><summary>Notas para el docente</summary><p>${promptNotes[index]}</p></details>`;dialog.querySelector('[data-count]').textContent=`${index+1} de ${slides.length}`;dialog.querySelector('[data-prev]').disabled=index===0;dialog.querySelector('[data-next]').textContent=index===slides.length-1?'Terminar':'Siguiente';stage.querySelector('[data-reveal]')?.addEventListener('click',e=>{stage.querySelector('.lesson-answer').hidden=false;e.currentTarget.hidden=true});fillMap(stage.querySelector('[data-lesson-map]'),topic);stage.scrollTop=0;stage.focus();}
    function close(){dialog.close();}dialog.querySelector('[data-close]').onclick=close;dialog.querySelector('[data-prev]').onclick=()=>{if(index>0){index--;draw();}};dialog.querySelector('[data-next]').onclick=()=>{if(index<slides.length-1){index++;draw();}else close();};
    dialog.addEventListener('keydown',e=>{if(e.target.matches('input,select,textarea,summary,a,button'))return;if(e.key==='ArrowRight'&&index<slides.length-1){e.preventDefault();index++;draw();}if(e.key==='ArrowLeft'&&index>0){e.preventDefault();index--;draw();}});
    dialog.addEventListener('close',()=>{document.body.classList.remove('presenting');dialog.remove();if(opener.isConnected)opener.focus();});
    document.body.classList.add('presenting');dialog.showModal();draw();
  }
  window.AtlasMesoamerica={install(topic) {
    const heading=document.querySelector('#ruta .route-heading');const panel=document.querySelector('#ruta [data-view="0"]');if(!heading||!panel)return;
    heading.classList.add('meso-heading');heading.querySelector('.actions').insertAdjacentHTML('afterbegin','<button type="button" class="btn btn-primary" id="presentMeso">Presentar en clase</button>');
    const lead=document.createElement('div');lead.className='meso-intro';lead.innerHTML=`${illustration()}<div class="meso-intro-copy"><p class="eyebrow">OBSERVA · UBICA · COMPARA</p><h2>Tres ciudades para empezar a preguntar</h2><p>Recorre seis momentos con tu grupo. Usa la imagen para observar, el mapa para ubicar y las fuentes para comprobar.</p><p class="muted">La ficha completa, la actividad y el juego siguen disponibles en las pestañas.</p></div>`;heading.after(lead);
    const placeArticle=[...panel.querySelectorAll('article')].find(a=>a.querySelector('h2')?.textContent==='Lugares de esta historia');if(placeArticle){placeArticle.classList.add('integrated-map');placeArticle.innerHTML='<h2>Ubica las ciudades</h2><div data-route-map></div>';fillMap(placeArticle.querySelector('[data-route-map]'),topic);}
    document.querySelector('#presentMeso').onclick=e=>present(topic,e.currentTarget);
  }};
  window.addEventListener('hashchange',()=>document.querySelector('#mesoPresenter')?.close());
})();
