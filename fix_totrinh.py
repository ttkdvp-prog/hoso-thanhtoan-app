import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the "Ý kiến chỉ đạo" box
old_box = r'''<table class="layout-table"><tr><td><p><strong>Ý kiến chỉ đạo của Lãnh đạo Trung tâm Hạ tầng</strong></p><li><em>Nội dung:</em></li><li><em>Thời gian hoàn thành:</em></li></td></tr></table>'''
new_box = r'''<table style="width: 100%; border: 1px solid black; border-collapse: collapse; margin-bottom: 20px;">
<tr>
<td style="padding: 15px; border: 1px solid black;">
<p class="title-center"><strong>Ý kiến chỉ đạo của Lãnh đạo Trung tâm Hạ tầng</strong></p>
<br>
<p>- <em>Nội dung:</em></p>
<br><br><br>
<p>- <em>Thời gian hoàn thành:</em></p>
<br>
</td>
</tr>
</table>'''
html = html.replace(old_box, new_box)

# Just in case the formatting is slightly different, let's use regex
box_pattern = r'<table class="layout-table">\s*<tr>\s*<td>\s*<p>\s*<strong>Ý kiến chỉ đạo của Lãnh đạo Trung tâm Hạ tầng</strong>\s*</p>\s*<li>\s*<em>Nội dung:</em>\s*</li>\s*<li>\s*<em>Thời gian hoàn thành:</em>\s*</li>\s*</td>\s*</tr>\s*</table>'
html = re.sub(box_pattern, new_box, html)

# 2. Fix the layout-table to data-table for the Tờ trình table
# The table starts with <table class="layout-table"><thead><tr><th rowspan="2"><p><strong>STT</strong></p></th>
html = re.sub(r'<table class="layout-table">(\s*<thead>\s*<tr>\s*<th[^>]*>\s*<p>\s*<strong>STT</strong>)', r'<table class="data-table">\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
