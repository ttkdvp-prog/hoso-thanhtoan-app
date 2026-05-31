import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix BIÊN BẢN NGHIỆM THU BÀN GIAO Header
html = html.replace(
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {NgayDeNghi}</p><h2 class="title-center">BIÊN BẢN NGHIỆM THU BÀN GIAO</h2>',
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {NgayGiaoNhan}</p><h2 class="title-center">BIÊN BẢN NGHIỆM THU BÀN GIAO</h2>'
)

# 2. Fix Giấy đề nghị thanh toán của đối tác Header
html = html.replace(
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {NgayDeNghi}</p>\n<p class="title-center"><strong>Kính gửi: Viễn',
    '<p style="text-align: right; font-style: italic;">Phú Thọ, ngày {NgayGiaoNhan}</p>\n<p class="title-center"><strong>Kính gửi: Viễn'
)

# 3. Fix Table Rows
# Row 3: Hóa đơn GTGT
html = html.replace(
    'Số: {SoHoaDon}</p><p>(1C26TTS)</p></td><td><p>{NgayDeNghi}</p></td><td><p>24.430.347',
    'Số: {SoHoaDon}</p><p>(1C26TTS)</p></td><td><p>{NgayGiaoNhan}</p></td><td><p>24.430.347'
)

# Row 7: Hợp đồng + biên bản bàn giao + thanh lý hợp đồng
html = html.replace(
    'Hợp đồng + biên bản bàn giao + thanh lý hợp đồng</p></td><td><p> </p></td><td><p> {NgayKyHopDong}</p>',
    'Hợp đồng + biên bản bàn giao + thanh lý hợp đồng</p></td><td><p> </p></td><td><p> {NgayThanhLy}</p>'
)

# Row 8: Giấy đề nghị thanh toán của đối tác
html = html.replace(
    'Giấy đề nghị thanh toán của đối tác </p></td><td><p> </p></td><td><p> {NgayDeNghi}</p>',
    'Giấy đề nghị thanh toán của đối tác </p></td><td><p> </p></td><td><p> {NgayGiaoNhan}</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
