import re
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if match:
    print(match.group(1))
