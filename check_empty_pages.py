import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'<div class="page-break"></div>', html))
for i in range(len(matches)-1):
    start = matches[i].end()
    end = matches[i+1].start()
    content = html[start:end]
    clean_content = re.sub(r'<[^>]+>', '', content).strip()
    if not clean_content:
        print(f'Empty content between break {i+1} and {i+2}')
    print(f'Length of content between {i+1} and {i+2}: {len(content)}, clean text length: {len(clean_content)}')

print('Number of breaks:', len(matches))
