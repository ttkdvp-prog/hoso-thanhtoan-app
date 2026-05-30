import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the "Ý kiến chỉ đạo..." frame box
old_box = '<p><strong>Ý kiến chỉ đạo của Lãnh đạo Trung tâm hạ tầng</strong></p><ul><li><em>Nội dung:</em></li><li><em>Thời gian hoàn thành:</em></li></ul>'
new_box = '''
<div style="border: 1px solid black; padding: 10px; margin: 15px 0;">
    <p style="text-align: center; margin: 5px 0;"><strong>Ý kiến chỉ đạo của Lãnh đạo Trung tâm hạ tầng</strong></p>
    <p style="margin: 10px 0 60px 0;">- <em>Nội dung:</em></p>
    <p style="margin: 10px 0 20px 0;">- <em>Thời gian hoàn thành:</em></p>
</div>
'''
html = html.replace(old_box, new_box)

# 2. Add signature space (dãn cách để đủ ký)
# The signature blocks are in <table class="layout-table">. The second row contains the names.
# We will inject a height style into the <tr> or <td> containing the names.
# For example: <tr><td><p><strong>Vũ Thị Lan Phương</strong></p></td> -> <tr style="height: 70px; vertical-align: bottom;"><td>...

html = html.replace('<tr><td><p><strong>Vũ Thị Lan Phương</strong></p>', '<tr style="height: 65px; vertical-align: bottom;"><td><p><strong>Vũ Thị Lan Phương</strong></p>')
html = html.replace('<tr><td><p><strong>Nguyễn Đăng Minh</strong></p>', '<tr style="height: 65px; vertical-align: bottom;"><td><p><strong>Nguyễn Đăng Minh</strong></p>')
html = html.replace('<tr><td><p><strong>Nguyễn Thu Trang............................</strong></p>', '<tr style="height: 65px; vertical-align: bottom;"><td><p><strong>Nguyễn Thu Trang............................</strong></p>')
html = html.replace('<tr><td><p><strong>GIÁM ĐỐC</strong></p></td></tr><tr><td><p><strong>(Ký, họ tên, đóng dấu)</strong></p></td></tr>', '<tr><td><p><strong>GIÁM ĐỐC</strong></p></td></tr><tr><td style="height: 80px; vertical-align: top;"><p><strong>(Ký, họ tên, đóng dấu)</strong></p></td></tr>')
html = html.replace('<tr><td><p><strong>BÊN GIAO</strong></p></td><td><p><strong>BÊN NHẬN</strong></p></td></tr><tr><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>', '<tr><td><p><strong>BÊN GIAO</strong></p></td><td><p><strong>BÊN NHẬN</strong></p></td></tr><tr style="height: 80px;"><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>')
html = html.replace('<tr><td><p><strong>BÊN A</strong></p></td><td><p><strong>BÊN B</strong></p></td></tr><tr><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>', '<tr><td><p><strong>BÊN A</strong></p></td><td><p><strong>BÊN B</strong></p></td></tr><tr style="height: 80px;"><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>')
html = html.replace('<tr><td><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr><tr><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>', '<tr><td><p><strong>ĐẠI DIỆN BÊN A</strong></p></td><td><p><strong>ĐẠI DIỆN BÊN B</strong></p></td></tr><tr style="height: 80px;"><td><p><strong> </strong></p></td><td><p><strong> </strong></p></td></tr>')

# Update the files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
