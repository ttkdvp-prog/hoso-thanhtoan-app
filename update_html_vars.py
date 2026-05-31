import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Contract number & Proposal number & Invoice number
html = html.replace('23426/VTPT-ST', '{SoHopDong}')
html = html.replace('62/TTr-TTHT-TTH', '{SoToTrinh}')
html = html.replace('00000207', '{SoHoaDon}')
html = html.replace('Công ty TNHH thương mại thiết bị điện công nghiệp Vĩnh Phúc', '{Tên khách hàng}')
html = html.replace('CÔNG TY TNHH THƯƠNG MẠI THIẾT BỊ ĐIỆN CÔNG NGHIỆP VĨNH PHÚC', '{Tên khách hàng}')

# 2. Quote Units
# Quote 1
html = html.replace('Hoàng Phương Thảo', '{Tendonvibaogia1}')
html = html.replace('Số 193A đường Nguyễn Viết Xuân, phường Vĩnh Phúc, Phú Thọ, Việt Nam', '{diachibaogia1}')
# Quote 2 (already partly replaced by {Tên khách hàng})
html = html.replace('- {Tên khách hàng}; Địa chỉ: {Địa chỉ};', '- {Tendonvibaogia2}; Địa chỉ: {diachibaogia2};')
# Quote 3
html = html.replace('Nguyễn Thị Bé', '{Tendonvibaogia3}')
html = html.replace('Chợ Vĩnh Yên, Phường Vĩnh Phúc, Tỉnh Phú Thọ, Việt Nam', '{diachibaogia3}')

# 3. Dates
# We will do context-based replacement for dates
# 23/04/2026 is NgayKyHopDong
html = re.sub(r'23/04/2026|23/4/2026|23 tháng 4 năm 2026|23 tháng 04 năm 2026', '{NgayKyHopDong}', html)

# 22/04/2026 is NgayToTrinh or Ngaybaogia
# For "báo giá ngày 22 tháng 4 năm 2026"
html = html.replace('báo giá ngày 22 tháng 4 năm 2026;', 'báo giá ngày {Ngaybaogia1};', 1)
html = html.replace('báo giá ngày 22 tháng 4 năm 2026;', 'báo giá ngày {Ngaybaogia2};', 1)
html = html.replace('báo giá ngày 22 tháng 4 năm 2026.', 'báo giá ngày {Ngaybaogia3}.')

# Any remaining 22/4/2026 is NgayToTrinh
html = re.sub(r'22/04/2026|22/4/2026|22 tháng 4 năm 2026|22 tháng 04 năm 2026', '{NgayToTrinh}', html)

# 28/04/2026 is either NgayDeNghi, NgayGiaoNhan, or NgayThanhLy
# Let's replace 28/4/2026 in specific sections.
# Giấy đề nghị thanh toán:
html = html.replace('Phú Thọ, ngày 28 tháng 4 năm 2026', 'Phú Thọ, ngày {NgayDeNghi}', 1)
# Bàn giao:
html = html.replace('ngày 28/4/2026, tại Viễn thông Phú Thọ', 'ngày {NgayGiaoNhan}, tại Viễn thông Phú Thọ')
# Thanh lý:
html = html.replace('ngày 28 tháng 04 năm 2026 tại Viễn thông Phú Thọ', 'ngày {NgayThanhLy} tại Viễn thông Phú Thọ')

# Any remaining 28/4/2026 might be generic, let's just make them {NgayDeNghi} as fallback
html = re.sub(r'28/04/2026|28/4/2026|28 tháng 4 năm 2026|28 tháng 04 năm 2026', '{NgayDeNghi}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
