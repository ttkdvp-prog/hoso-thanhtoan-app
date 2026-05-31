import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find <table class="layout-table"...> that contains "CỘNG HÒA"
# We match `<table class="layout-table"[^>]*>...CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM...</table>`
pattern = r'(<table class="layout-table"[^>]*>(?:(?!</table).)*?CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM(?:(?!</table).)*?</table>)'

def add_break(match):
    # Check if there is already a page-break before this table
    # We can't check what precedes it easily with just this match, so we will prepend it and then deduplicate
    return '<div class="page-break"></div>\n' + match.group(1)

html = re.sub(pattern, add_break, html, flags=re.DOTALL)

# Deduplicate page breaks
html = re.sub(r'(<div class="page-break"></div>\s*)+', '<div class="page-break"></div>\n', html)

# Remove page break if it's the very first thing in the body
# Assuming it might be at the very start of the file or after <body> tag
if html.strip().startswith('<div class="page-break"></div>'):
    html = html.replace('<div class="page-break"></div>\n', '', 1)

# Wait, there might be other standalone "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" that are not in tables.
# E.g. "BIÊN BẢN NGHIỆM THU BÀN GIAO"
# Let's ensure they have page breaks too.
pattern2 = r'(<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>)'
def add_break_p(match):
    return '<div class="page-break"></div>\n' + match.group(1)

# Temporarily remove all page breaks before standalone CỘNG HÒA to avoid duplicates
html = re.sub(r'<div class="page-break"></div>\s*<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>',
              r'<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html)

# Now add them back, BUT ONLY if they are NOT inside a table cell (<td>)
# We can do this by splitting the HTML by <td> and </td>, but regex is tricky.
# Wait, actually, if it is inside a table cell, it shouldn't have a page break directly before it ANYWAY.
# Because if it's inside a table cell, the page break should be before the TABLE!
# And we just added page breaks before ALL tables containing CỘNG HÒA!
# So for standalone ones, we can just do a regex replace, but we need to avoid adding breaks if it's inside a <td>.
# A simple way: find all CỘNG HÒA, if preceded by <td> or >\s*, it's in a cell.
# Let's use lookbehind:
html = re.sub(r'(?<!<td>)(?<!<td style="[^"]*">)(?<!<td style=\'[^\']*\'>)(?<!<td class="[^"]*">)\s*<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>',
              r'\n<div class="page-break"></div>\n<p class="quoc-hieu quoc-hieu-1"><strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong></p>', html)

# Clean up any potential double breaks again
html = re.sub(r'(<div class="page-break"></div>\s*)+', '<div class="page-break"></div>\n', html)

# Remove the very first page break if it's at the beginning of the file
html = re.sub(r'^\s*<div class="page-break"></div>\n', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
