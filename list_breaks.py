import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'<div class="page-break"></div>', html))
for i, m in enumerate(matches):
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    context = html[start:end].replace('\n', '\\n')
    print(f'Break {i+1} at index {m.start()}:\n{context}\n')
