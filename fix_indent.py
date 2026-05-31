import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the text-indent CSS rule
new_css = '''
        #contract-content p {
            text-indent: 1.27cm;
        }
        #contract-content p.quoc-hieu,
        #contract-content p.quoc-hieu-1,
        #contract-content p.co-quan-1,
        #contract-content p.title-center,
        #contract-content table p,
        #contract-content p[style*="text-align: right"],
        #contract-content p[style*="text-align: center"] {
            text-indent: 0;
        }
'''

# Insert it before the closing </style> tag
html = html.replace('</style>', new_css + '\n</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
