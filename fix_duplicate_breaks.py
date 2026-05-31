import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace multiple consecutive page-breaks with just one
html = re.sub(r'(<div class="page-break"></div>\n*)+', '<div class="page-break"></div>\n', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
