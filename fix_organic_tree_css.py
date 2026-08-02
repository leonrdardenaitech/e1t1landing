import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Bulletproof CSS with !important overrides for Organic Tree Mind Map
bulletproof_tree_css = '''
    /* Organic Leaf Tree Mind Map Engine - Bulletproof Overrides */
    .mindmap-container {
      background: linear-gradient(180deg, #092309 0%, #030a03 100%) !important;
      color: white !important;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
      padding: 30px !important;
      overflow-x: auto !important;
      min-height: 600px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }

    .tree {
      width: max-content !important;
      min-width: 100% !important;
      margin: 0 auto !important;
    }

    .tree ul {
      padding-top: 20px !important; 
      position: relative !important;
      display: flex !important;
      justify-content: center !important;
      transition: all 0.5s !important;
      margin: 0 !important;
      padding-left: 0 !important;
      list-style: none !important;
      list-style-type: none !important;
    }

    .tree li {
      float: left !important; 
      text-align: center !important;
      list-style-type: none !important;
      list-style: none !important;
      position: relative !important;
      padding: 20px 8px 0 8px !important;
      transition: all 0.5s !important;
      margin: 0 !important;
    }

    .tree li::before, .tree li::after {
      content: '' !important;
      position: absolute !important; 
      top: 0 !important; 
      right: 50% !important;
      border-top: 3px solid #5a8231 !important;
      width: 50% !important; 
      height: 20px !important;
      z-index: 1 !important;
    }

    .tree li::after {
      right: auto !important; 
      left: 50% !important;
      border-left: 3px solid #5a8231 !important;
    }

    .tree li:only-child::after, .tree li:only-child::before {
      display: none !important;
    }

    .tree li:only-child { 
      padding-top: 0 !important;
    }

    .tree li:first-child::before, .tree li:last-child::after {
      border: 0 none !important;
    }

    .tree li:last-child::before {
      border-right: 3px solid #5a8231 !important;
      border-radius: 0 5px 0 0 !important;
    }

    .tree li:first-child::after {
      border-radius: 5px 0 0 0 !important;
    }

    .tree ul ul::before {
      content: '' !important;
      position: absolute !important; 
      top: 0 !important; 
      left: 50% !important;
      border-left: 3px solid #5a8231 !important;
      width: 0 !important; 
      height: 20px !important;
      z-index: 1 !important;
    }

    .tree div.leaf {
      border: 2px solid #3d6e1d !important;
      padding: 10px 18px !important;
      text-decoration: none !important;
      color: #d1ffd1 !important;
      background: #184018 !important;
      font-size: 13px !important;
      font-weight: bold !important;
      display: inline-block !important;
      border-radius: 0 25px 0 25px !important; 
      transition: all 0.3s ease !important;
      cursor: pointer !important;
      box-shadow: 3px 3px 12px rgba(0,0,0,0.8) !important;
      white-space: nowrap !important;
      position: relative !important;
      z-index: 2 !important;
    }

    .tree div.leaf:hover {
      background: #2a6b2a !important;
      color: #ffffff !important;
      border-color: #71b835 !important;
      transform: scale(1.08) !important;
      box-shadow: 0 0 15px rgba(113, 184, 53, 0.6) !important;
    }

    .tree div.leaf.root-leaf {
      background: linear-gradient(135deg, #15803d, #047857) !important;
      border-color: #f59e0b !important;
      color: #fef08a !important;
      font-size: 15px !important;
      padding: 14px 24px !important;
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.5) !important;
    }

    .tree div.leaf.gen2-leaf {
      background: #064e3b !important;
      border-color: #34d399 !important;
      color: #a7f3d0 !important;
    }

    .tree div.leaf.blended-leaf {
      background: #3b0764 !important;
      border-color: #c084fc !important;
      color: #f3e8ff !important;
    }

    .leaf-hidden {
      display: none !important;
    }
'''

# Replace old Organic Leaf Tree Mind Map Engine CSS with Bulletproof CSS
old_css_pattern = re.compile(r'/\* Organic Leaf Tree Mind Map Engine \*/.*?\n\s*\.leaf-hidden\s*\{\s*display:\s*none;\s*\}', re.DOTALL)
if 'Organic Leaf Tree Mind Map Engine' in html:
    html = old_css_pattern.sub(bulletproof_tree_css.strip(), html, count=1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully applied bulletproof !important CSS rules to Organic Leaf Tree in darden_family_tree.html!')
