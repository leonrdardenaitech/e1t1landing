import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build Clean Mind Map Component
mindmap_clean_html = '''    <!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->
    <div class="w-full max-w-7xl mx-auto my-10 px-4">
      <div class="scrim-box p-6 md:p-8 rounded-2xl border-2 border-amber-500/60 shadow-[0_0_40px_rgba(245,158,11,0.3)] relative overflow-hidden bg-black/95">
        
        <!-- Mind Map Header & Controls -->
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-gray-800 pb-4 mb-6 gap-4">
          <div class="flex items-center gap-3">
            <span class="text-3xl text-amber-400">🧠</span>
            <div>
              <h3 class="font-cyber text-2xl text-white font-extrabold uppercase tracking-wider">
                DARDEN FAMILY HERITAGE <span class="text-amber-400">MIND MAP</span>
              </h3>
              <p class="font-mono-code text-xs text-gray-400 tracking-wider mt-0.5">
                Scalable Generational Network (Gen 1 → Gen 6) · Click Any Node to Inspect or Edit
              </p>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-2">
            <button onclick="zoomMindmap(0.15)" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 px-3.5 py-2 rounded font-mono-code text-xs">
              🔍 Zoom In
            </button>
            <button onclick="zoomMindmap(-0.15)" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 px-3.5 py-2 rounded font-mono-code text-xs">
              🔍 Zoom Out
            </button>
            <button onclick="resetMindmapZoom()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 px-3.5 py-2 rounded font-mono-code text-xs">
              🔄 Reset View
            </button>
            <button onclick="openMindmapModal()" class="bg-gradient-to-r from-amber-600 to-yellow-500 hover:from-amber-500 hover:to-yellow-400 text-black font-cyber font-bold text-xs px-5 py-2 rounded uppercase tracking-wider shadow-lg">
              ⛶ Fullscreen View
            </button>
          </div>
        </div>

        <!-- Mind Map Viewport Container -->
        <div class="w-full h-[540px] bg-black/95 rounded-xl border border-gray-800 overflow-auto relative p-6 cursor-grab active:cursor-grabbing reticle" id="mindmapViewport">
          <div id="mindmapTreeContainer" class="min-w-[1100px] flex flex-col items-center space-y-8 transition-transform duration-200 transform origin-top">
            
            <!-- ROOT NODE: Sam Darden Sr. & Freddie Shields -->
            <div class="flex flex-col items-center">
              <div class="bg-gradient-to-r from-amber-600 via-yellow-400 to-amber-300 text-black p-4 rounded-2xl shadow-[0_0_30px_rgba(245,158,11,0.6)] border-2 border-yellow-200 text-center font-cyber cursor-pointer" onclick="openMemberModal('Sam Darden Sr. & Freddie Shields', 'Gen 1 Founders')">
                <span class="text-3xl block mb-1">👑</span>
                <h4 class="font-black text-xl uppercase tracking-wider">Sam Darden Sr. &amp; Freddie Shields</h4>
                <span class="text-[10px] font-mono-code bg-black/80 text-yellow-300 px-3 py-0.5 rounded-full inline-block mt-1">GEN 1 ROOT FOUNDERS</span>
              </div>
              <div class="w-0.5 h-8 bg-amber-500/60 my-1"></div>
            </div>

            <!-- GEN 2 BRANCH NODES (6 CHILDREN) -->
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4 w-full text-center font-mono-code text-xs">
              
              <!-- 1. Sam Jr. -->
              <div class="bg-blue-950/90 p-3.5 rounded-xl border border-blue-500/60 shadow-md flex flex-col items-center">
                <span class="text-amber-400 font-bold font-cyber text-sm">🤠 Sam Jr. ("Cowboy")</span>
                <span class="text-[9px] text-blue-300 block my-1">Son · 5 Household Lines</span>
                <button onclick="openMemberModal('Sam Darden Jr.', 'Gen 2 Branch')" class="mt-2 text-[10px] bg-blue-900/80 border border-blue-400 text-blue-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

              <!-- 2. Mozzell -->
              <div class="bg-blue-950/90 p-3.5 rounded-xl border border-blue-500/60 shadow-md flex flex-col items-center">
                <span class="text-amber-400 font-bold font-cyber text-sm">👴 Mozzell Darden</span>
                <span class="text-[9px] text-blue-300 block my-1">First Son · 7 Lines</span>
                <button onclick="openMemberModal('Mozzell Darden', 'Gen 2 Branch')" class="mt-2 text-[10px] bg-blue-900/80 border border-blue-400 text-blue-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

              <!-- 3. Johnnie -->
              <div class="bg-purple-950/90 p-3.5 rounded-xl border border-purple-500/60 shadow-md flex flex-col items-center">
                <span class="text-purple-300 font-bold font-cyber text-sm">👵 Johnnie Watson</span>
                <span class="text-[9px] text-purple-300 block my-1">Daughter · 7 Lines</span>
                <button onclick="openMemberModal('Johnnie Watson', 'Gen 2 Branch')" class="mt-2 text-[10px] bg-purple-900/80 border border-purple-400 text-purple-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

              <!-- 4. Peggy -->
              <div class="bg-yellow-950/90 p-3.5 rounded-xl border border-yellow-500/60 shadow-md flex flex-col items-center">
                <span class="text-yellow-400 font-bold font-cyber text-sm">👵 Peggy Owens</span>
                <span class="text-[9px] text-yellow-300 block my-1">Matriarch Line</span>
                <button onclick="openMemberModal('Peggy Owens', 'Gen 2 Matriarch')" class="mt-2 text-[10px] bg-yellow-900/80 border border-yellow-400 text-yellow-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

              <!-- 5. Lovell -->
              <div class="bg-emerald-950/90 p-3.5 rounded-xl border border-emerald-500/60 shadow-md flex flex-col items-center">
                <span class="text-emerald-400 font-bold font-cyber text-sm">👨 Lovell Darden</span>
                <span class="text-[9px] text-emerald-300 block my-1">Living Elder</span>
                <button onclick="openMemberModal('Lovell Darden', 'Gen 2 Living Elder')" class="mt-2 text-[10px] bg-emerald-900/80 border border-emerald-400 text-emerald-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

              <!-- 6. Sarah -->
              <div class="bg-blue-950/90 p-3.5 rounded-xl border border-blue-500/60 shadow-md flex flex-col items-center">
                <span class="text-blue-300 font-bold font-cyber text-sm">👩 Sarah Darden</span>
                <span class="text-[9px] text-blue-300 block my-1">Daughter</span>
                <button onclick="openMemberModal('Sarah Darden', 'Gen 2 Branch')" class="mt-2 text-[10px] bg-blue-900/80 border border-blue-400 text-blue-200 px-2.5 py-1 rounded">✏️ Inspect / Edit</button>
              </div>

            </div>

            <!-- GEN 3 TO GEN 6 SUBNODE PREVIEW MAP -->
            <div class="w-full bg-gray-950 p-5 rounded-xl border border-gray-800 text-left font-mono-code text-xs space-y-3">
              <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                <span class="text-amber-400 font-bold">🌿 GEN 3 → GEN 6 DRILL-DOWN NETWORK</span>
                <span class="text-gray-400 text-[10px]">SCALABLE MAP NODES</span>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-[11px]">
                <div class="bg-black/90 p-3 rounded border border-gray-800">
                  <span class="text-amber-300 font-bold block mb-1">🤠 SAM JR. SUB-NODES</span>
                  <p class="text-gray-300 leading-relaxed">• Ronnie (Leon, Bikila → Asar, Sariah, Khalil)<br>• Bobby/Bill (Billy, Kim)<br>• Darrell (Darrell Jr, Harold, Keisha)</p>
                </div>

                <div class="bg-black/90 p-3 rounded border border-gray-800">
                  <span class="text-amber-300 font-bold block mb-1">👴 MOZZELL SUB-NODES</span>
                  <p class="text-gray-300 leading-relaxed">• Bernard (Beverly, Latasha, Larry)<br>• Mozzell Jr. (Mozzell 3rd, Kattely, Lisa)<br>• Derrick, Carol, Sheila, Mary, Lolita</p>
                </div>

                <div class="bg-black/90 p-3 rounded border border-gray-800">
                  <span class="text-yellow-400 font-bold block mb-1">👵 PEGGY SUB-NODES</span>
                  <p class="text-gray-300 leading-relaxed">• Derrick Owens (Aaron, Marques, Stephan, Darnielle)<br>• Debra Profitt (Jamila, Jewels → Ashley, Alani)</p>
                </div>

                <div class="bg-black/90 p-3 rounded border border-gray-800">
                  <span class="text-purple-300 font-bold block mb-1">👵 JOHNNIE SUB-NODES</span>
                  <p class="text-gray-300 leading-relaxed">• Irving (Erika, Joel)<br>• Darlene (Ronyelle, Eric, Melinda)<br>• Donna (Thomas Jr, Devin, Joy, Jayson)</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>'''

# Replace old Gen 5 & 6 section or old mindmap duplicates
pattern = re.compile(r'<!-- OVERARCHING COLLAPSIBLE WINDOW: GEN 5 & GEN 6 ARCHIVES -->.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
if 'OVERARCHING COLLAPSIBLE WINDOW' in html:
    html = pattern.sub(mindmap_clean_html, html, count=1)
else:
    html = html.replace('</div><!-- end gen3-carousel -->', '</div><!-- end gen3-carousel -->\n\n' + mindmap_clean_html, 1)

# Remove any extra duplicate section if present
second_mindmap = html.find('<!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->', html.find('<!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->') + 1)
if second_mindmap != -1:
    end_second = html.find('</section>', second_mindmap)
    if end_second != -1:
        html = html[:second_mindmap] + html[end_second+10:]

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully swapped Mind Map into primary position below Gen 3 Carousel!')
