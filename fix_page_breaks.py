import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Tách chuỗi theo <table
# Mỗi trang trong file Word gốc đều bắt đầu bằng <table> chứa chữ VIỄN THÔNG PHÚ THỌ và CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
# Ngoại trừ Tờ Trình thanh toán hoặc một số thứ khác?
# Dấu hiệu nhận biết chắc chắn nhất là thẻ <table> bắt đầu một form mới (thường chứa "CỘNG HOÀ").

# Ta thay thế tất cả <table><tr><td><p> VIỄN THÔNG PHÚ THỌ</p> bằng việc chèn page-break
html = html.replace('<table><tr><td><p> VIỄN THÔNG PHÚ THỌ</p>', '<div class="page-break"></div><table><tr><td><p> VIỄN THÔNG PHÚ THỌ</p>')

# Hợp đồng kinh tế cũng bắt đầu bằng CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM nhưng không nằm trong table
html = html.replace('<p><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập – Tự do – Hạnh phúc</strong></p><p><strong>HỢP ĐỒNG KINH TẾ </strong></p>', '<div class="page-break"></div><p><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập – Tự do – Hạnh phúc</strong></p><p><strong>HỢP ĐỒNG KINH TẾ </strong></p>')

# Tờ trình cũng bắt đầu bằng CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM không có table
html = html.replace('<p><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập - Tự do - Hạnh phúc</strong></p><p><em>                   Phú Thọ, ngày     tháng    năm 2026   </em></p><p>Kính gửi: Viễn thông Phú Thọ</p>', '<div class="page-break"></div><p><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p><p><strong>Độc lập - Tự do - Hạnh phúc</strong></p><p><em>                   Phú Thọ, ngày     tháng    năm 2026   </em></p><p>Kính gửi: Viễn thông Phú Thọ</p>')

# Bỏ cái page-break đầu tiên nếu có
html = html.replace('<div id="contract-content">\n        <div class="page-break"></div>', '<div id="contract-content">\n        ')
html = html.replace('<div id="contract-content"><div class="page-break"></div>', '<div id="contract-content">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
