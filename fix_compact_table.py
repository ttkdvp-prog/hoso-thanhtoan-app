import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_addition = """
        table.compact-table p {
            margin: 1pt 0;
        }
        table.compact-table td {
            padding: 2px;
        }
"""

html = html.replace('</style>', css_addition + '</style>')
html = html.replace('<table class="data-table" style="line-height: 1.0; font-size: 13pt;">', '<table class="data-table compact-table" style="line-height: 1.0; font-size: 12pt;">')

# Cập nhật cả file template expert
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
