import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace "Tổ tổng hợp" and "Tổ Tổng hợp" with {Tổ trình}
html = re.sub(r'Tổ tổng hợp|Tổ Tổng hợp', '{Tổ trình}', html)

# Replace "Vũ Thị Lan Phương" with {Tổ trưởng}
html = html.replace('Vũ Thị Lan Phương', '{Tổ trưởng}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
