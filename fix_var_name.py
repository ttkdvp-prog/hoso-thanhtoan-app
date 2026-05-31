import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace {HoSoThanhToan.NoiDungToTrinh} with {NoiDungToTrinh}
new_html = html.replace('{HoSoThanhToan.NoiDungToTrinh}', '{NoiDungToTrinh}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("SUCCESS")
