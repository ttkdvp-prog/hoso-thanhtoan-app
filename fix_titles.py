import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS class for centering
css_addition = """
        .title-center {
            text-align: center !important;
            margin: 5pt 0 !important;
        }
"""
html = html.replace('</style>', css_addition + '</style>')

# 2. Use regex to center specific document titles
titles_to_center = [
    r'(<p[^>]*>)(<strong>GIẤY ĐỀ NGHỊ THANH TOÁN</strong></p>)',
    r'(<p[^>]*>)(<strong>DANH MỤC HỒ SƠ THANH TOÁN</strong></p>)',
    r'(<p[^>]*>)(<strong>TỜ TRÌNH</strong></p>)',
    r'(<p[^>]*>)(<strong>HỢP ĐỒNG KINH TẾ\s*</strong></p>)',
    r'(<p[^>]*>)(<strong>BIÊN BẢN GIAO NHẬN VẬT TƯ, HÀNG HÓA</strong></p>)',
    r'(<p[^>]*>)(<strong>BIÊN BẢN THANH LÝ HỢP ĐỒNG</strong></p>)',
    r'(<p[^>]*>)(Số:\s*<strong>23426/VTPT-ST</strong></p>)', # Check for Hợp đồng số
    r'(<p[^>]*>)(Số:\s*23426/VTPT-ST</p>)',
    r'(<h\d[^>]*>)(<a[^>]*></a>)*(\s*BÁO CÁO ĐÁNH GIÁ BÁO GIÁ.*?</h\d>)',
    r'(<p[^>]*>)(<strong>BÁO CÁO ĐÁNH GIÁ BÁO GIÁ</strong></p>)',
]

# The "Kính gửi" line has tons of spaces: <p><strong><em>                                  Kính gửi</em></strong>: <strong>Lãnh đạo Viễn thông Phú Thọ</strong></p>
# We will strip the spaces and center it.
html = re.sub(r'<p>\s*<strong><em>\s+Kính gửi</em></strong>:\s*<strong>Lãnh đạo Viễn thông Phú Thọ</strong></p>',
              '<p class="title-center"><strong><em>Kính gửi:</em> Lãnh đạo Viễn thông Phú Thọ</strong></p>', html)

html = re.sub(r'<p>\s*<strong><em>\s+Kính gửi:\s*</em></strong>\s*<strong>Lãnh đạo Viễn thông Phú Thọ</strong></p>',
              '<p class="title-center"><strong><em>Kính gửi:</em> Lãnh đạo Viễn thông Phú Thọ</strong></p>', html)

html = re.sub(r'<p>\s*(<strong>)*Kính gửi:\s*Viễn thông Phú Thọ(</strong>)*\s*</p>',
              '<p class="title-center"><strong>Kính gửi: Viễn thông Phú Thọ</strong></p>', html)


# For the main document titles
for pattern in titles_to_center:
    html = re.sub(pattern, lambda m: '<p class="title-center">' + m.group(2) if m.group(1).startswith('<p') else '<p class="title-center">' + m.group(3), html)

# Some specific replacements from the screenshots:
# "BÁO CÁO ĐÁNH GIÁ BÁO GIÁ" / "mua vật tư..." / "Kính trình..."
html = re.sub(r'<p[^>]*>(<strong>)*BÁO CÁO ĐÁNH GIÁ BÁO GIÁ(</strong>)*</p>', '<p class="title-center"><strong>BÁO CÁO ĐÁNH GIÁ BÁO GIÁ</strong></p>', html)
html = re.sub(r'<p[^>]*>mua vật tư phục vụ sản xuất kinh doanh</p>', '<p class="title-center">mua vật tư phục vụ sản xuất kinh doanh</p>', html)
html = re.sub(r'<p[^>]*>Kính trình:\s*Giám đốc Trung tâm Hạ Tầng</p>', '<p class="title-center">Kính trình: Giám đốc Trung tâm Hạ Tầng</p>', html)
html = re.sub(r'<p[^>]*>Số:\s*<strong>23426/VTPT-ST</strong></p>', '<p class="title-center">Số: <strong>23426/VTPT-ST</strong></p>', html)
html = re.sub(r'<p[^>]*>Số:\s*23426/VTPT-ST</p>', '<p class="title-center">Số: 23426/VTPT-ST</p>', html)

# Update both files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
