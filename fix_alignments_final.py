import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix supplier date alignment
# <p><em>                   Phú Thọ, ngày 28 tháng 4 năm 2026   </em></p>
pattern_date = r'<p>\s*<em>\s*(Phú Thọ, ngày \d+ tháng \d+ năm \d+)\s*</em>\s*</p>\s*<p class="title-center"><strong>Kính gửi: Viễn thông Phú Thọ</strong></p>'
html = re.sub(pattern_date, r'<p style="text-align: right; font-style: italic;">\1</p>\n<p class="title-center"><strong>Kính gửi: Viễn thông Phú Thọ</strong></p>', html)

# 2. Fix Tờ Trình centering
# Current HTML:
# <p class="title-center"><strong>TỜ TRÌNH</strong></p>
# <p><strong>V/v</strong><a id="_Hlk212676384"></a><strong> mua vật tư phục vụ sản xuất kinh doanh</strong></p>
# <p><strong> </strong></p>
# <p>                         Kính trình:   Giám đốc Trung tâm hạ tầng</p>

# We'll just replace the exact block
block_old = r'''<p class="title-center"><strong>TỜ TRÌNH</strong></p>
<p><strong>V/v</strong><a id="_Hlk212676384"></a><strong> mua vật tư phục vụ sản xuất kinh doanh</strong></p>
<p><strong> </strong></p>
<p>                         Kính trình:   Giám đốc Trung tâm hạ tầng</p>'''

block_new = r'''<p class="title-center"><strong>TỜ TRÌNH</strong></p>
<p class="title-center"><strong>V/v mua vật tư phục vụ sản xuất kinh doanh</strong></p>
<p class="title-center">Kính trình: Giám đốc Trung tâm Hạ tầng</p>'''

# Using regex just in case there are slight differences in whitespace
html = re.sub(r'<p class="title-center"><strong>TỜ TRÌNH</strong></p>\s*<p><strong>V/v</strong>(?:<a[^>]*></a>)?<strong>\s*mua vật tư phục vụ sản xuất kinh doanh\s*</strong></p>\s*(?:<p><strong>\s*</strong></p>\s*)?<p>\s*Kính trình:\s*Giám đốc Trung tâm hạ tầng</p>',
              block_new, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
