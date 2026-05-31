import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'<div class="page-break"></div>', html))
print('Total page breaks remaining:', len(matches))
