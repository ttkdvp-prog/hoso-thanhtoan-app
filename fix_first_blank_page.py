import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the page break immediately following <div id="contract-content">
html = re.sub(r'(<div id="contract-content">\s*)<div class="page-break"></div>', r'\1', html)

# Double check there are no duplicate page breaks anywhere
html = re.sub(r'(<div class="page-break"></div>\s*)+', '<div class="page-break"></div>\n', html)

# Ensure there's no page-break at the very end of contract-content
html = re.sub(r'<div class="page-break"></div>\s*(?=</div>\s*<script)', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
