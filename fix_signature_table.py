import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the messy table at the end of BÁO CÁO ĐÁNH GIÁ.
# The table starts right after <h2 class="title-center">Báo cáo đánh giá này được lập bởi:</h2> 
# Wait, let's find the exact block.

old_table = """<table class="layout-table">
<tr>
<td></td>
<td>
<p><strong>TỔ TRƯỞNG</strong></p>
</td>
</tr>
<tr>
<td>
<p style="margin-top: 80px;"><strong>Nguyễn Thu Trang............................</strong></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p><strong>Nguyễn Thị Thúy................................</strong></p>
</td>
<td></td>
</tr>
<tr>
<td></td>
<td>
<p style="margin-top: 80px;"><strong>Vũ Thị Lan Phương</strong></p>
</td>
</tr>
</table>"""

# Actually, because of minification or lack of newlines, let's use regex.
pattern = r'<table class="layout-table">\s*<tr>\s*<td></td>\s*<td><p><strong>TỔ TRƯỞNG</strong></p></td>\s*</tr>\s*<tr>\s*<td><p( style="margin-top: 80px;")?><strong>Nguyễn Thu Trang\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.</strong></p></td>\s*<td></td>\s*</tr>\s*<tr>\s*<td><p><strong>Nguyễn Thị Thúy\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.</strong></p></td>\s*<td></td>\s*</tr>\s*<tr>\s*<td></td>\s*<td><p( style="margin-top: 80px;")?><strong>Vũ Thị Lan Phương</strong></p></td>\s*</tr>\s*</table>'

new_table = """<table class="layout-table">
<tr>
<td style="width: 50%;"><p><strong>CÁC THÀNH VIÊN</strong></p></td>
<td style="width: 50%;"><p><strong>TỔ TRƯỞNG</strong></p></td>
</tr>
<tr>
<td>
<p style="margin-top: 80px; margin-bottom: 20px;"><strong>Nguyễn Thu Trang............................</strong></p>
<p><strong>Nguyễn Thị Thúy................................</strong></p>
</td>
<td>
<p style="margin-top: 80px;"><strong>Vũ Thị Lan Phương</strong></p>
</td>
</tr>
</table>"""

# Let's do a more robust regex just in case spaces differ
html = re.sub(r'<table class="layout-table">\s*<tr>\s*<td>\s*</td>\s*<td>\s*<p>\s*<strong>TỔ TRƯỞNG</strong>\s*</p>\s*</td>\s*</tr>.*?Vũ Thị Lan Phương</strong>\s*</p>\s*</td>\s*</tr>\s*</table>', new_table, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
