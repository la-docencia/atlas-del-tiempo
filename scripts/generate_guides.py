import json,os,sys
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
os.makedirs('dist/downloads',exist_ok=True)
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
styles=getSampleStyleSheet()
for name in ['Normal','BodyText','Heading1','Heading2','Heading3','Title']:
 styles[name].fontName='DejaVu';styles[name].textColor=HexColor('#162b2f')
styles['BodyText'].fontSize=10;styles['BodyText'].leading=15;styles['BodyText'].spaceAfter=9
styles['Title'].fontSize=26;styles['Title'].leading=33;styles['Title'].alignment=TA_LEFT
styles['Heading2'].spaceBefore=16;styles['Heading2'].fontSize=15
styles.add(ParagraphStyle('Source',parent=styles['BodyText'],fontSize=8,leading=12,wordWrap='CJK'))
def footer(c,d):
 c.setStrokeColor(HexColor('#d9cbb7'));c.line(45,43,A4[0]-45,43);c.setFont('DejaVu',8);c.drawString(45,29,'ATLAS DEL TIEMPO · Guía docente · Septiembre 2026');c.drawRightString(A4[0]-45,29,str(d.page))
for t in json.load(open('dist/data/topics.json')):
 if len(sys.argv)>1 and t['id'] not in sys.argv[1:]:continue
 story=[]
 def p(x,style='BodyText'):story.append(Paragraph(escape(str(x)),styles[style]))
 def h(x):p(x,'Heading2')
 p('ATLAS DEL TIEMPO · HISTORIA PARA EL AULA','Heading3');p(t['title'],'Title');p(t['era']+' · '+str(t['duration'])+' minutos');p(t['level']);h('Pregunta guía');p(t['question']);h('Objetivo');p(t['objective']);h('Para explicar en clase');p(t['summary'])
 for x in t['classroom']:p(x)
 story.append(PageBreak());h('Una lectura más profunda')
 for x in t['deep']:p(x)
 h('Hechos, interpretaciones y tradiciones')
 for a,b in t['evidence']:p(a,'Heading3');p(b)
 h('Dato para conversar');p(t['curiosity']);h('Personajes y protagonistas')
 for a,b in t['people']:p(a+': '+b)
 story.append(PageBreak());h('Fechas y lugares')
 for a,b in t['dates']:p(a+' — '+b)
 for x in t['places']:p(x['name']+': '+x['note'])
 p('Las ubicaciones y límites actuales sirven para orientarse; no representan las fronteras de la época.');h('Secuencia didáctica')
 for i,x in enumerate(t['activity'],1):p(str(i)+'. '+x)
 h('Evaluación formativa');p(t['assessment']);h('Adaptación');p(t['adaptation'])
 story.append(PageBreak());h('Recorrido ampliado por episodios')
 for c in json.load(open('dist/data/chapters.json')):
  if c['route']!=t['id']:continue
  story.append(KeepTogether([Paragraph(escape(c['date']),styles['Heading3']),Paragraph(escape(c['title']),styles['Heading2']),Paragraph(escape(c['text']),styles['BodyText'])]))
  p('Antecedente: '+c['cause']);p('Consecuencia: '+c['effect']);p('Pregunta: '+c['question']);p('Orientación: '+c['answer']);p('Actividad: '+c['activity']);p(c['source'][0],'Source')
  story.append(Paragraph('<link href="'+escape(c['source'][1])+'" color="#355155">'+escape(c['source'][1])+'</link>',styles['Source']))
 if t['id']=='segunda-guerra-mundial':
  h('Secuencia ampliada: cuatro sesiones de 45 minutos')
  p('Sesión 1: antecedentes, Asia y comienzo europeo (episodios 1–4). Dedicar 10 minutos al mapa, 25 a lectura acompañada y 10 a comparar causas.')
  p('Sesión 2: expansión, Holocausto y México (episodios 5–8). Seleccionar previamente fuentes y biografías; reservar tiempo para preguntas y una reflexión escrita.')
  p('Sesión 3: cambios de frente y participación mexicana (episodios 9–13). Comparar mapas y explicar por qué una batalla no resume toda la guerra.')
  p('Sesión 4: final y posguerra (episodios 14–15). Analizar el documento de rendición, distinguir hechos e interpretaciones y elaborar una explicación con fuentes.')
 else:
  h('Secuencia ampliada: dos sesiones de 45 minutos')
  p('Sesión 1: 5 minutos para activar conocimientos, 20 para leer cuatro episodios, 15 para comparar antecedentes y consecuencias y 5 para una pregunta de salida.')
  p('Sesión 2: 15 minutos para completar el recorrido, 15 para contrastar una fuente, 10 para defender una explicación y 5 para revisar la respuesta inicial.')
 h('Rúbrica de explicación histórica')
 p('En proceso: enumera datos sin conectarlos. Logrado: relaciona tiempo, lugar y evidencia. Profundiza: compara explicaciones y reconoce límites de las fuentes. Permite respuestas orales, escritas o visuales.')
 story.append(PageBreak());h('Hoja de trabajo · Nombre: ____________________');p('1. Responde la pregunta guía con una evidencia de la lectura.');story.append(Spacer(1,65));p('2. Compara dos protagonistas o lugares. ¿En qué se parecen y en qué se diferencian?');story.append(Spacer(1,65));p('3. Elige un hecho y una interpretación. Explica cómo los distingues.');story.append(Spacer(1,65));p('4. Escribe una pregunta abierta y una fuente que consultarías para investigarla.');story.append(Spacer(1,65));h('Reto de comprensión')
 for q,opts,answer,why in t['quiz']:p(q);p(' / '.join(chr(65+i)+') '+o for i,o in enumerate(opts)))
 story.append(PageBreak());h('Clave para el docente')
 for q,opts,answer,why in t['quiz']:p(q,'Heading3');p(opts[answer]+'. '+why)
 h('Criterios para revisar la hoja');p('Busca explicaciones que distingan tiempo y lugar, utilicen una evidencia concreta y reconozcan los límites de lo que sabemos. Acepta formulaciones distintas cuando estén justificadas.');h('Fuentes y lecturas')
 for name,url,kind in t['sources']:
  p(name+' · '+kind);story.append(Paragraph('<link href="'+escape(url)+'" color="#355155">'+escape(url)+'</link>',styles['Source']))
 p('Síntesis y actividades elaboradas para Atlas del Tiempo. Fuentes consultadas en septiembre de 2026. “c.” significa aproximadamente. Las actividades son propuestas didácticas; no sustituyen la lectura de las fuentes.','Source')
 SimpleDocTemplate('dist/downloads/'+t['id']+'.pdf',pagesize=A4,rightMargin=45,leftMargin=45,topMargin=45,bottomMargin=60,title=t['title']+' · Guía docente',author='Atlas del Tiempo').build(story,onFirstPage=footer,onLaterPages=footer)
 print(t['id'])
