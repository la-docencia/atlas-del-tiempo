# Atlas · Espacio, Tierra e Historia

Aplicación educativa en español para estudiantes, familias y docentes. Web estática, sin base de datos ni claves API.

## Contenido

- Vida cotidiana y fuentes: tres casos, seis tarjetas de fuentes y doce afirmaciones para distinguir observación, información documental, interpretación y conclusiones no justificadas. Fotografías reales del Met y la Biblioteca del Congreso con procedencia y derechos, ampliación, notas temporales, impresión y tres profundidades.
- Taller de historia: cuatro líneas del tiempo temáticas, 24 tarjetas (18 conexiones con episodios existentes y seis hitos nuevos sobre participación política de las mujeres), tres ilustraciones conceptuales, puzzle cronológico, retos de causas/consecuencias y preguntas con evidencia. Tres profundidades, cuaderno temporal e impresión del trabajo.
- Espacio: 11 temas, desde el sistema solar hasta estrellas, galaxias, exoplanetas y agujeros negros.
- Tierra: 8 temas, incluyendo relieve, océanos, interior terrestre, agua y clima.
- Ciencia: 38 preguntas con explicación, tres rutas de aprendizaje (niñez, jóvenes y adultos/universidad), actividades y fuentes NASA, NOAA y USGS.
- Laboratorios: comparación de los ocho planetas, distancias a escala y zonas de luz oceánica.
- Misiones Atlas: puzzle para ordenar los planetas, detective de hechos/interpretaciones/tradiciones y visor de imágenes con zoom, preguntas y observaciones guardadas localmente.
- Biblioteca visual: cuatro diagramas vectoriales interactivos (Sistema Solar, capas de la Tierra, ciclo del agua y lectura de procesos históricos), además de una selección de referencias externas para proyectar.
- Animaciones guiadas: seis modelos paso a paso —eclipses, estaciones, gravedad, volcanes, placas tectónicas y una ruta histórica esquemática— con pausa, reproducción, control de pasos y enlaces a las fichas.
- Historia: seis rutas, 57 episodios ilustrados, 55 acontecimientos, 47 fichas patrimoniales, mapa de México, juegos por equipos, seis PDF y un PowerPoint.
- Búsqueda entre las tres áreas, selector de ruta que se conserva en el navegador, navegación lateral, adaptación móvil, impresión de fichas y modo proyector.

## Abrir en tu computadora

Con Python 3 instalado, ejecuta `python3 INICIAR.py`. En Mac también puedes abrir `INICIAR-MAC.command`; en Windows, `INICIAR-WINDOWS.bat`. Mantén el proceso abierto. Los datos JSON requieren servir el sitio por HTTP; abrir `index.html` directamente no basta.

## GitHub Pages

El directorio público es `dist`. No requiere compilación. Los recursos usan rutas relativas para funcionar tanto en la raíz de un dominio como bajo `/atlas-del-tiempo/`.

En Settings → Pages, selecciona **GitHub Actions** como origen. El flujo `pages.yml` valida el proyecto antes de publicar. Si GitHub Pages todavía no está habilitado, la configuración puede requerir que el propietario active ese ajuste; el código y las pruebas permanecen disponibles en el repositorio.

## Validación

`npm ci` y `npm test` ejecutan verificaciones de navegación, juegos, filtros, respuestas, búsqueda y laboratorios mediante un DOM simulado. `python3 scripts/verify_static.py` verifica recursos locales y referencias. Estas pruebas no sustituyen una revisión visual en dispositivos reales.

## Editar

- `dist/science.js`, `dist/interactive.js` y `dist/atlas.css`: experiencias de Tierra, Espacio y aprendizaje activo.
- `dist/visuals.js`: diagramas educativos vectoriales con partes clicables y explicaciones contextuales.
- `dist/animations.js`: modelos SVG guiados para explicar procesos científicos e históricos sin depender de imágenes externas.
- `scripts/expand_science.py`: contenido editorial; genera `dist/data/science.json`.
- `dist/app.js`, `learning.js`, `explorations.js`: Historia y patrimonio.
- `dist/data`: datos y cartografía.
- `dist/downloads`: recursos históricos incluidos.

La cartografía municipal histórica es un catálogo antiguo de referencia. Los nuevos artículos científicos son una introducción, no una enciclopedia exhaustiva. Los scripts históricos de generación pueden conservar rutas del entorno original: revísalas antes de regenerar ilustraciones o documentos.

## Imágenes y fuentes

Los temas muestran fuentes institucionales y fecha de revisión. Los datos planetarios son aproximados; el comparador usa diámetros ecuatoriales y distancias medias al Sol, no posiciones actuales.

Tierra: NASA, fotografía Apollo 17. Saturno: NASA/JPL/Space Science Institute, composición natural de Cassini. Orión: NASA, ESA, Hubble Space Telescope Orion Treasury Project Team, Massimo Robberto (STScI, ESA), mosaico con colores asignados. Consulta `#creditos` dentro de la aplicación para las páginas originales. El crédito no implica respaldo institucional. Las ilustraciones históricas generadas con IA se identifican como recreaciones.

## Estado de la entrega · 4 de octubre de 2026

Restauración completa de la versión histórica y primera ampliación de Tierra y Espacio. No incluye cuentas de alumnos ni almacenamiento de calificaciones. Las rondas se reinician al salir; no se envían respuestas a un servidor.

- Aventura «Del grano a las ciudades»: cinco etapas con fuentes reales, cronología, reparto de trabajo en un modelo didáctico explícito, contraste de ideas y conclusión con evidencia y límites. Tres profundidades, impresión, proyector y progreso guardado en el dispositivo; no incluye calificación automática del texto.

- «Detectives de la Revolución»: fotografía histórica Bain/LOC con ampliación y ficha, cuatro referencias cronológicas, comparación de tres programas mediante síntesis y fuentes, mapa con tres lugares y conclusión con evidencia y límites. Tres profundidades, proyector, impresión y progreso guardado en el dispositivo.
