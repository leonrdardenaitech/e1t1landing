import re, sys

# -------------------------------------------------------------
# 1. GENERATE DARDEN_FAMILY_TREE_V2.HTML (Organic Leaf Mind Map)
# -------------------------------------------------------------
v2_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive Family Mind Map - Darden Lineage</title>
<style>
    /* Container & Background */
    body {
        margin: 0;
        padding: 0;
        background-color: #030a03;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
    }

    .page-header {
        background: #061706;
        padding: 20px 40px;
        border-bottom: 2px solid #3d6e1d;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 15px;
    }

    .header-title {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .header-title h1 {
        margin: 0;
        font-size: 24px;
        color: #d1ffd1;
        letter-spacing: 1px;
    }

    .header-title p {
        margin: 4px 0 0 0;
        font-size: 13px;
        color: #71b835;
    }

    .header-btns {
        display: flex;
        gap: 10px;
    }

    .btn {
        background: #184018;
        border: 1px solid #5a8231;
        color: #d1ffd1;
        padding: 8px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 13px;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .btn:hover {
        background: #2a6b2a;
        color: #fff;
        border-color: #71b835;
    }

    .mindmap-container {
        background: linear-gradient(180deg, #092309 0%, #030a03 100%);
        color: white;
        padding: 40px 20px;
        overflow-x: auto; /* Allows horizontal scrolling for wide branches */
        min-height: calc(100vh - 120px);
        box-sizing: border-box;
    }

    /* Tree Layout Engine */
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

    /* Stems and Branches (Lines) */
    .tree li::before, .tree li::after {
        content: '';
        position: absolute; 
        top: 0; 
        right: 50%;
        border-top: 2px solid #5a8231; /* Stem color */
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

    /* Connecting stem down to the leaf */
    .tree ul ul::before {
        content: '';
        position: absolute; 
        top: 0; 
        left: 50%;
        border-left: 2px solid #5a8231;
        width: 0; 
        height: 20px;
    }

    /* Leaf Node Styling */
    .tree div.leaf {
        border: 2px solid #3d6e1d;
        padding: 12px 18px;
        text-decoration: none;
        color: #d1ffd1;
        background: #184018;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        /* This creates the leaf shape */
        border-radius: 0 25px 0 25px; 
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.6);
        white-space: nowrap;
    }

    .tree div.leaf.root-leaf {
        background: #2e5c1e;
        border-color: #71b835;
        font-size: 16px;
        padding: 14px 22px;
        box-shadow: 0 0 15px rgba(113, 184, 53, 0.4);
    }

    .tree div.leaf.gen2-leaf {
        background: #1e4d1e;
        border-color: #4c8a2b;
    }

    .tree div.leaf.blended-leaf {
        background: #3b1e4d;
        border-color: #8a2b8a;
        color: #f1d1ff;
    }

    /* Hover effect on leaves */
    .tree div.leaf:hover {
        background: #2a6b2a;
        color: #fff;
        border-color: #71b835;
        transform: scale(1.05);
    }

    /* Hidden class for the interactive toggle */
    .hidden {
        display: none !important;
    }
</style>
</head>
<body>

<div class="page-header">
    <div class="header-title">
        <span style="font-size: 28px;">🌿</span>
        <div>
            <h1>Interactive Family Mind Map</h1>
            <p>Darden Lineage (Sam Darden Sr. & Freddie Shields → Gen 6)</p>
        </div>
    </div>
    <div class="header-btns">
        <button class="btn" onclick="expandAllLeaves()">➕ Expand All</button>
        <button class="btn" onclick="collapseAllLeaves()">➖ Collapse Deep</button>
        <a href="darden_family_tree.html" class="btn">🏠 Return to Main Portal</a>
    </div>
</div>

<div class="mindmap-container">
    <div class="tree" id="family-tree">
        <ul>
            <li>
                <!-- ROOT -->
                <div class="leaf root-leaf">👑 Sam Darden Sr. &amp; Freddie Shields</div>
                <ul>
                    <!-- BRANCH 1 -->
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
                                                    <li><div class="leaf">👶 Asar's Children (Gen 5)</div></li>
                                                    <li><div class="leaf">👶 Asar's Grandchildren (Gen 6)</div></li>
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

                    <!-- BRANCH 2 -->
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

                    <!-- BRANCH 3 -->
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

                    <!-- BRANCH 4 -->
                    <li>
                        <div class="leaf gen2-leaf">👵 Johnnie Darden (Watson)</div>
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

                    <!-- BRANCH 5 -->
                    <li>
                        <div class="leaf gen2-leaf">👨 Lovell Darden</div>
                        <ul>
                            <li><div class="leaf">📌 Living Elder Lineage</div></li>
                        </ul>
                    </li>

                    <!-- BRANCH 6 -->
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

<script>
    // Interactivity: Click a leaf to toggle its child branches
    document.addEventListener("DOMContentLoaded", function() {
        const leaves = document.querySelectorAll('.tree div.leaf');
        
        leaves.forEach(leaf => {
            leaf.addEventListener('click', function(e) {
                e.stopPropagation(); // Prevent clicks from bubbling up
                
                // Find the adjacent <ul> containing the children of this leaf
                const children = this.nextElementSibling;
                
                if (children && children.tagName.toLowerCase() === 'ul') {
                    children.classList.toggle('hidden');
                }
            });
        });
    });

    function expandAllLeaves() {
        const allUls = document.querySelectorAll('.tree ul');
        allUls.forEach(ul => ul.classList.remove('hidden'));
    }

    function collapseAllLeaves() {
        const gen3Uls = document.querySelectorAll('.tree > ul > li > ul > li > ul');
        gen3Uls.forEach(ul => ul.classList.add('hidden'));
    }
</script>

</body>
</html>'''

with open('darden_family_tree_v2.html', 'w', encoding='utf-8') as f:
    f.write(v2_html)

print("[SUCCESS] Written darden_family_tree_v2.html")


# -------------------------------------------------------------
# 2. UPDATE DARDEN_FAMILY_TREE.HTML
# -------------------------------------------------------------
with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    main_html = f.read()

# A. Remove Correction Zone Announcement Banner
correction_banner_pattern = r'<!-- CORRECTION ZONE & ADD A DARDEN ANNOUNCEMENT BANNER -->.*?<\/section>'
main_html = re.sub(correction_banner_pattern, '', main_html, flags=re.DOTALL)

# B. Remove Gen 5 & 6 Overarching Archive Window if present
gen5_6_window_pattern = r'<!-- OVERARCHING COLLAPSIBLE WINDOW: GEN 5 & GEN 6 ARCHIVES -->.*?<\/div>\s*<\/div>\s*<\/div>'
main_html = re.sub(gen5_6_window_pattern, '', main_html, flags=re.DOTALL)

# C. Widget Window / Rectangle Component to insert under Gen 3 Scrollbar (gen3-carousel)
widget_window_html = '''</div><!-- end gen3-carousel -->

    <!-- ============================================================ -->
    # RECTANGULAR WIDGET WINDOW: INTERACTIVE MIND MAP SNIPPET LINK
    <!-- ============================================================ -->
    <div class="w-full max-w-7xl mx-auto my-8 px-4">
      <div class="bg-gradient-to-b from-[#092309] to-[#030a03] border-2 border-[#3d6e1d] rounded-2xl overflow-hidden shadow-[0_0_35px_rgba(61,110,29,0.5)]">
        
        <!-- Header Bar with Title & Direct Link -->
        <div class="bg-[#061706] p-5 flex flex-col md:flex-row justify-between items-start md:items-center border-b border-[#3d6e1d] gap-4">
          <div class="flex items-center gap-3">
            <span class="text-3xl">🌿</span>
            <div>
              <h3 class="font-cyber text-xl md:text-2xl text-[#d1ffd1] font-extrabold uppercase tracking-wider">
                DARDEN FAMILY INTERACTIVE MIND MAP
              </h3>
              <p class="font-mono-code text-xs text-[#71b835] tracking-wider">
                Generational Leaf Network · Click Any Leaf to Toggle Branches
              </p>
            </div>
          </div>
          <div class="flex items-center gap-3">
            <a href="darden_family_tree_v2.html" target="_blank" class="bg-[#184018] hover:bg-[#2a6b2a] border border-[#5a8231] text-[#d1ffd1] font-cyber font-bold text-xs px-4 py-2.5 rounded-lg uppercase tracking-wider transition-all shadow-md flex items-center gap-2">
              🔗 Open Full Mind Map Snippet Page (v2) ↗
            </a>
          </div>
        </div>

        <!-- Enclosed Mind Map Interactive Widget Window -->
        <div class="mindmap-container p-6 overflow-x-auto min-h-[500px]">
          <div class="tree" id="widget-family-tree">
            <ul>
              <li>
                <div class="leaf root-leaf">👑 Sam Darden Sr. &amp; Freddie Shields</div>
                <ul>
                  <!-- Branch 1 -->
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
                                  <li><div class="leaf">👶 Asar's Children (Gen 5)</div></li>
                                  <li><div class="leaf">👶 Asar's Grandchildren (Gen 6)</div></li>
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
                        <ul><li><div class="leaf">👦 Keith Darden</div></li></ul>
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

                  <!-- Branch 2 -->
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
                          <li><div class="leaf">👦 Mozzell 3rd</div></li>
                          <li><div class="leaf">👧 Kattely</div></li>
                          <li><div class="leaf">👧 Lisa</div></li>
                        </ul>
                      </li>
                      <li>
                        <div class="leaf">👨 Derrick Darden</div>
                        <ul>
                          <li><div class="leaf">👦 Derrick Jr.</div></li>
                          <li><div class="leaf">👧 Brianna</div></li>
                          <li><div class="leaf">👦 Kamal</div></li>
                        </ul>
                      </li>
                      <li>
                        <div class="leaf">👩 Carol Darden ("Bunny")</div>
                        <ul><li><div class="leaf">👧 Jovonda</div></li></ul>
                      </li>
                      <li>
                        <div class="leaf">👩 Sheila Darden</div>
                        <ul>
                          <li>
                            <div class="leaf">👧 Diamond</div>
                            <ul><li><div class="leaf">👦 Carter</div></li></ul>
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

                  <!-- Branch 3 -->
                  <li>
                    <div class="leaf gen2-leaf">👵 Peggy Darden</div>
                    <ul>
                      <li>
                        <div class="leaf">👨 Derrick Owens</div>
                        <ul>
                          <li>
                            <div class="leaf">👨 Aaron</div>
                            <ul><li><div class="leaf">👦 Aaron Owens Jr.</div></li></ul>
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
                            <ul><li><div class="leaf">👦 Raevon Profitt</div></li></ul>
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

                  <!-- Branch 4 -->
                  <li>
                    <div class="leaf gen2-leaf">👵 Johnnie Darden</div>
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
                        <ul><li><div class="leaf">👧 Jenean</div></li></ul>
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
                        <ul><li><div class="leaf">👦 Jonathan</div></li></ul>
                      </li>
                    </ul>
                  </li>

                  <!-- Branch 5 -->
                  <li>
                    <div class="leaf gen2-leaf">👨 Lovell Darden</div>
                    <ul><li><div class="leaf">📌 Living Elder Lineage</div></li></ul>
                  </li>

                  <!-- Branch 6 -->
                  <li>
                    <div class="leaf gen2-leaf">👩 Sarah Darden</div>
                    <ul><li><div class="leaf">📌 Daughter of Sam Sr.</div></li></ul>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>'''

if '</div><!-- end gen3-carousel -->' in main_html:
    main_html = main_html.replace('</div><!-- end gen3-carousel -->', widget_window_html, 1)

# Ensure CSS for Mindmap leaves is embedded in head if not already present
leaf_css = '''
    /* Organic Leaf Mind Map Styles */
    .mindmap-container {
        background: linear-gradient(180deg, #092309 0%, #030a03 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 40px;
        overflow-x: auto;
        min-height: 500px;
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

    .tree li:only-child::after, .tree li:only-child::before { display: none; }
    .tree li:only-child { padding-top: 0; }
    .tree li:first-child::before, .tree li:last-child::after { border: 0 none; }
    .tree li:last-child::before { border-right: 2px solid #5a8231; border-radius: 0 5px 0 0; }
    .tree li:first-child::after { border-radius: 5px 0 0 0; }

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
        padding: 12px 18px;
        text-decoration: none;
        color: #d1ffd1;
        background: #184018;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        border-radius: 0 25px 0 25px; 
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.6);
        white-space: nowrap;
    }

    .tree div.leaf.root-leaf {
        background: #2e5c1e;
        border-color: #71b835;
        font-size: 16px;
        padding: 14px 22px;
        box-shadow: 0 0 15px rgba(113, 184, 53, 0.4);
    }

    .tree div.leaf.gen2-leaf {
        background: #1e4d1e;
        border-color: #4c8a2b;
    }

    .tree div.leaf.blended-leaf {
        background: #3b1e4d;
        border-color: #8a2b8a;
        color: #f1d1ff;
    }

    .tree div.leaf:hover {
        background: #2a6b2a;
        color: #fff;
        border-color: #71b835;
        transform: scale(1.05);
    }

    .hidden { display: none !important; }
'''

if '</style>' in main_html and '.mindmap-container' not in main_html:
    main_html = main_html.replace('</style>', leaf_css + '\n</style>', 1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(main_html)

print("[SUCCESS] Updated darden_family_tree.html successfully!")
