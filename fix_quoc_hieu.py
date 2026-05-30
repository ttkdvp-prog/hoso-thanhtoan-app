import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_addition = """
        .quoc-hieu {
            text-align: center !important;
            margin: 0 !important;
        }
        .quoc-hieu-1 {
            font-size: 13pt;
        }
        .quoc-hieu-2 {
            font-size: 14pt;
            display: inline-block;
            border-bottom: 1.5px solid black;
            padding-bottom: 2px;
            margin-bottom: 5pt;
        }
        .co-quan-1 {
            text-align: center !important;
            font-size: 13pt;
            margin: 0 !important;
        }
        .co-quan-2 {
            font-size: 13pt;
            display: inline-block;
            border-bottom: 1px solid black;
            padding-bottom: 2px;
            margin-bottom: 5pt;
        }
        .ngay-thang {
            text-align: center !important;
            margin: 0 !important;
        }
"""

html = html.replace('</style>', css_addition + '</style>')

# Fix Quốc Hiệu 1
html = html.replace('<p><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', '<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>')
html = html.replace('<p><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', '<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>')

# Fix Quốc Hiệu 2
html = html.replace('<p><strong>Độc lập - Tự do - Hạnh phúc</strong></p>', '<p class="quoc-hieu"><span class="quoc-hieu-2"><strong>Độc lập - Tự do - Hạnh phúc</strong></span></p>')
html = html.replace('<p><strong>Độc lập – Tự do – Hạnh phúc</strong></p>', '<p class="quoc-hieu"><span class="quoc-hieu-2"><strong>Độc lập - Tự do - Hạnh phúc</strong></span></p>')

# Fix Cơ Quan 1
html = html.replace('<p> VIỄN THÔNG PHÚ THỌ</p>', '<p class="co-quan-1">VIỄN THÔNG PHÚ THỌ</p>')
html = html.replace('<p>VIỄN THÔNG PHÚ THỌ</p>', '<p class="co-quan-1">VIỄN THÔNG PHÚ THỌ</p>')

# Fix Cơ Quan 2
html = html.replace('<p><strong>TRUNG TÂM HẠ TẦNG</strong></p>', '<p class="quoc-hieu"><span class="co-quan-2"><strong>TRUNG TÂM HẠ TẦNG</strong></span></p>')

# Fix Ngày tháng (nếu nó đang bị lệch)
html = html.replace('<p><em>Phú Thọ, ngày 28 tháng 4 năm 2026</em></p>', '<p class="ngay-thang"><em>Phú Thọ, ngày 28 tháng 4 năm 2026</em></p>')
html = html.replace('<p><em>                   Phú Thọ, ngày     tháng    năm 2026   </em></p>', '<p class="ngay-thang"><em>Phú Thọ, ngày ..... tháng ..... năm 2026</em></p>')

# Cập nhật các thẻ TD chứa tiêu đề nếu cần (Table layout của Header)
# Các table header không có padding/margin để căn chỉnh đẹp hơn
html = html.replace('<table class="layout-table"><tr><td><p class="co-quan-1">', '<table class="layout-table" style="margin-bottom: 20px;"><tr><td style="width: 40%; vertical-align: top;"><p class="co-quan-1">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
