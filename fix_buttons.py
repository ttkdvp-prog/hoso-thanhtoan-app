import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS
css_addition = """
        @media print {
            .no-print { display: none !important; }
            body { box-shadow: none !important; margin: 0 !important; padding: 0 !important; max-width: 100% !important; }
        }
        .action-bar {
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }
        .action-bar button {
            padding: 10px 15px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-family: Arial, sans-serif;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            text-align: left;
        }
        .action-bar button:hover {
            background: #0056b3;
        }
        .action-bar button.pdf-btn { background: #dc3545; }
        .action-bar button.pdf-btn:hover { background: #a71d2a; }
        .action-bar button.doc-btn { background: #28a745; }
        .action-bar button.doc-btn:hover { background: #1e7e34; }
"""
html = html.replace('</style>', css_addition + '</style>')

# 2. Add HTML Action Bar
html_buttons = """
    <div class="action-bar no-print">
        <button onclick="window.print()">🖨️ In Hợp Đồng</button>
        <button class="pdf-btn" onclick="window.print()">📄 Xuất PDF</button>
        <button class="doc-btn" onclick="exportToDocx()">📝 Xuất DOCX</button>
    </div>
"""
html = html.replace('<body>', '<body>\n' + html_buttons)

# 3. Add JS function
js_addition = """
        function exportToDocx() {
            var header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' " +
                "xmlns:w='urn:schemas-microsoft-com:office:word' " +
                "xmlns='http://www.w3.org/TR/REC-html40'>" +
                "<head><meta charset='utf-8'><title>Export HTML to Word Document</title></head><body>";
            var footer = "</body></html>";
            var sourceHTML = header + document.getElementById("contract-content").innerHTML + footer;
            
            var source = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(sourceHTML);
            var fileDownload = document.createElement("a");
            document.body.appendChild(fileDownload);
            fileDownload.href = source;
            fileDownload.download = 'HopDong.doc';
            fileDownload.click();
            document.body.removeChild(fileDownload);
        }
"""
html = html.replace('</script>', js_addition + '\n    </script>')

# Update files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
