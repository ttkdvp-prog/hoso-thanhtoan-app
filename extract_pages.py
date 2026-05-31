import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('<div class="page-break"></div>')
for i, part in enumerate(parts):
    clean = re.sub(r'<[^>]+>', '', part).strip()
    preview = clean[:100].replace('\n', ' ')
    print(f'Page {i+1}: {preview}')
