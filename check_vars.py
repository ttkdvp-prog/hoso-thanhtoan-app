import re
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = set(re.findall(r'\{KhachHang\.[^}]+\}', html))
for m in matches:
    print(m)
