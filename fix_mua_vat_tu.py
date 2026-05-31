import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure any paragraph containing exactly this phrase (with or without strong tags) is centered
html = re.sub(r'<p[^>]*>((<strong>)*mua vật tư phục vụ sản xuất kinh doanh(</strong>)*)</p>', r'<p class="title-center">\1</p>', html)

# Just in case there's another variant:
html = html.replace('<p><strong>mua vật tư phục vụ sản xuất kinh doanh</strong></p>', '<p class="title-center"><strong>mua vật tư phục vụ sản xuất kinh doanh</strong></p>')
html = html.replace('<p>mua vật tư phục vụ sản xuất kinh doanh</p>', '<p class="title-center">mua vật tư phục vụ sản xuất kinh doanh</p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
