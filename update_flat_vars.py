import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace variables
html = html.replace('{KhachHang.Tên khách hàng}', '{Tên khách hàng}')
html = html.replace('{KhachHang.Địa chỉ}', '{Địa chỉ}')
html = html.replace('{KhachHang.Mã số thuế}', '{Mã số thuế}')
html = html.replace('{KhachHang.Người đại diện}', '{Người đại diện}')
html = html.replace('{KhachHang.Số tài khoản}', '{Số tài khoản}')

# Also replace the hardcoded bank name with the new column {Tại Ngân hàng}
html = html.replace('Ngân hàng TMCP Ngoại thương Việt Nam – CN Vĩnh Phúc', '{Tại Ngân hàng}')
# Just in case there are variations of the bank name spelling:
html = html.replace('Ngân hàng TMCP Ngoại thương Việt Nam - CN Vĩnh Phúc', '{Tại Ngân hàng}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
