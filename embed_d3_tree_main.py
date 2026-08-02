import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure D3.js script CDN is in head
if 'cdn.jsdelivr.net/npm/d3@7' not in html:
    html = html.replace('</head>', '  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>\n</head>', 1)

# Mind Map Section Container HTML in darden_family_tree.html
visual_mindmap_section = '''  <!-- ============================================================ -->
  <!-- D3.JS INTERACTIVE VISUAL MIND MAP GRAPH (NOTEBOOKLM STYLE)   -->
  <!-- ============================================================ -->
  <section class="w-full max-w-7xl mx-auto my-10 px-4">
    <div class="scrim-box p-6 md:p-8 rounded-2xl border-2 border-amber-500/60 shadow-[0_0_50px_rgba(245,158,11,0.35)] relative overflow-hidden bg-black/95">
      
      <!-- Mind Map Header & Controls -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-amber-500/30 pb-4 mb-6 gap-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl text-amber-400">🧠</span>
          <div>
            <h3 class="font-cyber text-2xl text-white font-extrabold uppercase tracking-wider">
              DARDEN FAMILY HERITAGE <span class="text-amber-400">VISUAL MIND MAP</span>
            </h3>
            <p class="font-mono-code text-xs text-amber-300/80 tracking-wider mt-0.5">
              Generation I (Root Ancestors: Sam Darden Sr. &amp; Freddie Shields) → Generation VI Descendants
            </p>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-2">
          <button onclick="expandAllNodes()" class="bg-amber-500 hover:bg-amber-400 text-black font-cyber font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-md">
            ➕ Expand All Branches
          </button>
          <button onclick="collapseDeepNodes()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 font-bold text-xs px-3.5 py-2 rounded-lg transition-all">
            ➖ Collapse Deep (Gens 4-6)
          </button>
          <button onclick="resetZoom()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 font-bold text-xs px-3.5 py-2 rounded-lg transition-all">
            🔄 Reset View
          </button>
          <a href="darden_family_tree_v2.html" target="_blank" class="bg-gradient-to-r from-amber-600 to-yellow-500 text-black font-cyber font-bold text-xs px-4 py-2 rounded-lg uppercase tracking-wider shadow-lg flex items-center gap-1">
            ⛶ Open Standalone v2 HTML ↗
          </a>
        </div>
      </div>

      <!-- Legend -->
      <div class="flex flex-wrap gap-4 items-center justify-between text-xs font-mono-code mb-4 p-3 bg-black/80 rounded-xl border border-gray-800">
        <div class="flex items-center gap-2">
          <span class="w-3.5 h-3.5 rounded-md bg-[#a7f3d0] border border-[#059669]"></span>
          <span class="text-emerald-300 font-bold">Gen 1: Sam Darden Sr. &amp; Freddie Shields</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3.5 h-3.5 rounded-md bg-[#86efac] border border-[#16a34a]"></span>
          <span class="text-green-300 font-bold">Gen 2: 6 Main Branches</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3.5 h-3.5 rounded-md bg-[#38bdf8] border border-[#0284c7]"></span>
          <span class="text-sky-300 font-bold">💙 Direct Bloodline</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3.5 h-3.5 rounded-md bg-[#c084fc] border border-[#9333ea]"></span>
          <span class="text-purple-300 font-bold">💜 Spouses &amp; Extensions</span>
        </div>
        <div class="text-amber-400 font-bold">
          💡 Click Badge Circles (&lt; / &gt;) to Expand or Collapse Branches
        </div>
      </div>

      <!-- SVG Graph Canvas -->
      <div id="mindmapSvgContainer" class="w-full h-[720px] bg-black/95 rounded-xl border border-amber-500/40 relative overflow-hidden cursor-grab active:cursor-grabbing"></div>
    </div>
  </section>'''

# Replace old mindmap section in darden_family_tree.html
old_section_pattern = re.compile(r'<!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->.*?<!-- FULLSCREEN MIND MAP POP-UP MODAL -->', re.DOTALL)
if 'DARDEN FAMILY HERITAGE MIND MAP COMPONENT' in html:
    html = old_section_pattern.sub(visual_mindmap_section + '\n\n  <!-- FULLSCREEN MIND MAP POP-UP MODAL -->', html, count=1)
elif '<section class="w-full max-w-7xl mx-auto my-10 px-4">' in html:
    # Replace that section directly
    sec_start = html.find('<!-- DARDEN FAMILY HERITAGE MIND MAP')
    if sec_start != -1:
        sec_end = html.find('</section>', sec_start)
        html = html[:sec_start] + visual_mindmap_section + html[sec_end+10:]

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully embedded visual SVG Mind Map canvas into darden_family_tree.html!')
