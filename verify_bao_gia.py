import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'(?:<div class="page-break"></div>\s*)?<p><strong>\s*CÔNG TY TNHH THƯƠNG MẠI THIẾT BỊ ĐIỆN CÔNG NGHIỆP VĨNH PHÚC\s*</strong></p>\s*<p>Địa chỉ[^<]*</p>\s*<p>Điện thoại[^<]*</p>\s*<p>Mã số thuế[^<]*</p>\s*(?:<div class="page-break"></div>\s*)?<p><strong>\s*BÁO GIÁ\s*</strong></p>'
matches = list(re.finditer(pattern, html))
if matches:
    print('Found the block, its content:')
    print(json.dumps(html[matches[-1].start()-100:matches[-1].end()]))
else:
    print('NOT FOUND')
