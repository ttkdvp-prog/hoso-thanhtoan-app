import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the block
old_block = """                    // Tự động lấy dữ liệu từ AppSheet để điền vào tất cả các chỗ {...}
                    content = content.replace(/\\{([^{}]+)\\}/g, function(match, key) {
                        // Tìm kiếm linh hoạt, kể cả khi sai khác khoảng trắng
                        const cleanKey = key.trim();
                        if (flatData[cleanKey] !== undefined) return flatData[cleanKey];
                        // Tìm thử theo KhachHang.Key nếu thiếu
                        if (flatData['KhachHang.' + cleanKey] !== undefined) return flatData['KhachHang.' + cleanKey];
                        // Mặc định trả về dấu ... nếu không tìm thấy dữ liệu
                        return '.........................';
                    });"""

new_block = """                    // Tự động lấy dữ liệu từ AppSheet để điền vào tất cả các chỗ {...}
                    content = content.replace(/\\{([^{}]+)\\}/g, function(match, key) {
                        const cleanKey = key.trim();
                        let val;
                        if (flatData[cleanKey] !== undefined) {
                            val = flatData[cleanKey];
                        } else if (flatData['KhachHang.' + cleanKey] !== undefined) {
                            val = flatData['KhachHang.' + cleanKey];
                        } else {
                            return '.........................';
                        }
                        
                        // Tự động format định dạng ngày tháng (ISO 8601 từ Google Sheets) sang dạng dd/mm/yyyy
                        if (typeof val === 'string' && /^\\d{4}-\\d{2}-\\d{2}T/.test(val)) {
                            const d = new Date(val);
                            const dd = String(d.getDate()).padStart(2, '0');
                            const mm = String(d.getMonth() + 1).padStart(2, '0');
                            const yyyy = d.getFullYear();
                            return `${dd}/${mm}/${yyyy}`;
                        }
                        
                        return val;
                    });"""

if old_block in html:
    html = html.replace(old_block, new_block)
else:
    print("WARNING: Old block not found exactly as written.")
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
