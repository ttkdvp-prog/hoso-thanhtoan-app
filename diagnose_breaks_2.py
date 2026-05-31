import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches2 = list(re.finditer(r'<div class="page-break"></div>(?:\s*|<p>\s*</p>|<p>&nbsp;</p>|<br>|<table class="layout-table"><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>)*<div class="page-break"></div>', html))
for m in matches2:
    print('Found empty content between breaks at index', m.start())
    print(repr(m.group(0)))
