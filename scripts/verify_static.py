"""Check packaged resources and data integrity without network access."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]/'dist'
errors=[]
for p in root.glob('*.html'):
 for target in re.findall(r'(?:src|href)=["\x27]([^"\x27]+)',p.read_text()):
  if target.startswith(('http:','https:','#','data:')):continue
  if not (root/target.split('?')[0]).is_file():errors.append(f'{p.name}: {target}')
science=json.loads((root/'data/science.json').read_text())
ids=[t['id'] for t in science['topics']]
assert len(ids)==len(set(ids))
for t in science['topics']:
 assert t['reading'] and t['deep'] and t['activity'] and t['source'][1].startswith('https://')
 for question,options,correct,why in t['quiz']:
  assert len(options)==3 and len(set(options))==3 and correct in range(3) and why
for c in json.loads((root/'data/chapters.json').read_text()):
 if not (root/c['image']).is_file():errors.append(c['image'])
for t in json.loads((root/'data/topics.json').read_text()):
 if not (root/'downloads'/f"{t['id']}.pdf").is_file():errors.append(t['id'])
assert not errors, errors
print('PASS: local scripts, styles, images, historical downloads and scientific content structure.')
