import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old Darden Family Heritage Mind Map Component section
old_mindmap_pattern = r'\s*<!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->.*?(?=\s*<!-- Add Family Member Modal -->)'
new_html = re.sub(old_mindmap_pattern, '\n\n', html, flags=re.DOTALL)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("[SUCCESS] Removed old text mindmap component from darden_family_tree.html")
