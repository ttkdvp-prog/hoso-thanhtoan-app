import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace all {NgayDeNghi} with {NgayTao}
html = html.replace('{NgayDeNghi}', '{NgayTao}')

# 2. Fix Invoice Date variables
# Table Row 3: Hóa đơn GTGT
html = html.replace(
    'Số: {SoHoaDon}</p><p>(1C26TTS)</p></td><td><p>{NgayGiaoNhan}</p>',
    'Số: {SoHoaDon}</p><p>(1C26TTS)</p></td><td><p>{Ngày hóa đơn}</p>'
)

# Table Row 8: Giấy đề nghị thanh toán của đối tác
html = html.replace(
    'Giấy đề nghị thanh toán của đối tác </p></td><td><p> </p></td><td><p> {NgayGiaoNhan}</p>',
    'Giấy đề nghị thanh toán của đối tác </p></td><td><p> </p></td><td><p> {Ngày hóa đơn}</p>'
)

# Header of Giấy đề nghị thanh toán của đối tác
html = html.replace(
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {NgayGiaoNhan}</p>\n<p class="title-center"><strong>Kính gửi: Viễn',
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {Ngày hóa đơn}</p>\n<p class="title-center"><strong>Kính gửi: Viễn'
)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
