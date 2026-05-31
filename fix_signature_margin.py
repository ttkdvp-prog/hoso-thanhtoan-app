import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the TR height attempt that failed (we leave the tr as is or clean it up)
html = html.replace('<tr style="height: 65px; vertical-align: bottom;">', '<tr>')

# We add margin-top to the actual names so they are pushed down robustly!
names = [
    'Vũ Thị Lan Phương',
    'Nguyễn Thị Phương Anh',
    'Lê Văn Đức',
    'Nguyễn Đăng Minh',
    'Nguyễn Việt Hùng',
    'Trần Thanh Phong',
    'Hoàng Phương Thảo'
]

# We also have generic signature lines:
# <p><strong>(Ký, họ tên, đóng dấu)</strong></p>
# <p><strong>Nguyễn Thu Trang............................</strong></p>
# And for "BÊN GIAO", "BÊN NHẬN", there is an empty <p><strong> </strong></p> or <p><strong> </strong></p> under it. 
# We'll replace them globally with margin-top.

# 1. Specific names
for name in names:
    html = re.sub(r'<p><strong>\s*' + name + r'\s*</strong></p>', r'<p style="margin-top: 80px;"><strong>' + name + r'</strong></p>', html)

# 2. Nguyễn Thu Trang............................
html = re.sub(r'<p><strong>\s*Nguyễn Thu Trang\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\s*</strong></p>', r'<p style="margin-top: 80px;"><strong>Nguyễn Thu Trang............................</strong></p>', html)

# 3. (Ký, họ tên, đóng dấu)
html = re.sub(r'<p><strong>\s*\(Ký, họ tên, đóng dấu\)\s*</strong></p>', r'<p style="margin-top: 80px;"><strong>(Ký, họ tên, đóng dấu)</strong></p>', html)

# 4. Remove the failed tr style:
html = html.replace('<tr style="height: 80px; vertical-align: top;">', '<tr>')
html = html.replace('<tr style="height: 80px;">', '<tr>')

# Now for the empty spaces in BÊN A / BÊN B
# Instead of empty <p><strong> </strong></p>, we just use <p style="height: 80px;"></p>
# Let's find: <tr><td><p><strong>BÊN A</strong></p>... then the next row
html = re.sub(r'<tr><td><p><strong>BÊN GIAO</strong></p></td><td><p><strong>BÊN NHẬN</strong></p></td></tr>\s*<tr><td><p><strong>\s*</strong></p></td><td><p><strong>\s*</strong></p></td></tr>', 
              r'<tr><td><p><strong>BÊN GIAO</strong></p></td><td><p><strong>BÊN NHẬN</strong></p></td></tr><tr><td><p style="height: 80px;"></p></td><td><p style="height: 80px;"></p></td></tr>', html)

html = re.sub(r'<tr><td><p><strong>BÊN A</strong></p></td><td><p><strong>BÊN B</strong></p></td></tr>\s*<tr><td><p><strong>\s*</strong></p></td><td><p><strong>\s*</strong></p></td></tr>', 
              r'<tr><td><p><strong>BÊN A</strong></p></td><td><p><strong>BÊN B</strong></p></td></tr><tr><td><p style="height: 80px;"></p></td><td><p style="height: 80px;"></p></td></tr>', html)

html = re.sub(r'<tr><td><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr>\s*<tr><td><p><strong>\s*</strong></p></td><td><p><strong>\s*</strong></p></td></tr>', 
              r'<tr><td><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr><tr><td><p style="height: 80px;"></p></td><td><p style="height: 80px;"></p></td></tr>', html)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
