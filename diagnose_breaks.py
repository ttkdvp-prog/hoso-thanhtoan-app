import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'<div class="page-break"></div>', html))
for i, m in enumerate(matches):
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    context = html[start:end].replace('\n', ' ')
    print(f'Break {i+1}: ...{context}...')

print("\n--- Consecutive spaces or empty paragraphs ---")
matches2 = list(re.finditer(r'<div class="page-break"></div>(?:\s*|<p>\s*</p>|<p>&nbsp;</p>|<br>)*<div class="page-break"></div>', html))
for i, m in enumerate(matches2):
    print(f'Found empty content between breaks at index {m.start()}')

