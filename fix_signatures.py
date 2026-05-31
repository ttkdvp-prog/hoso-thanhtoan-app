import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the paragraph-based signatures with a table
signature_table = '''<table class="layout-table" style="width: 100%; text-align: center;">
<tr>
<td style="width: 50%;"><p><strong>ĐẠI DIỆN BÊN A</strong></p></td>
<td style="width: 50%;"><p><strong>ĐẠI DIỆN BÊN B</strong></p></td>
</tr>
<tr><td style="height: 80px;"></td><td></td></tr>
</table>'''

html = re.sub(r'<p><strong>\s*ĐẠI DIỆN BÊN A\s*ĐẠI DIỆN BÊN B\s*</strong></p>', signature_table, html)

# Also let's make sure the other signature table is centered if it isn't
html = html.replace('<table class="layout-table"><tr><td><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr>', 
                    '<table class="layout-table" style="width: 100%; text-align: center;"><tr><td style="width: 50%;"><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td style="width: 50%;"><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
