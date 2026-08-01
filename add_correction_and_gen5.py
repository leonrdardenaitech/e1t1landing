import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Correction Zone Banner HTML
correction_zone_html = '''  <!-- CORRECTION ZONE & ADD A DARDEN ANNOUNCEMENT BANNER -->
  <section class="w-full max-w-7xl mx-auto my-6 px-4">
    <div class="bg-gradient-to-r from-amber-950/90 via-black to-purple-950/90 border-2 border-amber-500/60 rounded-2xl p-6 shadow-[0_0_30px_rgba(245,158,11,0.3)]">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-amber-500/30 pb-4 mb-4 gap-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl">✏️</span>
          <div>
            <h3 class="font-cyber text-xl md:text-2xl text-amber-300 font-extrabold uppercase tracking-wider">
              CORRECTION ZONE &amp; ADD A DARDEN
            </h3>
            <p class="font-mono-code text-xs text-amber-400/80 tracking-widest uppercase">
              Submit Name Fixes &amp; Add New Bloodline Descendants Directly to Family Archives
            </p>
          </div>
        </div>
        <div class="flex gap-2">
          <button onclick="openMemberModal('', 'Correction')" class="bg-amber-500 text-black hover:bg-amber-400 font-cyber font-bold text-xs px-4 py-2 rounded-lg uppercase tracking-wider shadow-md transition-all">
            ✏️ Submit Correction
          </button>
          <button onclick="openMemberModal('', 'Add A Darden')" class="bg-purple-900 border border-purple-400 text-purple-200 hover:bg-purple-800 font-cyber font-bold text-xs px-4 py-2 rounded-lg uppercase tracking-wider transition-all">
            ➕ Add A Darden
          </button>
        </div>
      </div>
      
      <p class="text-xs md:text-sm text-gray-200 font-sans leading-relaxed italic">
        "Correction Zone: I apologize if I spelled your name wrong, missed a middle initial, or omitted a family branch member—let's correct that now! Submit the right info using the form below and it will save directly to our Darden Family Spreadsheet archives. I will visually update the site layout as soon as possible to keep our lineage 100% accurate."
      </p>
    </div>
  </section>'''

# 2. Overarching Gen 5 & Gen 6 Collapsible Window HTML
gen5_gen6_window_html = '''    <!-- OVERARCHING COLLAPSIBLE WINDOW: GEN 5 & GEN 6 ARCHIVES -->
    <div class="w-full max-w-7xl mx-auto my-8 px-4">
      <div class="bg-black/90 border-2 border-emerald-500/60 rounded-2xl overflow-hidden shadow-[0_0_35px_rgba(52,211,153,0.3)]">
        
        <!-- Header Toggle Bar -->
        <div class="bg-gradient-to-r from-emerald-950 via-gray-950 to-black p-5 flex flex-col md:flex-row justify-between items-start md:items-center cursor-pointer border-b border-emerald-500/40" onclick="toggleDrawer('gen5-6-archive-window')">
          <div class="flex items-center gap-3">
            <span class="text-2xl text-emerald-400">⚡</span>
            <div>
              <h3 class="font-cyber text-lg md:text-xl text-white font-extrabold uppercase tracking-wider">
                OVERARCHING GEN 5 &amp; GEN 6 ARCHIVE WINDOW
              </h3>
              <p class="font-mono-code text-xs text-emerald-400 tracking-wider">
                Pre-Expanded Lineage Carousel · Quick Edit Name &amp; Add Descendants
              </p>
            </div>
          </div>
          <div class="mt-3 md:mt-0 flex items-center gap-3">
            <span class="text-xs font-mono-code text-emerald-300 bg-emerald-950 px-3 py-1 rounded border border-emerald-700">
              TAP TO EXPAND / COLLAPSE ▾
            </span>
          </div>
        </div>

        <!-- Overarching Drawer Content -->
        <div id="gen5-6-archive-window" class="card-drawer p-6 space-y-6">
          <div class="flex justify-between items-center border-b border-gray-800 pb-3">
            <span class="text-xs font-mono-code text-emerald-400 uppercase font-bold">
              👈 SWIPE HORIZONTALLY (OR CLICK CHEVRONS ◄ ►) TO EXPLORE GEN 5 &amp; GEN 6 DESCENDANTS 👉
            </span>
            <div class="flex gap-2">
              <button onclick="scrollCarousel('gen5-6-carousel', -360)" class="chevron-btn" title="Swipe Left">◄</button>
              <button onclick="scrollCarousel('gen5-6-carousel', 360)" class="chevron-btn" title="Swipe Right">►</button>
            </div>
          </div>

          <!-- Gen 5 & 6 Horizontal Swipe Track -->
          <div id="gen5-6-carousel" class="carousel-container space-x-4">
            
            <!-- Track 1: Asar Lineage (Gen 5 / Gen 6) -->
            <div class="family-card carousel-card bg-gray-950 p-4 rounded-xl border border-emerald-500/50">
              <div class="flex justify-between items-center mb-2">
                <span class="font-mono-code text-xs text-emerald-400 font-bold">ASAR LINEAGE (GEN 5/6)</span>
                <span class="text-[9px] font-mono-code text-emerald-300 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-700">PRE-EXPANDED</span>
              </div>
              <p class="text-xs text-gray-300 font-sans mb-3">Pre-expanded children &amp; grandchildren branch.</p>
              <div class="space-y-2 font-mono-code text-xs">
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Asar's Children <small class="text-emerald-400">(Gen 5)</small></span>
                  <button onclick="openMemberModal('Asar Children', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Asar's Grandchildren <small class="text-pink-400">(Gen 6)</small></span>
                  <button onclick="openMemberModal('Asar Grandchildren', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
              </div>
              <button onclick="openMemberModal('Asar Lineage', 'Gen 5 / 6 Add')" class="w-full mt-3 bg-emerald-950 border border-emerald-600 text-emerald-300 hover:bg-emerald-900 font-cyber font-bold text-xs py-1.5 rounded uppercase">
                ➕ Add Child to Asar Line
              </button>
            </div>

            <!-- Track 2: Sariah & Khalil Lineage (Gen 5) -->
            <div class="family-card carousel-card bg-gray-950 p-4 rounded-xl border border-emerald-500/50">
              <div class="flex justify-between items-center mb-2">
                <span class="font-mono-code text-xs text-emerald-400 font-bold">SARIAH &amp; KHALIL (GEN 5)</span>
                <span class="text-[9px] font-mono-code text-emerald-300 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-700">PRE-EXPANDED</span>
              </div>
              <p class="text-xs text-gray-300 font-sans mb-3">Bikila Darden's Gen 5 Descendant Lines.</p>
              <div class="space-y-2 font-mono-code text-xs">
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Sariah Line</span>
                  <button onclick="openMemberModal('Sariah', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Khalil Line</span>
                  <button onclick="openMemberModal('Khalil', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
              </div>
              <button onclick="openMemberModal('Sariah & Khalil Lineage', 'Gen 5 Add')" class="w-full mt-3 bg-emerald-950 border border-emerald-600 text-emerald-300 hover:bg-emerald-900 font-cyber font-bold text-xs py-1.5 rounded uppercase">
                ➕ Add Child
              </button>
            </div>

            <!-- Track 3: Jewels & Jamila Lineage (Gen 5/6) -->
            <div class="family-card carousel-card bg-gray-950 p-4 rounded-xl border border-emerald-500/50">
              <div class="flex justify-between items-center mb-2">
                <span class="font-mono-code text-xs text-yellow-400 font-bold">JEWELS &amp; JAMILA (GEN 5/6)</span>
                <span class="text-[9px] font-mono-code text-yellow-300 bg-yellow-950 px-2 py-0.5 rounded border border-yellow-700">PRE-EXPANDED</span>
              </div>
              <p class="text-xs text-gray-300 font-sans mb-3">Peggy Darden / Debra Profitt Descendant Lines.</p>
              <div class="space-y-2 font-mono-code text-xs">
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Raevon Profitt <small class="text-emerald-400">(Gen 5)</small></span>
                  <button onclick="openMemberModal('Raevon Profitt', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Ashley &amp; Alani <small class="text-pink-400">(Gen 6)</small></span>
                  <button onclick="openMemberModal('Ashley & Alani', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
              </div>
              <button onclick="openMemberModal('Debra Profitt Lineage', 'Gen 5/6 Add')" class="w-full mt-3 bg-yellow-950 border border-yellow-600 text-yellow-300 hover:bg-yellow-900 font-cyber font-bold text-xs py-1.5 rounded uppercase">
                ➕ Add Child to Jewels Line
              </button>
            </div>

            <!-- Track 4: Thomas Earl, Jason, Jeremy Lineage (Gen 5/6) -->
            <div class="family-card carousel-card bg-gray-950 p-4 rounded-xl border border-emerald-500/50">
              <div class="flex justify-between items-center mb-2">
                <span class="font-mono-code text-xs text-emerald-400 font-bold">DONNA WATKINS LINEAGE (GEN 5/6)</span>
                <span class="text-[9px] font-mono-code text-emerald-300 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-700">PRE-EXPANDED</span>
              </div>
              <p class="text-xs text-gray-300 font-sans mb-3">Johnnie Darden / Donna Branch Descendants.</p>
              <div class="space-y-2 font-mono-code text-xs">
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Thomas Jr, Skylar, Archer, Ace</span>
                  <button onclick="openMemberModal('Thomas Earl Watkins Kids', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
                <div class="flex justify-between items-center bg-black/80 p-2 rounded border border-gray-800">
                  <span>• Devin, Amya, Alexander, Joy</span>
                  <button onclick="openMemberModal('Jason Kids', 'Fix/Edit Name')" class="text-[10px] bg-amber-950 text-amber-300 border border-amber-700 px-2 py-0.5 rounded">✏️ Fix</button>
                </div>
              </div>
              <button onclick="openMemberModal('Donna Watkins Lineage', 'Gen 5/6 Add')" class="w-full mt-3 bg-emerald-950 border border-emerald-600 text-emerald-300 hover:bg-emerald-900 font-cyber font-bold text-xs py-1.5 rounded uppercase">
                ➕ Add Child to Donna Line
              </button>
            </div>

          </div>
        </div>
      </div>
    </div>'''

# Insert Correction Zone before Tree Portal main container
if '<section class="tree-portal">' in html:
    html = html.replace('<section class="tree-portal">', correction_zone_html + '\n\n  <section class="tree-portal">', 1)

# Insert Overarching Gen 5 & 6 Archive Window directly after Gen 3 Carousel block
if '</div><!-- end gen3-carousel -->' in html:
    html = html.replace('</div><!-- end gen3-carousel -->', '</div><!-- end gen3-carousel -->\n\n' + gen5_gen6_window_html, 1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully added Correction Zone and Overarching Gen 5 & 6 Archive Window!')
