import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'<div class="page-break"></div>\s*<table class="layout-table" style="margin-bottom: 20px;">', html)
print('Found', len(matches), 'page breaks before layout tables')

matches_all = re.findall(r'<table class="layout-table" style="margin-bottom: 20px;">', html)
print('Found', len(matches_all), 'layout tables total')
