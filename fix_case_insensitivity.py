import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_block = """                        const cleanKey = key.trim();
                        let val;
                        if (flatData[cleanKey] !== undefined) {
                            val = flatData[cleanKey];
                        } else if (flatData['KhachHang.' + cleanKey] !== undefined) {
                            val = flatData['KhachHang.' + cleanKey];
                        } else {
                            return '.........................';
                        }"""

new_block = """                        const cleanKey = key.trim().normalize("NFC").toLowerCase();
                        let val;
                        const actualKey = Object.keys(flatData).find(k => k.normalize("NFC").toLowerCase() === cleanKey);
                        const actualKhachHangKey = Object.keys(flatData).find(k => k.normalize("NFC").toLowerCase() === ('khachhang.' + cleanKey));
                        
                        if (actualKey) {
                            val = flatData[actualKey];
                        } else if (actualKhachHangKey) {
                            val = flatData[actualKhachHangKey];
                        } else {
                            return '.........................';
                        }"""

if old_block in html:
    html = html.replace(old_block, new_block)
else:
    print("WARNING: Could not find old block to replace.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("SUCCESS")
