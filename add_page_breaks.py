import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to make sure every National Motto block has a <div class="page-break"></div> BEFORE it.
# Except maybe the very first one.

# Let's just find all <p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>
# and check if there's a page-break before it.
# If not, add one. 
# Wait, let's just do a blanket replacement.
# But what if there's already one? We don't want duplicate page breaks.

# First, remove ALL page-breaks that are IMMEDIATELY followed by the National Motto.
html = re.sub(r'<div class="page-break"></div>\s*<p class="quoc-hieu quoc-hieu-1">\s*<strong>CỘNG HO?À XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*</strong>\s*</p>', 
              r'<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html, flags=re.IGNORECASE)

# Now, add a page break before ALL National Mottos.
html = re.sub(r'<p class="quoc-hieu quoc-hieu-1">\s*<strong>CỘNG HO?À XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*</strong>\s*</p>', 
              r'<div class="page-break"></div>\n<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html, flags=re.IGNORECASE)

# EXCEPT the very first one! 
# We can just remove the very first page break.
html = html.replace('<div class="page-break"></div>', '', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
