import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# First, remove the page-break before BÁO GIÁ
html = html.replace('<div class="page-break"></div>\n<p><strong>BÁO GIÁ</strong></p>', '<p><strong>BÁO GIÁ</strong></p>')

# Add the page-break before CÔNG TY... but ONLY the one that is before BÁO GIÁ
# We can find the exact block:
block = r'''<p><strong>CÔNG TY TNHH THƯƠNG MẠI THIẾT BỊ ĐIỆN CÔNG NGHIỆP VĨNH PHÚC</strong></p>
<p>Địa chỉ\t           : {KhachHang.Địa chỉ}</p>
<p>Điện thoại              : 0211 3861284</p>
<p>Mã số thuế\t: {KhachHang.Mã số thuế}</p>
<p><strong>BÁO GIÁ</strong></p>'''

# Let's use regex to find this block because there might be varying whitespaces
pattern = r'(<p><strong>\s*CÔNG TY TNHH THƯƠNG MẠI THIẾT BỊ ĐIỆN CÔNG NGHIỆP VĨNH PHÚC\s*</strong></p>\s*<p>Địa chỉ[^<]*</p>\s*<p>Điện thoại[^<]*</p>\s*<p>Mã số thuế[^<]*</p>\s*(?:<div class="page-break"></div>\s*)?<p><strong>\s*BÁO GIÁ\s*</strong></p>)'

html = re.sub(pattern, r'<div class="page-break"></div>\n\1', html)

# Just in case the page break was already there or something, let's also remove any page-breaks inside the block.
def remove_internal_page_breaks(match):
    content = match.group(0)
    content = content.replace('<div class="page-break"></div>', '')
    content = content.replace('<div class="page-break"></div>\n', '')
    return '<div class="page-break"></div>\n' + content

html = re.sub(pattern, remove_internal_page_breaks, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
