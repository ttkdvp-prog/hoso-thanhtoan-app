import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix borders by changing layout-table back to data-table for actual data tables
html = html.replace('<table class="layout-table"><tr><td><p><strong>STT</strong></p>', '<table class="data-table"><tr><td><p><strong>STT</strong></p>')

# Fix line-height 1.0 for DANH MỤC HỒ SƠ THANH TOÁN table (starts with rowspan)
html = html.replace('<table class="layout-table"><tr><td rowspan="2"><p><strong>STT</strong></p>', '<table class="data-table" style="line-height: 1.0; font-size: 13pt;"><tr><td rowspan="2"><p><strong>STT</strong></p>')

# Fix the HỢP ĐỒNG KINH TẾ table (Hàng Hóa)
html = html.replace('<table class="layout-table"><tr><td><p><strong>STT</strong></p></td><td><p><strong>Tên hàng hóa, dịch vụ</strong></p>', '<table class="data-table" style="line-height: 1.0; font-size: 13pt;"><tr><td><p><strong>STT</strong></p></td><td><p><strong>Tên hàng hóa, dịch vụ</strong></p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
