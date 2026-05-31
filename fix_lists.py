import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Điều 5 list items:
# <ul><li>text</li></ul> -> <p>- text</p>
# Since there might be multiple ul/li we only want to fix them generically if they represent standard text.
# Actually, looking at the whole document, almost all ul/li are converted poorly from Word and should be just paragraphs.
# Let's replace <ul> and </ul> with nothing, and <li> with <p>- and </li> with </p>.

# Specifically for Điều 6:
# <ul><li><ol><li> text </li><li> text </li></ol></li></ul>
# We want to replace the whole block with <p>1. text</p><p>2. text</p>

# Let's target Điều 6 first to be safe:
dieu6_old = """<ul><li><ol><li> Thời hạn bảo hành: Theo quy định của hãng sản xuất.</li><li> Điều kiện bảo hành: Điều kiện bảo hành sản phẩm tuân thủ theo đúng các quy định và điều kiện của nhà sản xuất áp dụng cho thị trường Việt Nam. </li></ol></li></ul>"""
# The exact HTML might have slightly different spacing, so regex is better:
html = re.sub(r'<ul>\s*<li>\s*<ol>\s*<li>\s*(Thời hạn bảo hành.*?)\s*</li>\s*<li>\s*(Điều kiện bảo hành.*?)\s*</li>\s*</ol>\s*</li>\s*</ul>', 
              r'<p>1. \1</p>\n<p>2. \2</p>', html, flags=re.DOTALL)

# For Điều 5, let's find all <ul><li> blocks and convert them to <p>- ...</p>
# It's safer to just replace all <li> inside <ul> that don't have <ol> inside them.
# We'll just replace <li> with <p>- 
# and </li> with </p>
# and remove <ul> and </ul>.

# But wait! If there are other lists, this might break them. 
# Let's specifically target the text of Điều 5.
dieu5_text = [
    "Thanh toán đúng thời hạn như đã quy định ở Điều 3.",
    "Từ chối thanh toán trong trường hợp Bên B giao hàng không đúng chất lượng, chủng loại theo đúng yêu cầu.",
    "Yêu cầu Bên B bồi thường đối với những thiệt hại thực tế, phát sinh trong trường hợp Bên B vi phạm các nghĩa vụ được quy định trong Hợp đồng này.",
    "Thông báo về số lượng, chủng loại hàng hoá cho Bên B tối thiểu 48 giờ trước thời gian nhận hàng nếu có thay đổi so với hợp đồng đã ký.",
    "Chuẩn bị mặt bằng vị trí tập kết giúp Bên B giao hàng và giải phóng hàng kịp tiến độ.",
    "Yêu cầu Bên A thanh toán đúng thời hạn.",
    "Tiến hành cung ứng đủ chủng loại, số lượng hàng hoá đảm bảo chất lượng như được quy định về quy cách và chất lượng sản phẩm theo Điều 2 của Hợp đồng này."
]

for text in dieu5_text:
    # Escape special characters
    safe_text = re.escape(text)
    # Replace <li>text</li> with <p>- text</p>
    html = re.sub(r'<li>\s*' + safe_text + r'\s*</li>', r'<p>- ' + text + r'</p>', html)

# Now remove any empty <ul> and </ul> that might be left behind around these paragraphs.
# Instead of doing that, let's just globally replace <ul> and </ul> with empty strings since there are no other legitimate lists that need ul styling. 
# Actually, the replacement above put <p> inside <ul>. So <ul><p>...</p></ul>.
# We can safely remove all <ul> and </ul> tags in the document because in legal documents, lists are typically just paragraphs starting with "- " or "1. ".
html = html.replace('<ul>', '')
html = html.replace('</ul>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
