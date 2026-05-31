import re
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

patterns = [
    r'23426/VTPT-ST',
    r'62/TTr-TTHT-TTH',
    r'00000207',
    r'ngày \d+ tháng \d+ năm \d+',
    r'\d{1,2}/\d{1,2}/2026',
    r'Công ty TNHH thương mại thiết bị điện công nghiệp Vĩnh Phúc',
    r'BÁO GIÁ',
    r'Công ty [A-Za-z0-9\s]+'
]

for p in patterns:
    matches = re.finditer(p, html, re.IGNORECASE)
    print(f"--- Pattern: {p} ---")
    for m in matches:
        start = max(0, m.start() - 60)
        end = min(len(html), m.end() + 60)
        print(f"...{html[start:end]}...")
    print("\n")
