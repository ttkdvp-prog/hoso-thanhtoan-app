import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove page breaks that are inside <td> elements right before the National Motto
# Wait, it's easier: if <div class="page-break"></div> is immediately preceded by <td...> or <td> or </td><td>
# We should move the page break to BEFORE the <table> instead of inside the <td>.
# But there's ALREADY a <div class="page-break"></div> before the table in some cases!
# Let's see:
# <div class="page-break"></div><table class="layout-table" style="margin-bottom: 20px;"><tr><td style="width: 40%; vertical-align: top;"><p class="co-quan-1">VIỄN THÔNG PHÚ THỌ</p><p class="quoc-hieu"><span class="co-quan-2"><strong>TRUNG TÂM HẠ TẦNG</strong></span></p></td><td><div class="page-break"></div>

# Yes, there's already a page break before the table! So the one inside the <td> is just causing a blank page.
# We can safely delete any <div class="page-break"></div> that is IMMEDIATELY preceded by <td> or >\s*
# Let's just find `<td><div class="page-break"></div>` and replace it with `<td>`
html = re.sub(r'<td[^>]*>\s*<div class="page-break"></div>', lambda m: m.group(0).replace('<div class="page-break"></div>', ''), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed")
