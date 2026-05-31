import re
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Tổ tổng hợp' in line or 'Vũ Thị Lan Phương' in line or 'Lê Văn Đức' in line or 'Nguyễn Đăng Minh' in line or 'Nguyễn Việt Hùng' in line:
        print(f'{i}: {line.strip()}')
