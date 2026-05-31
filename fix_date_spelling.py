import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_code = "document.getElementById('contract-content').innerHTML = content;"
new_code = """                    // Chuyển đổi "ngày dd/mm/yyyy" thành "ngày d tháng m năm yyyy"
                    content = content.replace(/ngày\\s+(\\d{1,2})\\/(\\d{1,2})\\/(\\d{4})/g, function(match, d, m, y) {
                        return `ngày ${parseInt(d, 10)} tháng ${parseInt(m, 10)} năm ${y}`;
                    });

                    document.getElementById('contract-content').innerHTML = content;"""

if old_code in html:
    html = html.replace(old_code, new_code)
else:
    print("WARNING: Could not find target code in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("SUCCESS")
