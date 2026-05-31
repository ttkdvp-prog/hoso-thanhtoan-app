import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add page break before any table that contains the National Motto
pattern = r'(<table class="layout-table"[^>]*>(?:(?!</table).)*?CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM(?:(?!</table).)*?</table>)'

def add_break(match):
    return '<div class="page-break"></div>\n' + match.group(1)

html = re.sub(pattern, add_break, html, flags=re.DOTALL)

# 2. For standalone National Mottos not inside a table
# Since the layout-table replacement above handled all Mottos inside a table,
# ANY remaining `<p class="quoc-hieu...">CỘNG HÒA` that doesn't have a page break before it should get one.
# But wait, what if we just prepend a page break to ALL CỘNG HÒA?
# If it's inside a table cell, it will be added inside the cell! Which we specifically DO NOT WANT.
# So let's NOT prepend to all CỘNG HÒA.
# Let's find all `<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>`
# If the 10 characters before it contain `><td>` or `> <td>`, it's inside a cell.
# Wait, let's just do a manual string split and replace:
parts = html.split('<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>')
new_html = parts[0]
for part in parts[1:]:
    # Check what ends new_html
    if new_html.strip().endswith('>') and ('<td' in new_html[-15:]):
        # It's right after a <td>, don't add page break here
        new_html += '<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>' + part
    else:
        # Not right after a <td>, so add a page break if not already one
        if not new_html.strip().endswith('<div class="page-break"></div>'):
            new_html += '<div class="page-break"></div>\n'
        new_html += '<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>' + part
html = new_html

# Deduplicate
html = re.sub(r'(<div class="page-break"></div>\s*)+', '<div class="page-break"></div>\n', html)

# Remove the very first page break if it's at the beginning of the file
html = re.sub(r'^\s*<div class="page-break"></div>\n', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
