import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'\.{3,}', html))
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(html), m.end() + 50)
    print(f'...{html[start:end]}...')
