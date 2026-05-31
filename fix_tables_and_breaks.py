import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix CSS table page-break
# Replace:
# table { page-break-inside: avoid; break-inside: avoid; 
#     width: 100%;
#     border-collapse: collapse;
#     margin-bottom: 10pt;
# }
css_old = r'table\s*\{\s*page-break-inside:\s*avoid;\s*break-inside:\s*avoid;\s*width:\s*100%;\s*border-collapse:\s*collapse;\s*margin-bottom:\s*10pt;\s*\}'
css_new = r'''table { 
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10pt;
        }
        tr {
            page-break-inside: avoid; break-inside: avoid;
        }'''
html = re.sub(css_old, css_new, html)

# 2. Fix layout-table to data-table for actual data tables
# Find <table class="layout-table"> that contains STT in the first row.
# We will use regex to find `<table class="layout-table">` that is immediately followed by `<thead><tr><th>` or `<tr><td>` and then STT.
html = re.sub(r'<table class="layout-table">(\s*<thead>\s*<tr>\s*<th>\s*<p>\s*<strong>STT</strong>)', r'<table class="data-table">\1', html)
html = re.sub(r'<table class="layout-table">(\s*<tr>\s*<td>\s*<p>\s*<strong>STT</strong>)', r'<table class="data-table">\1', html)

# 3. Add page break before BÁO GIÁ
html = re.sub(r'(<div class="page-break"></div>)?\s*<p[^>]*><strong>BÁO GIÁ</strong></p>', r'<div class="page-break"></div>\n<p><strong>BÁO GIÁ</strong></p>', html)

# 4. Add page break before ANY CỘNG HÒA or CỘNG HOÀ (if not already there)
# First remove any existing ones to avoid duplicates
html = re.sub(r'<div class="page-break"></div>\s*<p class="quoc-hieu quoc-hieu-1">\s*<strong>CỘNG H[OÒ][AÀ] XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*</strong>\s*</p>', 
              r'<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html, flags=re.IGNORECASE)

html = re.sub(r'<p class="quoc-hieu quoc-hieu-1">\s*<strong>CỘNG H[OÒ][AÀ] XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*</strong>\s*</p>', 
              r'<div class="page-break"></div>\n<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html, flags=re.IGNORECASE)

# Remove the very first page break
html = html.replace('<div class="page-break"></div>', '', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
