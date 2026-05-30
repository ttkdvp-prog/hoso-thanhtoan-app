import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('''        h1, h2, h3, h4, h5, h6 {
            margin: 10pt 0 5pt 0;
        }''', '''        h1, h2, h3, h4, h5, h6 {
            margin: 5pt 0;
            font-size: 13pt;
            font-weight: bold;
            font-family: inherit;
        }''')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
