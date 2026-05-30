import os
import re

with open('hop_dong_mammoth.html', 'r', encoding='utf-8') as f:
    body_html = f.read()

# Replace specific static text with {} placeholders for dynamic rendering
replacements = {
    'Công ty TNHH TM thiết bị điện công nghiệp Vĩnh Phúc': '{KhachHang.Tên khách hàng}',
    'Số 231, đường Nguyễn Viết Xuân, Phường Vĩnh Phúc, Tỉnh Phú Thọ, Việt Nam': '{KhachHang.Địa chỉ}',
    '2500293679': '{KhachHang.Mã số thuế}',
    '0361001742938': '{KhachHang.Số tài khoản}',
    'Vũ Thị Bích Thúy': '{KhachHang.Người đại diện}',
    '26.384.775': '{GiaTriSauThue}',
    'Hai mươi sáu triệu ba trăm tám mươi bốn nghìn bảy trăm bảy mươi lăm đồng': '{BangChu}'
}

for old, new in replacements.items():
    body_html = body_html.replace(old, new)

# Thay thế thẻ table để không có viền cho các bảng layout
body_html = body_html.replace('<table>', '<table class="layout-table">')

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>In Hợp Đồng</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm 15mm;
        }}
        body {{
            font-family: "Times New Roman", Times, serif;
            font-size: 13pt;
            line-height: 1.5;
            color: #000;
            background: #fff;
            margin: 0;
            padding: 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10pt;
        }}
        table.data-table, table.data-table th, table.data-table td {{
            border: 1px solid black;
        }}
        td {{
            padding: 4px;
            vertical-align: top;
        }}
        p {{
            margin: 5pt 0;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin: 10pt 0 5pt 0;
        }}
        .page-break {{
            page-break-after: always;
        }}
        /* Tắt viền bảng đối với các bảng dùng để dàn layout (chữ ký, tiêu đề) */
        table.layout-table, table.layout-table td {{
            border: none !important;
        }}
        @media screen {{
            body {{
                max-width: 210mm;
                margin: 20px auto;
                padding: 20mm;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        }}
    </style>
</head>
<body>
    <div id="contract-content">
        {body_html}
    </div>

    <script>
        // Cấu hình URL API (giống admin.html)
        const APPS_SCRIPT_URL = window.APPS_SCRIPT_URL || "PASTE_WEB_APP_URL_HERE";

        async function loadDataAndPrint() {{
            const urlParams = new URLSearchParams(window.location.search);
            const id = urlParams.get('id');
            if (!id) {{
                alert("Không tìm thấy ID hồ sơ trong URL (ví dụ: ?id=HS001)");
                return;
            }}

            try {{
                document.title = "Đang tải dữ liệu...";
                // Gọi API lấy dữ liệu chi tiết
                const response = await fetch(`${{APPS_SCRIPT_URL}}?action=get&id=${{id}}`);
                const result = await response.json();
                
                if (result.status === "success") {{
                    const data = result.data;
                    let content = document.getElementById('contract-content').innerHTML;
                    
                    // Hàm đệ quy để map dữ liệu lồng nhau
                    const flattenObj = (ob) => {{
                        let result = {{}};
                        for (const i in ob) {{
                            if ((typeof ob[i]) === 'object' && !Array.isArray(ob[i])) {{
                                const temp = flattenObj(ob[i]);
                                for (const j in temp) {{
                                    result[i + '.' + j] = temp[j];
                                }}
                            }} else {{
                                result[i] = ob[i];
                            }}
                        }}
                        return result;
                    }};
                    
                    const flatData = flattenObj(data);

                    // Thay thế tất cả các chuỗi {{Key}} trong HTML
                    for (const key in flatData) {{
                        const regex = new RegExp(`\\\\{{${{key}}\\\\}}`, 'g');
                        content = content.replace(regex, flatData[key] || '');
                    }}

                    document.getElementById('contract-content').innerHTML = content;
                    document.title = "In Hợp Đồng - " + id;
                    
                    setTimeout(() => window.print(), 500);
                }} else {{
                    alert("Lỗi tải dữ liệu: " + result.message);
                }}
            }} catch (err) {{
                alert("Không thể kết nối tới server. Vui lòng kiểm tra lại link API.");
            }}
        }}

        window.onload = loadDataAndPrint;
    </script>
</body>
</html>
"""

os.makedirs('dashboard-sheets-expert/assets/dashboard-shell/vanilla', exist_ok=True)
out_path = 'dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_template)
print(f'Successfully wrote {out_path}')
