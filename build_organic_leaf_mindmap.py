import re

leaf_mindmap_html = '''  <!-- ============================================================ -->
  <!-- ORGANIC LEAF-SHAPED INTERACTIVE TREE MIND MAP ENGINE         -->
  <!-- ============================================================ -->
  <section class="w-full max-w-7xl mx-auto my-10 px-4">
    <div class="scrim-box p-6 md:p-8 rounded-2xl border-2 border-emerald-500/60 shadow-[0_0_50px_rgba(52,211,153,0.3)] relative overflow-hidden bg-gradient-to-b from-[#092309] to-[#030a03]">
      
      <!-- Mind Map Header & Controls -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-emerald-500/30 pb-4 mb-6 gap-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl text-emerald-400">🌿</span>
          <div>
            <h3 class="font-cyber text-2xl text-white font-extrabold uppercase tracking-wider">
              DARDEN FAMILY HERITAGE <span class="text-emerald-400">ORGANIC LEAF MIND MAP</span>
            </h3>
            <p class="font-mono-code text-xs text-emerald-300/80 tracking-wider mt-0.5">
              Click Any Leaf Node to Expand / Collapse Generational Branches (Gen 1 → Gen 6)
            </p>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-2">
          <button onclick="expandAllLeaves()" class="bg-emerald-800 hover:bg-emerald-700 text-white font-cyber font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-md">
            ➕ Expand All Leaves
          </button>
          <button onclick="collapseDeepLeaves()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 font-bold text-xs px-3.5 py-2 rounded-lg transition-all">
            ➖ Collapse Deep
          </button>
        </div>
      </div>

      <!-- Organic Leaf Mind Map Scrollable Container -->
      <div class="mindmap-container w-full overflow-x-auto p-4 rounded-xl border border-emerald-800/60 bg-black/60">
        <div class="tree" id="organic-family-tree">
          <ul>
            <li>
              <!-- ROOT NODE: Sam Darden Sr. & Freddie Shields -->
              <div class="leaf root-leaf" onclick="openMemberModal('Sam Darden Sr. & Freddie Shields', 'Gen 1 Founders')">
                👑 Sam Darden Sr. &amp; Freddie Shields
              </div>
              <ul>
                
                <!-- BRANCH 1: Sam Darden Jr. ("Cowboy") -->
                <li>
                  <div class="leaf gen2-leaf">🤠 Sam Darden Jr. ("Cowboy")</div>
                  <ul>
                    <li>
                      <div class="leaf">👨 George R. Darden ("Ronnie")</div>
                      <ul>
                        <li><div class="leaf">👨 Leon Darden ("Rondell")</div></li>
                        <li>
                          <div class="leaf">👨 Bikila Darden</div>
                          <ul>
                            <li>
                              <div class="leaf">👨 Asar Lineage</div>
                              <ul>
                                <li><div class="leaf">• Asar's Children (Gen 5)</div></li>
                                <li><div class="leaf">• Asar's Grandchildren (Gen 6)</div></li>
                              </ul>
                            </li>
                            <li><div class="leaf">👩 Sariah</div></li>
                            <li><div class="leaf">👨 Khalil</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👨 William Darden ("Bobby/Bill")</div>
                      <ul>
                        <li><div class="leaf">👦 Billy Darden</div></li>
                        <li><div class="leaf">👧 Kim Darden</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf blended-leaf">👨 Darrell Darden</div>
                      <ul>
                        <li><div class="leaf">👦 Darrell Darden Jr.</div></li>
                        <li><div class="leaf blended-leaf">🟣 Harold</div></li>
                        <li><div class="leaf blended-leaf">🟣 Keisha</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Pattie Darden</div>
                      <ul>
                        <li><div class="leaf">👦 Keith Darden</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Sharon Darden</div>
                      <ul>
                        <li><div class="leaf">👦 Sherron Darden</div></li>
                        <li><div class="leaf">👦 Stephon Darden</div></li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <!-- BRANCH 2: Mozzell Darden -->
                <li>
                  <div class="leaf gen2-leaf">👴 Mozzell Darden</div>
                  <ul>
                    <li>
                      <div class="leaf">👨 Bernard Darden</div>
                      <ul>
                        <li><div class="leaf">👧 Beverly</div></li>
                        <li><div class="leaf">👧 Latasha</div></li>
                        <li><div class="leaf">👦 Larry</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👨 Mozzell Darden Jr.</div>
                      <ul>
                        <li><div class="leaf">👦 Mozzell Darden 3rd</div></li>
                        <li><div class="leaf">👧 Kattely Darden</div></li>
                        <li><div class="leaf">👧 Lisa Darden</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👨 Derrick Darden</div>
                      <ul>
                        <li><div class="leaf">👦 Derrick Darden Jr.</div></li>
                        <li><div class="leaf">👧 Brianna</div></li>
                        <li><div class="leaf">👦 Kamal</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Carol Darden ("Bunny")</div>
                      <ul>
                        <li><div class="leaf">👧 Jovonda</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Sheila Darden</div>
                      <ul>
                        <li>
                          <div class="leaf">👧 Diamond</div>
                          <ul>
                            <li><div class="leaf">👦 Carter</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Mary Washington</div>
                      <ul>
                        <li><div class="leaf">👦 Charles Jr.</div></li>
                        <li><div class="leaf">👦 Deshaun</div></li>
                        <li>
                          <div class="leaf">👨 Kevin</div>
                          <ul>
                            <li><div class="leaf">👧 Maddison</div></li>
                            <li><div class="leaf">👦 Dillion</div></li>
                            <li><div class="leaf">👦 Daniel</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Lolita Darden</div>
                      <ul>
                        <li>
                          <div class="leaf">👨 Che</div>
                          <ul>
                            <li><div class="leaf">👦 Che Jr.</div></li>
                            <li><div class="leaf">👧 Aniyah</div></li>
                          </ul>
                        </li>
                        <li><div class="leaf">👧 Brittney</div></li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <!-- BRANCH 3: Peggy Darden (Peggy Owens) -->
                <li>
                  <div class="leaf gen2-leaf">👵 Peggy Darden (Peggy Owens)</div>
                  <ul>
                    <li>
                      <div class="leaf">👨 Derrick Owens</div>
                      <ul>
                        <li>
                          <div class="leaf">👨 Aaron</div>
                          <ul>
                            <li><div class="leaf">👦 Aaron Owens Jr.</div></li>
                          </ul>
                        </li>
                        <li><div class="leaf">👨 Marques</div></li>
                        <li><div class="leaf">👨 Stephan</div></li>
                        <li><div class="leaf">👩 Darnielle</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Debra Profitt</div>
                      <ul>
                        <li>
                          <div class="leaf">👩 Jamila</div>
                          <ul>
                            <li><div class="leaf">👦 Raevon Profitt</div></li>
                          </ul>
                        </li>
                        <li>
                          <div class="leaf">👩 Jewels (Reunion Lead)</div>
                          <ul>
                            <li><div class="leaf">👧 Ashley</div></li>
                            <li><div class="leaf">👧 Alani</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <!-- BRANCH 4: Johnnie Darden (Johnnie Watson) -->
                <li>
                  <div class="leaf gen2-leaf">👵 Johnnie Darden (Johnnie Watson)</div>
                  <ul>
                    <li>
                      <div class="leaf">👨 Irving</div>
                      <ul>
                        <li>
                          <div class="leaf">👩 Erika</div>
                          <ul>
                            <li><div class="leaf">👧 Alisyah Watson</div></li>
                            <li><div class="leaf">👧 Hailie</div></li>
                            <li><div class="leaf">👦 Sebastion</div></li>
                            <li><div class="leaf">👧 Naomi</div></li>
                          </ul>
                        </li>
                        <li>
                          <div class="leaf">👨 Joel</div>
                          <ul>
                            <li><div class="leaf">👩 Elaine</div></li>
                            <li><div class="leaf">👧 Adriana</div></li>
                            <li><div class="leaf">👧 Genisis Watson</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👨 Louis</div>
                      <ul>
                        <li><div class="leaf">👦 Louis Jr.</div></li>
                        <li><div class="leaf">👧 Nadine</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👨 Charles</div>
                      <ul>
                        <li><div class="leaf">👧 Jenean</div></li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Darlene</div>
                      <ul>
                        <li>
                          <div class="leaf">👩 Ronyelle Stallworth</div>
                          <ul>
                            <li><div class="leaf">👧 Nyalla</div></li>
                            <li><div class="leaf">👦 Aden</div></li>
                          </ul>
                        </li>
                        <li><div class="leaf">👨 Eric</div></li>
                        <li><div class="leaf">👩 Melinda</div></li>
                      </ul>
                    </li>
                    <li><div class="leaf">👨 Donald</div></li>
                    <li>
                      <div class="leaf">👩 Donna</div>
                      <ul>
                        <li>
                          <div class="leaf">👨 Thomas Earl Watkins</div>
                          <ul>
                            <li><div class="leaf">👦 Thomas Jr.</div></li>
                            <li><div class="leaf">👧 Skylar</div></li>
                            <li><div class="leaf">👦 Archer</div></li>
                            <li><div class="leaf">👦 Ace</div></li>
                          </ul>
                        </li>
                        <li>
                          <div class="leaf">👨 Jason</div>
                          <ul>
                            <li><div class="leaf">👦 Devin</div></li>
                            <li><div class="leaf">👧 Amya</div></li>
                            <li><div class="leaf">👦 Alexander</div></li>
                            <li><div class="leaf">👧 Joy</div></li>
                          </ul>
                        </li>
                        <li><div class="leaf">👩 Joy</div></li>
                        <li>
                          <div class="leaf">👨 Jeremy</div>
                          <ul>
                            <li><div class="leaf">👦 Jayson</div></li>
                            <li><div class="leaf">👧 Myrikal</div></li>
                            <li><div class="leaf">👧 Malayah</div></li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="leaf">👩 Beverly</div>
                      <ul>
                        <li><div class="leaf">👦 Jonathan</div></li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <!-- BRANCH 5: Lovell Darden ("Uncle Lovell") -->
                <li>
                  <div class="leaf gen2-leaf">👨 Lovell Darden ("Uncle Lovell")</div>
                  <ul>
                    <li><div class="leaf">📌 Living Elder Lineage</div></li>
                  </ul>
                </li>

                <!-- BRANCH 6: Sarah Darden -->
                <li>
                  <div class="leaf gen2-leaf">👩 Sarah Darden</div>
                  <ul>
                    <li><div class="leaf">📌 Daughter of Sam Sr.</div></li>
                  </ul>
                </li>

              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>'''

# CSS for Organic Leaf Tree Engine
organic_css = '''
    /* Organic Leaf Tree Mind Map Engine */
    .mindmap-container {
      background: linear-gradient(180deg, #092309 0%, #030a03 100%);
      color: white;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      padding: 30px;
      overflow-x: auto;
      min-height: 600px;
    }

    .tree ul {
      padding-top: 20px; 
      position: relative;
      display: flex;
      justify-content: center;
      transition: all 0.5s;
    }

    .tree li {
      float: left; 
      text-align: center;
      list-style-type: none;
      position: relative;
      padding: 20px 5px 0 5px;
      transition: all 0.5s;
    }

    .tree li::before, .tree li::after {
      content: '';
      position: absolute; 
      top: 0; 
      right: 50%;
      border-top: 2px solid #5a8231;
      width: 50%; 
      height: 20px;
    }

    .tree li::after {
      right: auto; 
      left: 50%;
      border-left: 2px solid #5a8231;
    }

    .tree li:only-child::after, .tree li:only-child::before {
      display: none;
    }

    .tree li:only-child { 
      padding-top: 0;
    }

    .tree li:first-child::before, .tree li:last-child::after {
      border: 0 none;
    }

    .tree li:last-child::before {
      border-right: 2px solid #5a8231;
      border-radius: 0 5px 0 0;
    }

    .tree li:first-child::after {
      border-radius: 5px 0 0 0;
    }

    .tree ul ul::before {
      content: '';
      position: absolute; 
      top: 0; 
      left: 50%;
      border-left: 2px solid #5a8231;
      width: 0; 
      height: 20px;
    }

    .tree div.leaf {
      border: 2px solid #3d6e1d;
      padding: 10px 16px;
      text-decoration: none;
      color: #d1ffd1;
      background: #184018;
      font-size: 13px;
      font-weight: bold;
      display: inline-block;
      border-radius: 0 25px 0 25px; 
      transition: all 0.3s ease;
      cursor: pointer;
      box-shadow: 3px 3px 8px rgba(0,0,0,0.6);
      white-space: nowrap;
    }

    .tree div.leaf:hover {
      background: #2a6b2a;
      color: #fff;
      border-color: #71b835;
      transform: scale(1.06);
    }

    .tree div.leaf.root-leaf {
      background: linear-gradient(135deg, #15803d, #047857);
      border-color: #f59e0b;
      color: #fef08a;
      font-size: 15px;
      padding: 12px 22px;
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
    }

    .tree div.leaf.gen2-leaf {
      background: #064e3b;
      border-color: #34d399;
      color: #a7f3d0;
    }

    .tree div.leaf.blended-leaf {
      background: #3b0764;
      border-color: #c084fc;
      color: #f3e8ff;
    }

    .leaf-hidden {
      display: none !important;
    }
'''

# JavaScript for Organic Leaf Tree
organic_js = '''
    // Interactivity: Click a leaf to toggle its child branches
    document.addEventListener("DOMContentLoaded", function() {
      const leaves = document.querySelectorAll('.tree div.leaf');
      
      leaves.forEach(leaf => {
        leaf.addEventListener('click', function(e) {
          e.stopPropagation();
          const children = this.nextElementSibling;
          if (children && children.tagName.toLowerCase() === 'ul') {
            children.classList.toggle('leaf-hidden');
          }
        });
      });
    });

    function expandAllLeaves() {
      document.querySelectorAll('.tree ul').forEach(ul => {
        ul.classList.remove('leaf-hidden');
      });
    }

    function collapseDeepLeaves() {
      // Collapse everything deeper than level 2
      document.querySelectorAll('.tree ul ul ul').forEach(ul => {
        ul.classList.add('leaf-hidden');
      });
    }
'''

# Update darden_family_tree.html
with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS
if '</style>' in html:
    html = html.replace('</style>', organic_css + '\n</style>', 1)

# Replace Mind Map section with Organic Leaf Mind Map Engine
pattern = re.compile(r'<!-- =+ -->\s*<!-- D3\.JS INTERACTIVE VISUAL MIND MAP GRAPH.*?<!-- FULLSCREEN MIND MAP POP-UP MODAL -->', re.DOTALL)
if 'ORGANIC LEAF-SHAPED INTERACTIVE TREE MIND MAP ENGINE' not in html:
    html = pattern.sub(leaf_mindmap_html + '\n\n  <!-- FULLSCREEN MIND MAP POP-UP MODAL -->', html, count=1)

# Add JS
if '</script>' in html:
    html = html.replace('</script>', organic_js + '\n</script>', 1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully integrated Organic Leaf Mind Map Engine into darden_family_tree.html!')
