from pathlib import Path
import csv, html
from collections import OrderedDict
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1]
groups = OrderedDict()
with (ROOT / 'data/models.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
seen = set()
for row in rows:
    if not all(row.get(k, '').strip() for k in ('model','part_code','sticker','url')):
        raise ValueError('Every row needs model, part_code, sticker and url')
    if urlparse(row['url']).scheme not in ('https','http'):
        raise ValueError('URL must start with https:// or http://')
    if row['model'] in seen: raise ValueError('Duplicate model: ' + row['model'])
    seen.add(row['model'])
    groups.setdefault((row['part_code'],row['sticker']),[]).append(row)
e = html.escape
sections = []
for (code,label), records in groups.items():
    content = '<section><div class="group"><h2>'+e(label)+'</h2><p>Part code <strong>'+e(code)+'</strong></p></div><div class="models">'
    for row in records:
        content += '<a href="'+e(row['url'],quote=True)+'"><span>'+e(row['model'])+'</span><span class="open">View photo <span aria-hidden="true">&#8599;</span></span></a>'
    sections.append(content + '</div></section>')
template = (ROOT/'scripts/page-template.html').read_text(encoding='utf-8')
assert template.count('{{MODEL_SECTIONS}}') == 1
(ROOT/'website/index.html').write_text(template.replace('{{MODEL_SECTIONS}}',''.join(sections)),encoding='utf-8')
print(f'Built website/index.html: {len(rows)} models, {len(groups)} groups.')
