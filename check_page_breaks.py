import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'(<div class="page-break"></div>)?\s*(<p[^>]*>\s*<strong>CỘNG HO?À XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*</strong>\s*</p>)', html, re.IGNORECASE)

for i, m in enumerate(matches):
    print(f'Match {i}: has_page_break={m.group(1) is not None}')
