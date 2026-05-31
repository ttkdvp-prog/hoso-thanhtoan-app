import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <h2><em>Phú Thọ, ngày 28 tháng 4 năm 2026</em></h2>
html = re.sub(r'<h2>\s*<em>Phú Thọ, ngày 28 tháng 4 năm 2026</em>\s*</h2>',
              r'<p style="text-align: right; font-style: italic;">Phú Thọ, ngày 28 tháng 4 năm 2026</p>', html)

# Replace <h2>BIÊN BẢN NGHIỆM THU BÀN GIAO</h2>
html = re.sub(r'<h2>\s*BIÊN BẢN NGHIỆM THU BÀN GIAO\s*</h2>',
              r'<h2 class="title-center">BIÊN BẢN NGHIỆM THU BÀN GIAO</h2>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
