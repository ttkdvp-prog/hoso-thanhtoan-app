import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all exact matches
new_html = html.replace('mua vật tư phục vụ sản xuất kinh doanh', '{HoSoThanhToan.NoiDungToTrinh}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("SUCCESS")
