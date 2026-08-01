import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Gen 1 & Gen 2 section cleanly
gen1_and_gen2_html = '''    <!-- Generation 1 (Foundations - Stays Open) -->
    <div class="gen-group">
      <div class="gen-label">
        <span>Generation 1</span>
        <span style="font-size: 0.72rem; opacity: 0.8;">Patriarch &amp; Matriarch</span>
      </div>
      <div class="family-card union text-center p-4" data-card>
        <div class="card-header flex-col justify-center text-center" onclick="toggleDrawer('gen1')">
          <!-- Large Crest Icon -->
          <div class="w-16 h-16 mx-auto mb-3 rounded-full bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-300 flex items-center justify-center text-black text-2xl font-black shadow-[0_0_25px_rgba(245,158,11,0.6)]">
            👑
          </div>
          <div>
            <div class="card-title-text text-xl md:text-2xl font-black" style="color: var(--primary-gold);">Sam Darden Sr. &amp; Freddie Shields</div>
            <div class="card-subtitle text-xs text-amber-300/80 mt-1">6 Children · Root Lineage Anchor</div>
          </div>
          <span class="badge-tag badge-root mt-2 inline-block">Founders</span>
        </div>
        <div class="card-drawer active text-left" id="gen1">
          <div class="nested-cards">
            <div class="nested-card">
              <div class="nested-header">
                <span>Sam Darden Jr. ("Cowboy")</span>
                <span style="color: var(--color-bloodline)">Son · 5 Children Household Lines</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Mozzell Darden</span>
                <span style="color: var(--color-bloodline)">Son · 7 Primary Lines</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Johnnie Darden (Johnnie Watson)</span>
                <span style="color: var(--color-bloodline)">Daughter · 7 Children Lineage</span>
              </div>
            </div>
            <div class="nested-card" style="border-left-color: #ffd700;">
              <div class="nested-header">
                <span style="color: #ffd700; font-weight: bold;">Peggy Darden (Peggy Owens)</span>
                <span class="badge-tag badge-matriarch">Matriarch</span>
              </div>
            </div>
            <div class="nested-card" style="border-left-color: #34d399;">
              <div class="nested-header">
                <span style="color: #34d399; font-weight: bold;">Lovell Darden ("Uncle Lovell")</span>
                <span class="badge-tag badge-elder">Living Elder</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Sarah Darden</span>
                <span style="color: var(--color-bloodline)">Daughter</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Generation 2 (Collapsible Branches - 6 Children of Sam Sr. & Freddie Shields) -->
    <div class="gen-group">
      <div class="gen-label">
        <span>Generation 2</span>
        <span style="font-size: 0.72rem; opacity: 0.8;">The 6 Children of Sam Darden Sr. &amp; Freddie Shields</span>
      </div>

      <!-- 1. Sam Jr. ("Cowboy") Branch -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('sam-jr')">
          <div>
            <div class="card-title-text">Sam Darden Jr. ("Cowboy") Branch</div>
            <div class="card-subtitle">Son of Sam Darden Sr. · 5 Children Household Lines</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="sam-jr">
          <div class="nested-cards">
            <div class="nested-card">
              <div class="nested-header">
                <span>George R. Darden ("Ronnie")</span>
                <span style="color: var(--color-bloodline)">Son · 5 Children &amp; Extensions</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>William Darden ("Bobby/Bill")</span>
                <span style="color: var(--color-bloodline)">Son · 2 Children</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Darrell Darden</span>
                <span style="color: var(--color-bloodline)">Son · 3 Children</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Pattie Darden</span>
                <span style="color: var(--color-bloodline)">Daughter · 1 Child</span>
              </div>
            </div>
            <div class="nested-card">
              <div class="nested-header">
                <span>Sharon Darden</span>
                <span style="color: var(--color-bloodline)">Daughter · 2 Children</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. Mozzell Darden Branch -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('mozell')">
          <div>
            <div class="card-title-text">Mozzell Darden Branch</div>
            <div class="card-subtitle">Son of Sam Darden Sr. · 7 Primary Lines &amp; Descendants</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="mozell">
          <div class="collab-badge mb-3">
            <span>📌 Lead Manager: Mozzell's Branch Lead &amp; Tree Research</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo">📷 Album</a>
          </div>

          <div class="nested-cards">
            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('bernard-kids')">
                <span>👨 Bernard Darden <small class="text-amber-400 font-normal">(Oldest Son)</small></span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
              </div>
              <div class="nested-drawer" id="bernard-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👧 Beverly</div>
                  <div>👧 Latasha</div>
                  <div>👦 Larry</div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('mozzell-jr-kids')">
                <span>👨 Mozzell Darden Jr.</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
              </div>
              <div class="nested-drawer" id="mozzell-jr-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👦 Mozzell Darden 3rd</div>
                  <div>👧 Kattely Darden</div>
                  <div>👧 Lisa Darden</div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('derrick-kids')">
                <span>👨 Derrick Darden</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
              </div>
              <div class="nested-drawer" id="derrick-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👦 Derrick Darden Jr.</div>
                  <div>👧 Brianna</div>
                  <div>👦 Kamal</div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('carol-kids')">
                <span>👩 Carol Darden ("Bunny")</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="carol-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jovonda</div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('sheila-kids')">
                <span>👩 Sheila Darden</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child (1 Grandchild)</span>
              </div>
              <div class="nested-drawer" id="sheila-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">
                  <div>👧 Diamond</div>
                  <div class="ml-4 text-emerald-400">└─ 👦 Carter <small>(Grandson)</small></div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('mary-kids')">
                <span>👩 Mary Washington</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children (3 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="mary-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👦 Charles Jr.</div>
                  <div>👦 Deshaun</div>
                  <div>👨 Kevin</div>
                  <div class="ml-4 space-y-0.5 text-emerald-400">
                    <div>├─ 👧 Maddison</div>
                    <div>├─ 👦 Dillion</div>
                    <div>└─ 👦 Daniel</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('lolita-kids')">
                <span>👩 Lolita Darden</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children (2 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="lolita-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👨 Che</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👦 Che Jr.</div>
                    <div>└─ 👧 Aniyah</div>
                  </div>
                  <div>👧 Brittney</div>
                </div>
              </div>
            </div>
          </div>
          <button class="btn-add-descendant mt-3" onclick="openMemberModal('Mozzell Darden Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>

      <!-- 3. Johnnie Darden Branch (Johnnie Watson) -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('johnnie-watson')">
          <div>
            <div class="card-title-text">Johnnie Darden Branch (Johnnie Watson)</div>
            <div class="card-subtitle">Daughter of Sam Darden Sr. · 7 Children &amp; Descendants</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="johnnie-watson">
          <div class="collab-badge mb-3">
            <span>📌 Lead Manager: Johnnie Watson Family Research</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo">📷 Album</a>
          </div>

          <div class="nested-cards">
            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('irving-kids')">
                <span>👨 Irving</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children (7 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="irving-kids">
                <div class="p-2 space-y-1.5 text-xs font-mono-code text-gray-300">
                  <div>👩 Erika</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👧 Alisyah Watson</div>
                    <div>├─ 👧 Hailie</div>
                    <div>├─ 👦 Sebastion</div>
                    <div>└─ 👧 Naomi</div>
                  </div>
                  <div>👨 Joel</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👩 Elaine</div>
                    <div>├─ 👧 Adriana</div>
                    <div>└─ 👧 Genisis Watson</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('louis-kids')">
                <span>👨 Louis</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
              </div>
              <div class="nested-drawer" id="louis-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👦 Louis Jr.</div>
                  <div>👧 Nadine</div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('charles-w-kids')">
                <span>👨 Charles</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="charles-w-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jenean</div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('darlene-kids')">
                <span>👩 Darlene</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children (2 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="darlene-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👩 Ronyelle Stallworth</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👧 Nyalla</div>
                    <div>└─ 👦 Aden</div>
                  </div>
                  <div>👨 Eric</div>
                  <div>👩 Melinda</div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header">
                <span>👨 Donald</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">Son</span>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('donna-kids')">
                <span>👩 Donna</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 4 Children (11 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="donna-kids">
                <div class="p-2 space-y-2 text-xs font-mono-code text-gray-300">
                  <div>👨 Thomas Earl Watkins</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👦 Thomas Jr.</div>
                    <div>├─ 👧 Skylar</div>
                    <div>├─ 👦 Archer</div>
                    <div>└─ 👦 Ace</div>
                  </div>
                  <div>👨 Jason</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👦 Devin</div>
                    <div>├─ 👧 Amya</div>
                    <div>├─ 👦 Alexander</div>
                    <div>└─ 👧 Joy</div>
                  </div>
                  <div>👩 Joy</div>
                  <div>👨 Jeremy</div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👦 Jayson</div>
                    <div>├─ 👧 Myrikal</div>
                    <div>└─ 👧 Malayah</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('beverly-w-kids')">
                <span>👩 Beverly</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="beverly-w-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👦 Jonathan</div>
              </div>
            </div>
          </div>
          <button class="btn-add-descendant mt-3" onclick="openMemberModal('Johnnie Watson Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>

      <!-- 4. Peggy Darden Branch (Peggy Owens) -->
      <div class="family-card matriarch-card" data-card>
        <div class="card-header" onclick="toggleDrawer('peggy')">
          <div>
            <div class="card-title-text matriarch-title">Peggy Darden Branch (Peggy Owens)</div>
            <div class="card-subtitle" style="color: #ffe066;">Daughter of Sam Darden Sr. · Family Matriarch · Reunion &amp; Media Hub</div>
          </div>
          <span class="badge-tag badge-matriarch">Matriarch</span>
        </div>
        <div class="card-drawer" id="peggy">
          <div class="collab-badge mb-3" style="background: rgba(255, 215, 0, 0.15); border-color: rgba(255, 215, 0, 0.4);">
            <span>📌 Lead Manager: Peggy's Granddaughter Jewel (Reunion Master Strategist)</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo" style="background: #ffd700; color: #08070b; font-weight: bold;">📷 Album</a>
          </div>

          <div class="nested-cards">
            <div class="nested-card" style="border-left-color: #ffd700;">
              <div class="nested-header" onclick="toggleNested('derrick-owens-kids')">
                <span>👨 Derrick Owens</span>
                <span style="font-size: 0.75rem; color: #ffd700;">▼ 4 Children (1 Grandchild)</span>
              </div>
              <div class="nested-drawer" id="derrick-owens-kids">
                <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                  <div>👨 Aaron</div>
                  <div class="ml-4 text-emerald-400">└─ 👦 Aaron Owens Jr.</div>
                  <div>👨 Marques</div>
                  <div>👨 Stephan</div>
                  <div>👩 Darnielle</div>
                </div>
              </div>
            </div>

            <div class="nested-card" style="border-left-color: #ffd700;">
              <div class="nested-header" onclick="toggleNested('debra-profitt-kids')">
                <span>👩 Debra Profitt</span>
                <span style="font-size: 0.75rem; color: #ffd700;">▼ 2 Daughters (3 Grandchildren)</span>
              </div>
              <div class="nested-drawer" id="debra-profitt-kids">
                <div class="p-2 space-y-1.5 text-xs font-mono-code text-gray-300">
                  <div>👩 Jamila</div>
                  <div class="ml-4 text-emerald-400">└─ 👦 Raevon Profitt</div>
                  <div>👩 Jewels <small class="text-amber-400">(Reunion Master Strategist)</small></div>
                  <div class="ml-4 text-emerald-400">
                    <div>├─ 👧 Ashley</div>
                    <div>└─ 👧 Alani</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button class="btn-add-descendant mt-3" style="background: rgba(255, 215, 0, 0.2); border-color: #ffd700; color: #ffd700;" onclick="openMemberModal('Peggy Darden Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>

      <!-- 5. Lovell Darden Branch ("Uncle Lovell") -->
      <div class="family-card elder-card" data-card>
        <div class="card-header" onclick="toggleDrawer('lovell-info')">
          <div>
            <div class="card-title-text elder-title">Lovell Darden Branch ("Uncle Lovell")</div>
            <div class="card-subtitle" style="color: #a7f3d0;">Son of Sam Darden Sr. · Living Elder &amp; Tree Originator</div>
          </div>
          <span class="badge-tag badge-elder">Living Elder</span>
        </div>
        <div class="card-drawer" id="lovell-info">
          <div class="collab-badge mb-3" style="background: rgba(52, 211, 153, 0.15); border-color: rgba(52, 211, 153, 0.4);">
            <span>📌 Lead Manager: Lovell's Granddaughter (Tree Research Lead)</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo" style="background: #34d399; color: #08070b; font-weight: bold;">📷 Album</a>
          </div>
          <button class="btn-add-descendant mt-3" style="background: rgba(52, 211, 153, 0.2); border-color: #34d399; color: #34d399;" onclick="openMemberModal('Lovell Darden Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>

      <!-- 6. Sarah Darden Branch -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('sarah-info')">
          <div>
            <div class="card-title-text">Sarah Darden Branch</div>
            <div class="card-subtitle">Daughter of Sam Darden Sr.</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="sarah-info">
          <button class="btn-add-descendant" onclick="openMemberModal('Sarah Darden Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>

    </div>'''

# Replace old Gen 1 & Gen 2 block cleanly using regex
gen_pattern = re.compile(r'<!-- Generation 1 \(Foundations - Stays Open\) -->.*?<!-- Generation 3', re.DOTALL)
html = gen_pattern.sub(gen1_and_gen2_html + '\n\n    <!-- Generation 3', html, count=1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully rebuilt Gen 1 and Gen 2 with Sam Sr. & Freddie Shields crest and all 6 children cards!')
