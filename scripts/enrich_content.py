import json
from pathlib import Path
D=Path('dist/data')
chapters=json.loads((D/'chapters.json').read_text());topics=json.loads((D/'topics.json').read_text())
q={
'mesoamerica':[
['¿Qué significa «c.» delante de una fecha?',['Aproximadamente','Exactamente','Después de Cristo'],0,'Las fechas aproximadas reconocen límites y convenciones de la cronología.'],
['¿Qué lugar de esta ruta está en los Valles Centrales de Oaxaca?',['Monte Albán','Palenque','Teotihuacan'],0,'Monte Albán permite estudiar una trayectoria regional zapoteca.'],
['¿Qué ayudan a investigar las inscripciones de Palenque?',['Gobernantes y vida ritual','El pensamiento de cada habitante por igual','La historia completa de todas las ciudades mayas'],0,'Una inscripción aporta información, pero tiene una perspectiva y un contexto.'],
['¿Qué muestra Tlailotlacan en Teotihuacan?',['Vínculos con población de origen zapoteco','Que todos los habitantes eran mexicas','Que no hubo movilidad entre regiones'],0,'La arqueología del barrio ayuda a estudiar contactos y diversidad urbana.'],
['¿Qué ocurrió en Palenque en 1952?',['Se localizó la tumba de Pakal','Se fundó la ciudad','Se construyó el Templo de las Inscripciones'],0,'Alberto Ruz L’Huillier realizó el hallazgo; descubrimiento y construcción no son la misma fecha.']],
'independencia':[
['¿Qué relación tiene 1808 con la Independencia?',['Abrió una crisis de autoridad y representación','Fue el año de la Constitución de Apatzingán','Fue la entrada trigarante en la capital'],0,'La crisis de la monarquía española abrió debates en Nueva España.'],
['¿Dónde emitió Hidalgo el bando del 6 de diciembre de 1810?',['Guadalajara','Chilpancingo','Iguala'],0,'El bando de Guadalajara permite estudiar la demanda de abolición de la esclavitud.'],
['¿Qué lugar conecta la trayectoria de Hidalgo con el norte?',['Chihuahua','Querétaro','Cuautla'],0,'Fue llevado preso a Chihuahua y ejecutado allí en 1811.'],
['¿Cuál de estos documentos corresponde a 1814?',['Constitución de Apatzingán','Plan de Iguala','Plan de Ayala'],0,'El Congreso insurgente promulgó el Decreto Constitucional el 22 de octubre de 1814.'],
['¿Qué forma de gobierno proponía el Plan de Iguala?',['Monarquía','República federal de 1824','Gobierno municipal sin autoridad nacional'],0,'No debe confundirse el programa de 1821 con la organización republicana posterior.']],
'revolucion':[
['¿Qué ciudad fue decisiva en la fase maderista de mayo de 1911?',['Ciudad Juárez','Aguascalientes','Querétaro'],0,'Su toma y los acuerdos de mayo ayudaron a abrir la transición política.'],
['¿Qué documento expresó demandas agrarias zapatistas?',['Plan de Ayala','Plan de Iguala','Constitución de Apatzingán'],0,'Se proclamó el 28 de noviembre de 1911.'],
['¿Qué acontecimiento corresponde a 1913?',['Golpe contra Madero','Congreso de Chilpancingo','Promulgación de la Constitución de 1917'],0,'La ruptura abrió una nueva fase de lucha contra Huerta.'],
['¿Para qué se reunió la Convención revolucionaria?',['Buscar acuerdos entre fuerzas','Promulgar el Plan de Iguala','Restaurar el gobierno virreinal'],0,'La Convención de 1914 intentó resolver diferencias sobre el futuro gobierno.'],
['¿Dónde sesionó el Constituyente de 1916–1917?',['Querétaro','Dolores','Apatzingán'],0,'La elaboración constitucional ocurrió en Querétaro.']],
'nacion':[
['¿Qué forma de gobierno existió antes de la república federal?',['Primer Imperio','Virreinato independiente','Segundo Imperio'],0,'La experiencia imperial de Iturbide antecedió a la Constitución federal de 1824.'],
['¿Qué distingue a una federación?',['Distribuye facultades dentro de un orden común','Cada entidad se convierte en país independiente','Todas las decisiones corresponden al municipio'],0,'Federalismo implica distribución de competencias, no desaparición de la autoridad nacional.'],
['¿Qué orientación tuvieron las Siete Leyes de 1836?',['Centralista','Federal como la de 1824','Ausencia de organización nacional'],0,'Reorganizaron el país en departamentos.'],
['¿Con qué proceso se relaciona el movimiento de Ayutla?',['Oposición a Santa Anna y apertura de reformas','Inicio de la insurgencia de Hidalgo','Redacción del Plan de Ayala'],0,'El movimiento de 1854–1855 abrió una nueva etapa política.'],
['¿Qué recinto de Chihuahua alojó al gobierno republicano?',['Casa de Juárez','Paquimé','Teatro de la República'],0,'Alojaba al Ejecutivo durante parte de su desplazamiento por la intervención francesa.']],
'antigua':[
['¿En qué material se hicieron registros tempranos de Uruk?',['Arcilla','Papel industrial','Pergamino impreso'],0,'Las tablillas permiten investigar actividades administrativas.'],
['¿Qué río se relaciona con el papiro de Egipto?',['Nilo','Tigris','Éufrates'],0,'El papiro permite relacionar entorno, materiales y trabajo.'],
['¿Qué revela mejor un inventario de bienes?',['Qué se registró y administró','Lo que pensaban todos los habitantes','Todos los conflictos de una ciudad'],0,'Una fuente responde algunas preguntas y deja otras abiertas.'],
['¿Qué relación tiene Teseo con Atenas?',['Es un personaje de su tradición mítica','Fue un escriba documentado de Uruk','Construyó las primeras pirámides de Egipto'],0,'El mito puede investigarse como expresión cultural y política.'],
['¿Qué permite afirmar un objeto de procedencia distante?',['Que hubo circulación; su mecanismo requiere estudio','Que ocurrió necesariamente una conquista','Que ambos lugares tenían la misma lengua'],0,'El comercio, el regalo y otros mecanismos pueden producir circulación de objetos.']]
}
for t in topics:
 for item in q[t['id']]:
  if not any(x[0]==item[0] for x in t['quiz']):t['quiz'].append(item)
 if t['id']=='antigua':
  t['sources'].append(['British Museum · Atenas en el siglo V a. C.','https://www.britishmuseum.org/blog/historical-city-travel-guide-athens-5th-century-bc','Contexto de ciudadanía, trabajo y vida urbana'])
for c in chapters:
 if c['id']=='antigua-7':c['source']=['British Museum · Atenas en el siglo V a. C.','https://www.britishmuseum.org/blog/historical-city-travel-guide-athens-5th-century-bc']
 c['timeline']=c['id'] not in ['antigua-4','antigua-5']
 # The number is only a sorting aid, never a claim of an exact date for broad topics.
 if c['id']=='revolucion-10':c['year']=1917.1
pairs={
'independencia':[
 ['Sí: ambas propuestas exigían una separación total.','Autonomía era únicamente cambiar impuestos, sin discutir gobierno.'],
 ['Todos seguían un programa idéntico desde 1810.','Solo importaban las decisiones del dirigente principal.'],
 ['El bando basta para probar su cumplimiento en todo el territorio.','Solo una conmemoración actual permitiría comprobarlo.'],
 ['Siempre termina cuando muere su primer dirigente.','Las demandas sociales no influyen en su continuidad.'],
 ['Porque todas sus propuestas coinciden con los derechos actuales.','Porque los puntos que hoy resultan extraños deben eliminarse.'],
 ['No: solo cuentan las leyes que se aplicaron sin obstáculos.','Sí: su importancia prueba que se aplicó en todas partes.'],
 ['Sí: un acuerdo demuestra que sus proyectos son idénticos.','No: por eso ningún acuerdo puede tener efectos políticos.'],
 ['Sí: independencia y fin de la desigualdad suceden juntos.','Sí: la entrada en la capital resolvió todos los conflictos.']],
'nacion':[
 ['Sí: el federalismo empezó el mismo día de la consumación.','No: el virreinato siguió siendo la forma de gobierno.'],
 ['Una federación elimina toda autoridad nacional.','Federarse significa que cada entidad tiene soberanía internacional propia.'],
 ['Sí: las facultades territoriales no cambiaron.','Solo cambió la ubicación geográfica de las capitales.'],
 ['Sí: los hechos ocurrieron porque no había otras alternativas.','Sí: conocer el desenlace elimina la necesidad de explicar decisiones.'],
 ['Porque toda norma elimina inmediatamente la oposición.','Porque una ley nunca afecta intereses ni instituciones.'],
 ['Nada: los nombres de los bandos explican todas las experiencias.','Solo los uniformes; los efectos sociales son ajenos a la historia.'],
 ['No: un gobierno deja de existir si se desplaza.','Sí: el traslado demuestra que se creó otro país.'],
 ['Porque ningún cambio político tiene consecuencias.','Porque las leyes nunca influyen en la sociedad.']],
'mesoamerica':[
 ['Sí: los periodos comienzan en un día exacto para todas las regiones.','Sí: todas las aldeas se convirtieron en ciudades al mismo tiempo.'],
 ['Sí: todas sus construcciones pertenecen al momento de fundación.','Sí: los edificios siempre conservaron el mismo uso.'],
 ['Sí: compartir ciudad implica compartir origen y lengua.','No: por eso no había relaciones entre sus barrios.'],
 ['Nadie: el texto representa por igual a todos los habitantes.','Solo los gobernantes, porque nunca aparecían en monumentos.'],
 ['Sí: los edificios abandonados prueban la desaparición de todo un pueblo.','Sí: perder poder político equivale a perder toda continuidad cultural.'],
 ['Sí: quienes dieron el nombre actual siempre construyeron el lugar.','Sí: los nombres se conservaron sin cambios desde la fundación.'],
 ['Nada, porque solo importa el valor estético del objeto.','Únicamente su precio; la ubicación no aporta información.'],
 ['Porque las comunidades permanecen sin cambios desde la antigüedad.','Porque los objetos antiguos explican por completo la vida actual.']],
'antigua':[
 ['Solo monumentos: el abastecimiento era automático.','Únicamente defensas, porque no existían intercambios.'],
 ['Sí: todos los aspectos de la vida quedan en la contabilidad.','Sí: registrar bienes implica conocer todas las voces.'],
 ['Sí: únicamente la guerra hace viajar objetos.','Sí: un objeto basta para demostrar una misma forma de gobierno.'],
 ['Sí: un río produce siempre la misma sociedad.','No: por eso los recursos naturales no influyen en las actividades.'],
 ['Son iguales: observar un rasgo demuestra cualquier significado.','Interpretar es decidir sin contrastar evidencias.'],
 ['Sí: únicamente interesan los relatos que ocurrieron literalmente.','No: por eso todo lo narrado debe aceptarse como hecho.'],
 ['Sí: toda democracia tiene las mismas reglas de participación.','Sí: una palabra conserva siempre el mismo significado histórico.'],
 ['Sí: investigar exige presentar todas las respuestas como definitivas.','Sí: las dudas deben ocultarse en la explicación final.']],
'revolucion':[
 ['Sí: ambas demandas pedían exactamente la misma reforma.','No: por eso no podían coexistir dentro del movimiento.'],
 ['Solo por su tamaño; sus conexiones no importan.','Porque todas las ciudades fronterizas deciden cualquier guerra.'],
 ['Sí: cualquier cambio presidencial modifica toda la propiedad.','Sí: una demanda desaparece con la renuncia de un gobernante.'],
 ['Porque haber compartido enemigo exige pensar igual para siempre.','Porque los proyectos políticos no influyen después de una victoria.'],
 ['Sí: los territorios controlados nunca cambiaron.','Sí: las fronteras estatales actuales muestran exactamente los frentes.'],
 ['Solo elegir una fecha; los proyectos distintos no importan.','Nada: vencer a un enemigo común produce acuerdo permanente.'],
 ['Solo una pintura actual, sin conocer su autoría.','Solo el nombre de un general, sin otras evidencias.'],
 ['Sí: el Congreso solo copia la voluntad de una persona.','Sí: las demandas sociales no influyen en su redacción.'],
 ['No hay diferencia: toda ley se cumple desde su publicación.','Solo es necesario leer una conmemoración actual.'],
 ['Sí: existe una sola fecha válida para cualquier pregunta.','Sí: las consecuencias de una revolución ocurren todas juntas.']]
}
for route,pp in pairs.items():
 for c,p in zip([c for c in chapters if c['route']==route],pp):c['distractors']=p
(D/'chapters.json').write_text(json.dumps(chapters,ensure_ascii=False,indent=2));(D/'topics.json').write_text(json.dumps(topics,ensure_ascii=False,indent=2))
places=json.loads((D/'heritage.json').read_text())
# New editorial entries: exact official sources, locality rather than unverified street coordinates.
new=[
('casa-juarez',8,'Chihuahua','Museo de la Lealtad Republicana · Casa de Juárez','Chihuahua','Siglo XIX','Museo histórico','El edificio alojó al Poder Ejecutivo federal y a Benito Juárez entre 1864 y 1866 durante parte del desplazamiento del gobierno republicano. Permite estudiar la intervención francesa desde el norte.','La relación entre espacios de gobierno, memoria del edificio y el relato museográfico.','¿Cómo cambia nuestra idea de capital al estudiar un gobierno itinerante?','Traza una ruta de desplazamiento republicano con fechas de una fuente; distingue el inmueble histórico y la museografía posterior.','https://www.chihuahua.gob.mx/prensa/reabre-sus-puertas-el-museo-de-la-lealtad-republicana-casa-de-juarez','Gobierno del Estado de Chihuahua','nacion'),
('casa-chihuahua',8,'Chihuahua','Casa Chihuahua · Calabozo de Hidalgo','Chihuahua','Independencia · 1811','Sitio de memoria','El museo de sitio explica el cautiverio de Hidalgo en Chihuahua. Vincula su trayectoria con las instituciones y espacios en los que fue procesado, y permite preguntar cómo se construye la memoria de la Independencia.','El calabozo, las referencias documentales y la diferencia entre objetos originales, facsímiles y ambientaciones.','¿Qué puede probar un espacio conservado y qué requiere documentos?','Haz dos columnas: evidencia material y evidencia escrita. Relaciona ambas con una pregunta sobre 1811.','https://www.casachihuahua.org.mx/Movil/casa_sitio_sala_ii.php','Casa Chihuahua Centro de Patrimonio Cultural','independencia'),
('cueva-olla',8,'Chihuahua','Cueva de la Olla','Casas Grandes','Prehispánico','Sitio arqueológico','En un abrigo del Valle de las Cuevas se conserva un granero de forma redondeada que da nombre al sitio. Ayuda a estudiar almacenamiento, alimentación y adaptación al entorno en sociedades del norte.','La forma del granero y su relación con el abrigo natural, sin tocar ni entrar en estructuras restringidas.','¿Qué revela almacenar alimentos sobre la organización de una comunidad?','Dibuja un esquema del almacenamiento e indica cuáles partes observaste y cuáles son hipótesis.','https://www.inah.gob.mx/zonas/zona-arqueologica-cueva-de-la-olla','INAH',None),
('mitla',20,'Oaxaca','Mitla','San Pablo Villa de Mitla','Prehispánico y comunidad actual','Sitio arqueológico','Los conjuntos de Mitla permiten observar arquitectura y ornamentación de tradición zapoteca. La zona arqueológica forma parte de una población viva: estudiar sus edificios no equivale a presentar a sus habitantes actuales como pasado.','Grecas, patios y relación entre vestigios y población actual.','¿Cómo conviven patrimonio arqueológico y vida cotidiana?','Describe un patrón geométrico y redacta una pregunta sobre su uso sin asignarle un significado que no hayas verificado.','https://lugares.inah.gob.mx/es/node/4350','INAH','mesoamerica'),
('cholula',21,'Puebla','Zona arqueológica de Cholula','Cholula','Prehispánico y periodo virreinal','Sitio arqueológico','La Gran Pirámide y sus áreas asociadas muestran una larga historia constructiva. El paisaje de Cholula permite plantear preguntas sobre cambios de uso y superposición de espacios a lo largo del tiempo.','Etapas de construcción descritas por el museo y relaciones entre edificios de distintas épocas.','¿Por qué no debemos asignar un solo año a todo un conjunto?','Construye una secuencia de usos apoyada en cédulas o la ficha institucional. No supongas que el acceso a túneles está habilitado.','https://www.inah.gob.mx/zonas/zona-arqueologica-de-cholula','INAH','mesoamerica'),
('calakmul',4,'Campeche','Calakmul','Calakmul','Maya · periodo Clásico','Sitio arqueológico','Calakmul fue un importante centro urbano maya. Sus conjuntos de plazas, grandes estructuras y calzadas permiten investigar organización espacial y relaciones políticas dentro del mundo maya.','La organización de los conjuntos alrededor de plazas y su relación con el paisaje.','¿Qué información ofrece un plano que no se observa desde un solo edificio?','Compara un plano de Calakmul y uno de Palenque. Registra semejanzas sin concluir que tenían un gobierno idéntico.','https://lugares.inah.gob.mx/es/node/4376','INAH','mesoamerica'),
('chichen-itza',31,'Yucatán','Chichén Itzá','Tinum','Clásico tardío y Posclásico','Sitio arqueológico','Chichén Itzá conserva conjuntos de funciones diversas, incluyendo áreas residenciales de élite. Mirar más allá del edificio más conocido ayuda a estudiar cómo se organizaba una ciudad y cómo cambió con el tiempo.','Diferencias entre espacios residenciales, plazas y edificios ceremoniales en la información institucional.','¿Una pirámide basta para explicar toda la ciudad?','Elige tres tipos de espacio en un plano y formula una pregunta distinta para cada uno.','https://lugares.inah.gob.mx/es/node/4335','INAH','mesoamerica'),
('virreinato',15,'México','Museo Nacional del Virreinato','Tepotzotlán','Periodo virreinal','Museo histórico','El museo ocupa un antiguo conjunto jesuita en Tepotzotlán y conserva colecciones de arte e historia novohispanos. El edificio y las piezas permiten estudiar instituciones, prácticas y cambios en los usos de un inmueble.','Materiales, autoría y uso de una pieza; distingue el origen del objeto y su ingreso al museo.','¿La fecha del edificio es la misma que la del museo?','Elabora una ficha con fecha de producción, función original y pregunta de investigación para un objeto.','https://lugares.inah.gob.mx/es/node/4239','INAH','independencia'),
('casa-hidalgo',11,'Guanajuato','Museo Ex Curato de Dolores · Casa de Hidalgo','Dolores Hidalgo','Independencia','Museo histórico','El recinto presenta distintas facetas de Hidalgo y su transformación de párroco en dirigente insurgente. La museografía combina piezas, documentos y ambientaciones que deben identificarse al observar.','Cédulas de originales y facsímiles, y distintas dimensiones de la vida de Hidalgo.','¿Cómo distinguir una ambientación de un documento original?','Registra el tipo de tres piezas y explica qué pregunta responde cada una.','https://lugares.inah.gob.mx/es/node/4520','INAH','independencia'),
('constituciones',9,'Ciudad de México','Museo de las Constituciones','Centro Histórico, Ciudad de México','Siglo XIX e historia constitucional','Museo histórico','El antiguo templo de San Pedro y San Pablo fue recinto de debates fundacionales del Estado mexicano. El museo de la UNAM permite relacionar ese espacio con el estudio de constituciones, derechos y formas de gobierno.','El vínculo entre edificio, asamblea y documentos constitucionales.','¿Qué diferencia existe entre el lugar donde se debate una ley y el territorio donde se aplica?','Compara dos disposiciones constitucionales y redacta una pregunta sobre su aplicación histórica.','https://museodelasconstituciones.unam.mx/exposicion-fundar/','UNAM','nacion')]
for row in new:
 id,code,state,name,loc,period,kind,history,observe,question,activity,url,inst,route=row
 if any(p['id']==id for p in places):continue
 places.append(dict(id=id,stateCode=code,state=state,name=name,location=loc,period=period,kind=kind,history=history,observe=observe,question=question,activity=activity,source=url,visitorSource=url,institution=inst,route=route,reviewed='2026-09-29'))
(D/'heritage.json').write_text(json.dumps(places,ensure_ascii=False,indent=2))
print('Routes',len(topics),'Quiz',sum(len(t['quiz']) for t in topics),'Scenes',len(chapters),'Timeline',sum(c['timeline'] for c in chapters),'Places',len(places),'Chihuahua',sum(p['stateCode']==8 for p in places))
