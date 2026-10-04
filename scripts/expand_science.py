"""Contenido editorial de Atlas: Tierra y Espacio. Regenera science.json."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=[]
def add(id,area,title,tag,summary,reading,deep,activity,source,questions):
 items.append(dict(id=id,area=area,title=title,tag=tag,summary=summary,reading=reading.split('|'),deep=deep,activity=activity,source=source,quiz=questions,minutes=5+len(reading.split())//80))
add('sistema-solar','espacio','Nuestro sistema solar','Empieza aquí','Una estrella, ocho planetas y muchos mundos por descubrir.',
'El Sol es la estrella de nuestro sistema. Su gravedad mantiene unidos planetas, lunas y numerosos cuerpos menores. Los planetas, en orden desde el Sol, son Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano y Neptuno.|Los cuatro primeros son rocosos. Júpiter y Saturno son gigantes gaseosos; Urano y Neptuno se clasifican como gigantes helados. El sistema también incluye planetas enanos, asteroides y cometas.',
'Los dibujos escolares suelen comprimir las distancias y aumentar el tamaño de los planetas. Una unidad astronómica (UA) equivale aproximadamente a la distancia media entre la Tierra y el Sol. En el laboratorio puedes comparar estas distancias sin confundirlas con tamaños.',
'Escribe los ocho planetas en orden. Después predice qué espacio necesitarías si la Tierra estuviera a un metro del Sol y compruébalo en el laboratorio.',
['NASA · Sistema solar','https://science.nasa.gov/solar-system/solar-system-facts/'],
[['¿Cuál es la estrella de nuestro sistema?',['El Sol','La Luna','Júpiter'],0,'El Sol es una estrella; los planetas orbitan a su alrededor.'],['¿Qué representa una UA?',['El diámetro terrestre','La distancia media Tierra-Sol','Un año de tiempo'],1,'La UA es una unidad de distancia.']])
add('planetas','espacio','Ocho planetas, muchas diferencias','Comparar mundos','Tamaño, distancia y composición cuentan historias distintas.',
'Júpiter es el planeta de mayor tamaño. Mercurio es el más pequeño y el más cercano al Sol; Neptuno es el más lejano de los ocho planetas. Ser grande y estar lejos son propiedades diferentes.|Las distancias al Sol cambian mientras los planetas recorren sus órbitas. Para compararlos usamos valores medios aproximados. No equivalen a la distancia desde la Tierra, que también se mueve.',
'Un diámetro mide de un extremo al otro pasando por el centro. El volumen mide espacio ocupado y crece con el cubo del diámetro: duplicar el diámetro de una esfera multiplica su volumen por ocho. El comparador distingue diámetro y distancia.',
'Compara Tierra, Júpiter y Neptuno. Encuentra un planeta más grande que otro, pero más cercano al Sol.',
['NASA · Tamaños y distancias','https://science.nasa.gov/solar-system/planet-sizes-and-locations-in-our-solar-system/'],
[['¿Cuál es el planeta más grande?',['Neptuno','Júpiter','La Tierra'],1,'Júpiter tiene el mayor diámetro planetario del sistema solar.'],['La distancia media al Sol es…',['Igual a la distancia a la Tierra','Una referencia aproximada de la órbita','El diámetro del planeta'],1,'Los planetas se mueven: la distancia entre dos planetas varía.']])
add('sol','espacio','El Sol: nuestra estrella','Energía','La luz que sostiene la vida tiene su origen en una estrella.',
'El Sol es una esfera de plasma: materia muy caliente con partículas cargadas. En su núcleo, la fusión transforma hidrógeno en helio y libera energía. No arde como una fogata.|La luz solar tarda unos ocho minutos en llegar a la Tierra. Esa energía impulsa la fotosíntesis y participa en el clima y el ciclo del agua.',
'La superficie visible del Sol se llama fotosfera. Sobre ella hay otras capas, incluida la corona. Las manchas y erupciones muestran actividad magnética. Nunca mires directamente al Sol ni lo observes con binoculares o telescopio sin equipo solar adecuado y supervisión especializada.',
'Haz una cadena de conexiones: Sol, planta, alimento, persona. Explica cómo viaja la energía. Para observar, utiliza fotografías científicas.',
['NASA · Datos del Sol','https://science.nasa.gov/sun/facts/'],
[['¿De dónde procede la energía solar?',['De quemar madera','De la fusión nuclear','Del reflejo de la Tierra'],1,'En el núcleo solar ocurre fusión nuclear.'],['¿La luz solar llega instantáneamente?',['Sí','No, tarda unos ocho minutos','Tarda un año'],1,'La luz viaja muy rápido, pero tarda en recorrer la distancia Tierra-Sol.']])
add('luna-eclipses','espacio','La Luna y los eclipses','Mirar el cielo','Alineaciones que producen sombras, no magia.',
'Un eclipse solar ocurre cuando la Luna pasa entre el Sol y la Tierra y su sombra alcanza nuestro planeta. En un eclipse lunar, la Tierra queda entre el Sol y la Luna y proyecta su sombra sobre ella.|No hay un eclipse cada mes: la órbita lunar está inclinada respecto al plano de la órbita terrestre. Las alineaciones necesarias solo ocurren en ciertas ocasiones.',
'Las fases habituales muestran distintas porciones de la mitad lunar iluminada por el Sol; no son la sombra de la Tierra. Esa sombra interviene en los eclipses lunares. La Luna puede verse de día. Nunca observes el Sol directamente: utiliza recursos de observación solar segura de NASA.',
'Con una lámpara y dos pelotas, representa ambas alineaciones. Dibuja qué cuerpo queda en medio en cada eclipse. No uses el Sol real para esta actividad.',
['NASA · Geometría de eclipses','https://science.nasa.gov/eclipses/geometry/'],
[['En un eclipse solar, ¿qué cuerpo queda en medio?',['La Tierra','La Luna','Marte'],1,'La Luna se coloca entre el Sol y la Tierra.'],['¿Por qué no hay eclipses cada mes?',['La órbita lunar está inclinada','El Sol se apaga','La Luna deja de moverse'],0,'La inclinación evita que las sombras coincidan en cada vuelta.']])
add('orbitas','espacio','Gravedad y órbitas','Cómo se mueven','Orbitar es caer continuamente alrededor de un mundo.',
'La gravedad atrae a los cuerpos con masa. Un satélite en órbita no está fuera de su alcance: avanza mientras cae hacia la Tierra. Con la velocidad y trayectoria adecuadas, su caída sigue la curvatura del planeta.|Los astronautas flotan porque ellos y su nave están en caída libre juntos. Esto produce microgravedad, no la desaparición de la gravedad.',
'Una órbita combina movimiento y atracción gravitatoria. Cambiar la velocidad de una nave modifica su trayectoria. Las órbitas pueden ser elípticas; el círculo es un caso particular. Los modelos sencillos dejan fuera el rozamiento y la influencia de otros cuerpos.',
'Dibuja una Tierra y una trayectoria orbital. Usa dos flechas: una hacia el centro por la gravedad y otra tangente para el movimiento instantáneo.',
['NASA · Gravedad y mecánica','https://science.nasa.gov/learn/basics-of-space-flight/chapter3-4/'],
[['¿Hay gravedad en una órbita terrestre?',['Sí','No','Solo cuando hay luna llena'],0,'La gravedad curva la trayectoria de la nave.'],['¿Por qué flotan los astronautas en órbita?',['No tienen masa','Están en caída libre con la nave','El aire los empuja hacia arriba'],1,'La nave y sus ocupantes caen juntos alrededor de la Tierra.']])
add('estrellas','espacio','La vida de las estrellas','Más allá del Sol','Las estrellas nacen, cambian y tienen finales diferentes.',
'Las estrellas se forman cuando regiones de gas y polvo se contraen por gravedad. Si el centro alcanza condiciones suficientes, comienza la fusión nuclear. El Sol es una de las estrellas de nuestra galaxia.|La masa inicial influye mucho en su evolución. Las estrellas más masivas consumen rápidamente su combustible. El brillo que vemos también depende de la distancia: una estrella tenue puede estar muy lejos.',
'Una estrella como el Sol terminará como una enana blanca después de desprender sus capas externas. Algunas estrellas muy masivas terminan en explosiones de supernova y dejan estrellas de neutrones o agujeros negros. No todas las estrellas explotan.',
'Escribe dos razones por las que una estrella puede verse menos brillante que otra. Distingue su luminosidad real de su brillo aparente.',
['NASA · Estrellas','https://science.nasa.gov/universe/stars/'],
[['¿El Sol es una estrella?',['Sí','No, es un planeta','No, es una luna'],0,'El Sol produce energía mediante fusión como otras estrellas.'],['¿Todas las estrellas tienen el mismo final?',['Sí','No, su masa influye en su evolución','Solo depende del color del cielo'],1,'La masa condiciona los procesos y el final de la estrella.']])
add('galaxias','espacio','Galaxias y Vía Láctea','Nuestra dirección cósmica','El sistema solar forma parte de una estructura mucho mayor.',
'Una galaxia reúne estrellas, gas, polvo y materia oscura ligados por gravedad. Hay galaxias espirales, elípticas e irregulares. Nuestro sistema solar está en la Vía Láctea.|Una nebulosa es una nube de gas y polvo. Puede ser una región donde nacen estrellas o material expulsado por ellas. No es lo mismo que una galaxia, aunque en fotografías ambas puedan verse difusas.',
'Un año luz mide distancia: es lo que recorre la luz en un año. Al observar objetos lejanos vemos luz emitida en el pasado. Las imágenes de telescopios pueden combinar observaciones y asignar colores a distintas longitudes de onda.',
'Ordena de menor a mayor escala: Tierra, sistema solar, Vía Láctea. Después explica por qué una nebulosa no es necesariamente una galaxia.',
['NASA · Galaxias','https://science.nasa.gov/universe/galaxies/'],
[['¿En qué galaxia está el sistema solar?',['Andrómeda','Vía Láctea','Saturno'],1,'Nuestra galaxia es la Vía Láctea.'],['Un año luz mide…',['Tiempo de vida','Distancia','Temperatura'],1,'Es la distancia que recorre la luz en un año.']])
add('agujeros-negros','espacio','Agujeros negros','Preguntas del universo','Una frontera de la que la luz no puede escapar.',
'Un agujero negro concentra tanta masa que existe una región de la que nada, ni siquiera la luz, puede salir. Su límite se llama horizonte de sucesos. No es una superficie sólida.|Los detectamos por sus efectos: movimiento de estrellas cercanas, gas caliente y ondas gravitacionales. Algunos se forman tras el colapso de estrellas masivas; otros, enormes, están en centros de galaxias.',
'No son aspiradoras cósmicas. Lejos de ellos, su gravedad actúa como la de cualquier cuerpo de la misma masa. No hay evidencia de que funcionen como portales. El interior del horizonte sigue planteando preguntas que la ciencia investiga.',
'Clasifica estas afirmaciones: “se estudian por sus efectos”, “son portales comprobados”. Explica qué evidencia exigirías para aceptar cada una.',
['NASA · Agujeros negros','https://science.nasa.gov/universe/black-holes/'],
[['¿Cómo se llama su frontera?',['Corteza','Horizonte de sucesos','Atmósfera'],1,'Desde el interior del horizonte la luz no puede escapar.'],['¿Son portales demostrados a otros universos?',['Sí','No','Solo los pequeños'],1,'Esa idea pertenece a la ficción; no está comprobada.']])
add('exoplanetas','espacio','Mundos alrededor de otras estrellas','Buscar otros mundos','Encontrar un planeta no equivale a encontrar vida.',
'Los exoplanetas están fuera de nuestro sistema solar. Muchos orbitan otras estrellas y presentan tamaños y composiciones muy variados. Uno de los métodos de detección mide pequeñas disminuciones de brillo cuando un planeta pasa delante de su estrella.|Otro método estudia el movimiento de la estrella por la atracción gravitatoria del planeta. Diferentes técnicas aportan información complementaria.',
'La zona habitable es la región donde podría existir agua líquida superficial bajo condiciones atmosféricas adecuadas. Estar allí no demuestra que un planeta tenga agua ni vida. Hasta ahora, la Tierra es el único mundo con vida confirmada.',
'Representa un tránsito pasando una bolita frente a una linterna. Describe por qué el brillo puede disminuir sin que la estrella se apague.',
['NASA · Exoplanetas','https://science.nasa.gov/exoplanets/facts/'],
[['¿Qué es un exoplaneta?',['Un planeta fuera del sistema solar','Una luna terrestre','Un cometa cercano'],0,'El término se refiere a planetas externos a nuestro sistema.'],['¿Zona habitable significa vida confirmada?',['Sí','No','Siempre que el planeta sea azul'],1,'La habitabilidad potencial no es una detección de vida.']])
add('universo','espacio','Un universo que cambia','Grandes escalas','Qué explica el Big Bang y qué seguimos investigando.',
'El modelo del Big Bang describe la evolución del universo desde un estado muy caliente y denso. La expansión del espacio y la radiación cósmica de fondo son evidencias fundamentales. La edad estimada del universo es de unos 13 800 millones de años.|No se trata de una explosión corriente dentro de un espacio vacío. El propio espacio se expande; las galaxias lejanas permiten estudiar esa historia.',
'Un modelo científico reúne evidencias y hace predicciones comprobables. Aún investigamos cuestiones como la naturaleza de la materia oscura y la energía oscura. “No lo sabemos todavía” es una parte honesta del conocimiento científico.',
'Construye tres tarjetas: observación, explicación y pregunta abierta. Relaciona la radiación de fondo con una observación y el Big Bang con un modelo.',
['NASA · El Big Bang','https://science.nasa.gov/universe/the-big-bang/'],
[['El Big Bang describe…',['La evolución temprana del universo','La formación de una montaña','La caída de un meteorito'],0,'Es un modelo de la evolución del universo desde un estado caliente y denso.'],['¿La ciencia tiene todas las respuestas?',['Sí','No, quedan preguntas abiertas','No utiliza evidencias'],1,'La investigación contrasta modelos con nuevas observaciones.']])
add('exploracion','espacio','Cómo exploramos el espacio','Instrumentos','Telescopios, sondas y preguntas que pueden comprobarse.',
'Los telescopios recogen luz y otras formas de radiación para estudiar objetos lejanos. Las sondas llevan instrumentos hacia otros mundos; algunas sobrevuelan, otras orbitan y otras aterrizan.|Voyager permitió estudiar los planetas exteriores y sus lunas. Una misión obtiene mediciones: imágenes, composición, campos magnéticos o partículas. Las imágenes son datos que necesitan interpretación.',
'Una fotografía no responde todas las preguntas. Para conocer tamaño o distancia hacen falta escalas y mediciones adicionales. Los colores pueden ser naturales, aproximados o asignados para mostrar información invisible al ojo.',
'Diseña una misión en papel. Elige un mundo, una pregunta, un instrumento y el dato que necesitarías recoger para responderla.',
['NASA · Voyager','https://science.nasa.gov/mission/voyager/fact-sheet/'],
[['¿Qué conviene definir primero en una misión científica?',['Una pregunta investigable','El color del uniforme','Un resultado inventado'],0,'La pregunta orienta los instrumentos y las mediciones.'],['¿Todas las imágenes espaciales usan colores como los ve el ojo?',['Sí','No','Solo existen imágenes en blanco y negro'],1,'Algunas asignan colores para representar distintas longitudes de onda.']])
add('tierra','tierra','La Tierra: un sistema conectado','Nuestro planeta','Roca, agua, aire y vida se relacionan continuamente.',
'La Tierra es el tercer planeta desde el Sol. En ella se relacionan la geosfera (rocas), la hidrosfera (agua), la atmósfera (aire) y la biosfera (vida). Un cambio en una parte puede afectar a las demás.|La rotación produce la alternancia de día y noche. La traslación es el recorrido alrededor del Sol. Las estaciones se deben principalmente a la inclinación del eje terrestre mientras orbitamos.',
'Cuando un hemisferio se inclina hacia el Sol recibe luz más directa y días más largos. Por eso las estaciones son opuestas entre hemisferios. No se explican principalmente por acercarnos o alejarnos del Sol.',
'Relaciona una lluvia con las cuatro esferas: aire que transporta humedad, agua que cae, suelo que la recibe y plantas que la aprovechan.',
['NASA · La Tierra','https://science.nasa.gov/earth/facts/'],
[['¿Qué causa el día y la noche?',['La rotación terrestre','Las nubes','Las fases lunares'],0,'Al girar la Tierra, distintos lugares quedan iluminados.'],['¿Qué explica principalmente las estaciones?',['La inclinación del eje y la traslación','La distancia a la Luna','Que el Sol se apague'],0,'La inclinación cambia cómo recibe luz cada hemisferio.']])
add('interior','tierra','Dentro de la Tierra','Geología','Conocer lo que no podemos visitar directamente.',
'La Tierra tiene corteza, manto y núcleo. El núcleo se divide en una parte externa líquida y otra interna sólida. El manto es mayormente sólido, aunque puede deformarse muy lentamente.|Las ondas sísmicas cambian de velocidad y trayectoria al atravesar materiales distintos. Sus registros permiten inferir cómo es el interior. No hemos perforado hasta el centro terrestre.',
'La litosfera incluye la corteza y la parte superior rígida del manto. Está dividida en placas que se desplazan sobre una región del manto capaz de deformarse. Las placas no flotan sobre un océano global de magma.',
'Dibuja un corte de la Tierra y marca las capas. Anota al lado qué evidencia permite estudiarlas: las ondas de los sismos.',
['USGS · Interior de la Tierra','https://pubs.usgs.gov/gip/interior/'],
[['¿El manto es un océano de magma?',['Sí','No, es mayormente sólido','Es aire caliente'],1,'La roca sólida puede deformarse lentamente a altas temperaturas.'],['¿Qué ayuda a estudiar el interior?',['Las ondas sísmicas','Solo fotografías de nubes','Las fases lunares'],0,'Su propagación revela diferencias entre capas.']])
add('montanas','tierra','Montañas y relieve','Paisajes en transformación','Las montañas tienen una historia que sigue escribiéndose.',
'Las montañas pueden formarse por colisión de placas, fallas o acumulación de materiales volcánicos. La convergencia de India y Eurasia contribuyó a levantar el Himalaya. No todas las montañas son volcanes.|El agua, el viento, el hielo y la gravedad desgastan y transportan materiales. El relieve resulta de la interacción entre levantamiento, erosión y sedimentación durante largos periodos.',
'La altura sobre el nivel del mar y la altura desde la base son medidas distintas. También conviene distinguir montaña, cordillera, meseta y valle. Un paisaje conserva pistas de procesos, pero una foto aislada no revela toda su historia.',
'Observa una sierra cercana o una fotografía. Describe pendientes, valles y materiales sin inventar su origen. Formula una pregunta para investigar.',
['USGS · Tectónica de placas','https://www.usgs.gov/publications/dynamic-earth-story-plate-tectonics'],
[['¿Todas las montañas son volcanes?',['Sí','No','Solo en México'],1,'También se forman por colisiones y fallas.'],['¿Qué proceso desgasta y transporta materiales?',['Erosión','Rotación de la Luna','Fusión solar'],0,'Agua, hielo, viento y gravedad modifican el relieve.']])
add('volcanes','tierra','Volcanes y sismos','Una Tierra activa','Dos fenómenos relacionados con el movimiento del planeta.',
'El magma es roca fundida bajo la superficie; cuando sale se llama lava. Un volcán puede emitir lava, gases y fragmentos. Las erupciones tienen estilos diferentes.|Los sismos liberan energía cuando las rocas se desplazan bruscamente en una falla. Muchos volcanes y sismos se concentran cerca de límites de placas, aunque no todos.',
'Un sismo no implica necesariamente una erupción. Estudiar un volcán requiere observar varias señales y su contexto. Las explicaciones escolares no sustituyen los avisos de protección civil ni permiten predecir un evento concreto.',
'Haz una tabla con “magma” y “lava”. Añade dónde se encuentra cada uno y explica por qué cambia el nombre.',
['USGS · Volcanes','https://www.usgs.gov/programs/VHP/about-volcanoes'],
[['¿Cómo se llama el magma que llega a la superficie?',['Lava','Núcleo','Atmósfera'],0,'Lava es el nombre del material fundido que sale al exterior.'],['¿Todo sismo indica una erupción?',['Sí','No','Solo si es de noche'],1,'Los sismos tienen distintos contextos; muchos no se relacionan con erupciones.']])
add('oceanos','tierra','Un océano, cinco grandes regiones','Planeta azul','El agua conecta costas, clima y vida.',
'El océano cubre aproximadamente el 71 % de la superficie terrestre. Sus aguas están conectadas, aunque distinguimos cinco grandes regiones: Pacífico, Atlántico, Índico, Ártico y Austral.|Las corrientes transportan agua y calor. El fondo marino tiene cordilleras, llanuras, cañones y fosas. La superficie relativamente plana del agua oculta un relieve complejo.',
'Las mareas se relacionan principalmente con la gravedad de la Luna y del Sol. No son lo mismo que las olas generadas por el viento. El océano influye en el clima y también recibe los efectos de actividades realizadas tierra adentro.',
'Localiza los cinco océanos en un mapa. Sigue una ruta de agua desde un río hasta el mar y describe qué podría transportar.',
['NOAA · Océanos y costas','https://www.noaa.gov/education/resource-collections/ocean-coasts'],
[['¿Qué proporción aproximada de la superficie cubre el océano?',['21 %','71 %','100 %'],1,'Cubre cerca del 71 % de la superficie, no del volumen terrestre.'],['¿Los cinco océanos están totalmente separados?',['Sí','No, forman un sistema conectado','Solo durante el invierno'],1,'Los nombres distinguen regiones de un océano global.']])
add('profundidades','tierra','Viaje a las profundidades','Exploración oceánica','La luz cambia mucho antes de llegar al fondo.',
'En aguas claras, la zona iluminada ocupa aproximadamente los primeros 200 metros. Entre 200 y 1 000 metros queda poca luz solar; por debajo de unos 1 000 metros no llega luz solar útil.|Estos límites son orientativos: la transparencia y las condiciones del agua cambian. Algunos seres vivos producen luz mediante bioluminiscencia. Oscuridad no significa ausencia de vida.',
'La profundidad y la distancia a la costa son cosas diferentes. Hay plataformas poco profundas y fosas muy hondas. Para observar el fondo se utilizan vehículos e instrumentos especializados. El laboratorio representa zonas de luz, no una inmersión real.',
'Mueve el control de profundidad. Anota en qué zonas podría utilizarse la luz solar para fotosíntesis y en cuáles sería insuficiente.',
['NOAA · Luz en el océano','https://oceanservice.noaa.gov/facts/light_travel.html'],
[['¿Dónde hay más luz solar?',['Cerca de la superficie','A 5 000 metros','Igual en todo el océano'],0,'El agua absorbe y dispersa la luz.'],['¿La oscuridad significa que no hay vida?',['Sí','No','Solo viven plantas'],1,'Existen organismos adaptados a ambientes oscuros.']])
add('agua','tierra','El agua está en movimiento','Ciclos de la Tierra','Un ciclo con muchos caminos posibles.',
'La energía solar favorece la evaporación. El vapor puede condensarse y formar pequeñas gotas o cristales en las nubes. El agua regresa como precipitación y puede infiltrarse, escurrir o almacenarse.|Las plantas devuelven agua a la atmósfera mediante transpiración. El agua también permanece en glaciares, suelo, acuíferos y océanos durante tiempos muy distintos.',
'El ciclo no es una rueda con una única ruta. Una gota puede permanecer mucho tiempo almacenada o cambiar varias veces de estado. La gravedad ayuda a mover el agua hacia zonas bajas; los usos humanos también modifican sus recorridos.',
'Cuenta el viaje de una gota usando evaporación, condensación y precipitación. Después inventa un segundo recorrido que pase por el subsuelo.',
['NOAA · Ciclo del agua','https://www.noaa.gov/education/resource-collections/freshwater/water-cycle'],
[['¿Qué es la evaporación?',['Paso de líquido a vapor','Paso de vapor a líquido','Formación de roca'],0,'La evaporación incorpora agua en forma de vapor al aire.'],['¿Toda el agua sigue exactamente la misma ruta?',['Sí','No','Solo el agua salada'],1,'Puede almacenarse y seguir muchos caminos.']])
add('clima','tierra','Tiempo y clima','Observar patrones','Un día frío y un clima frío no dicen lo mismo.',
'El tiempo describe condiciones atmosféricas de un momento y lugar: temperatura, lluvia o viento. El clima describe patrones y variabilidad durante periodos largos.|El océano, la atmósfera, el hielo y la superficie intercambian energía. Para estudiar cambios climáticos necesitamos series de datos, no una sola observación.',
'Una gráfica debe indicar variable, unidad, lugar y periodo. La variación de un día no resume una tendencia de décadas. Comparar datos exige revisar cómo y dónde se midieron.',
'Registra el tiempo durante una semana. Explica qué puedes concluir de esa semana y por qué no basta para describir el clima de décadas.',
['NOAA · Alfabetización oceánica y climática','https://oceanservice.noaa.gov/education/literacy.html'],
[['“Hoy llueve” describe…',['El tiempo','El clima de un siglo','El interior terrestre'],0,'Se refiere a una condición de corto plazo.'],['¿Qué se necesita para estudiar el clima?',['Un solo día','Series de datos a largo plazo','Solo una fotografía'],1,'El clima se estudia con patrones y variaciones prolongadas.']])
planets=[
 ['mercurio','Mercurio','Rocoso',4879,0.387,'El más cercano al Sol.'],
 ['venus','Venus','Rocoso',12104,0.723,'Una atmósfera muy densa.'],
 ['tierra','Tierra','Rocoso',12756,1,'Nuestro punto de referencia.'],
 ['marte','Marte','Rocoso',6792,1.524,'Un mundo rocoso con una atmósfera tenue.'],
 ['jupiter','Júpiter','Gigante gaseoso',142984,5.203,'El mayor planeta del sistema solar.'],
 ['saturno','Saturno','Gigante gaseoso',120536,9.537,'Sus anillos destacan en las observaciones.'],
 ['urano','Urano','Gigante helado',51118,19.191,'Un gigante con el eje muy inclinado.'],
 ['neptuno','Neptuno','Gigante helado',49528,30.069,'El más lejano de los ocho planetas.']]
data={'reviewed':'2026-10-04','topics':items,'planets':[dict(zip(['id','name','kind','diameter','au','note'],p)) for p in planets]}
(ROOT/'dist/data/science.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(len(items),'temas;',sum(len(t['quiz']) for t in items),'preguntas')
