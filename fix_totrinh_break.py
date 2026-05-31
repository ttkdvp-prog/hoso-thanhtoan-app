import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The specific table for Tờ Trình:
# <table class="layout-table"><tr><td><p>TRUNG TÂM HẠ TẦNG </p>...
pattern = r'(<table class="layout-table">\s*<tr>\s*<td>\s*<p>TRUNG TÂM HẠ TẦNG </p>)'

# Only add if it doesn't already have a page-break before it
def add_break(match):
    return '<div class="page-break"></div>\n' + match.group(1)

# We can just do a replace, but we need to ensure we don't duplicate page breaks
html = re.sub(pattern, add_break, html)
html = html.replace('<div class="page-break"></div>\n<div class="page-break"></div>\n', '<div class="page-break"></div>\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
