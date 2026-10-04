# Atlas · Espacio, Tierra e Historia

Aplicación educativa en español para estudiantes, familias y docentes. Web estática, sin base de datos ni claves API.

## Contenido

- Espacio: 11 temas, desde el sistema solar hasta estrellas, galaxias, exoplanetas y agujeros negros.
- Tierra: 8 temas, incluyendo relieve, océanos, interior terrestre, agua y clima.
- Ciencia: 38 preguntas con explicación, lecturas en dos niveles, actividades y fuentes NASA, NOAA y USGS.
- Laboratorios: comparación de los ocho planetas, distancias a escala y zonas de luz oceánica.
- Historia: seis rutas, 57 episodios ilustrados, 55 acontecimientos, 47 fichas patrimoniales, mapa de México, juegos por equipos, seis PDF y un PowerPoint.
- Búsqueda entre las tres áreas, navegación lateral, adaptación móvil, impresión de fichas y modo proyector.

## Abrir en tu computadora

Con Python 3 instalado, ejecuta `python3 INICIAR.py`. En Mac también puedes abrir `INICIAR-MAC.command`; en Windows, `INICIAR-WINDOWS.bat`. Mantén el proceso abierto. Los datos JSON requieren servir el sitio por HTTP; abrir `index.html` directamente no basta.

## GitHub Pages

El directorio público es `dist`. No requiere compilación. Los recursos usan rutas relativas para funcionar tanto en la raíz de un dominio como bajo `/atlas-del-tiempo/`.

En Settings → Pages, selecciona **GitHub Actions** como origen. El flujo `pages.yml` valida el proyecto antes de publicar. Si GitHub Pages todavía no está habilitado, la configuración puede requerir que el propietario active ese ajuste; el código y las pruebas permanecen disponibles en el repositorio.

## Validación

`npm ci` y `npm test` ejecutan verificaciones de navegación, juegos, filtros, respuestas, búsqueda y laboratorios mediante un DOM simulado. `python3 scripts/verify_static.py` verifica recursos locales y referencias. Estas pruebas no sustituyen una revisión visual en dispositivos reales.

## Editar

- `dist/science.js` y `dist/atlas.css`: experiencias de Tierra y Espacio.
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
