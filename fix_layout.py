import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix CSS
html = html.replace('line-height: 1.5;', 'line-height: 1.13;\n            text-align: justify;')
html = html.replace('font-size: 13pt;', 'font-size: 14pt;')
html = html.replace('margin: 20mm 15mm;', 'margin: 20mm 15mm 20mm 30mm;')

# Fix missing page breaks
html = html.replace('<table class="layout-table"><tr><td><p>VIỄN THÔNG PHÚ THỌ</p>', '<div class="page-break"></div><table class="layout-table"><tr><td><p>VIỄN THÔNG PHÚ THỌ</p>')

# Hợp đồng phần cuối có "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" không?
# Tốt nhất cứ dùng replace 
html = html.replace('<p><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập - Tự do - Hạnh phúc</strong></p><p><strong>BIÊN BẢN', '<div class="page-break"></div><p><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập - Tự do - Hạnh phúc</strong></p><p><strong>BIÊN BẢN')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
