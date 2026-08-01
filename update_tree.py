import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build HTML for Mozzell Darden Branch
mozzell_html = '''      <!-- Mozzell Darden Branch (First Son) -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('mozell')">
          <div>
            <div class="card-title-text">Mozzell Darden Branch (First Son)</div>
            <div class="card-subtitle">9 Children Lineage &amp; Descendants</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="mozell">
          <div class="collab-badge mb-3">
            <span>📌 Lead Manager: Mozzell's Branch Lead &amp; Tree Research</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo">📷 Album</a>
          </div>

          <div class="nested-cards">
            <!-- Bernard Darden -->
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

            <!-- Mozzell Darden Jr. -->
            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('mozzell-jr-kids')">
                <span>👨 Mozzell Darden Jr.</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="mozzell-jr-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👦 Mozzell Darden 3rd</div>
              </div>
            </div>

            <!-- Derrick Darden -->
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

            <!-- Carol Darden ("Bunny") -->
            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('carol-kids')">
                <span>👩 Carol Darden ("Bunny")</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="carol-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jovonda</div>
              </div>
            </div>

            <!-- Sheila Darden -->
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

            <!-- Mary Washington -->
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

            <!-- Lolita Darden -->
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

            <!-- Kattely Darden -->
            <div class="nested-card">
              <div class="nested-header">
                <span>👧 Kattely Darden</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">Daughter</span>
              </div>
            </div>

            <!-- Lisa Darden -->
            <div class="nested-card">
              <div class="nested-header">
                <span>👧 Lisa Darden</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">Daughter</span>
              </div>
            </div>

          </div>
          <button class="btn-add-descendant mt-3" onclick="openMemberModal('Mozzell Darden Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>'''

# Build HTML for Johnnie Watson Branch
johnnie_html = '''      <!-- Johnnie Watson (Johnnie Darden) Branch -->
      <div class="family-card" data-card>
        <div class="card-header" onclick="toggleDrawer('johnnie-watson')">
          <div>
            <div class="card-title-text">Johnnie Watson (Johnnie Darden) Branch</div>
            <div class="card-subtitle">7 Children Lineage &amp; Descendants</div>
          </div>
          <span class="badge-tag badge-blood">Gen 2</span>
        </div>
        <div class="card-drawer" id="johnnie-watson">
          <div class="collab-badge mb-3">
            <span>📌 Lead Manager: Johnnie Watson Family Research</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo">📷 Album</a>
          </div>

          <div class="nested-cards">
            <!-- Irving -->
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

            <!-- Louis -->
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

            <!-- Charles -->
            <div class="nested-card">
              <div class="nested-header" onclick="toggleNested('charles-w-kids')">
                <span>👨 Charles</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
              </div>
              <div class="nested-drawer" id="charles-w-kids">
                <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jenean</div>
              </div>
            </div>

            <!-- Darlene -->
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

            <!-- Donald Watson -->
            <div class="nested-card">
              <div class="nested-header">
                <span>👨 Donald Watson</span>
                <span style="font-size: 0.75rem; color: var(--color-bloodline);">Son</span>
              </div>
            </div>

            <!-- Donna -->
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

            <!-- Beverly -->
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
      </div>'''

# Build HTML for Peggy Owens Branch
peggy_html = '''      <!-- Peggy Owens (Peggy Darden) Branch -->
      <div class="family-card matriarch-card" data-card>
        <div class="card-header" onclick="toggleDrawer('peggy')">
          <div>
            <div class="card-title-text matriarch-title">Peggy Owens (Peggy Darden) Branch</div>
            <div class="card-subtitle" style="color: #ffe066;">Family Matriarch · Reunion &amp; Media Hub</div>
          </div>
          <span class="badge-tag badge-matriarch">Matriarch</span>
        </div>
        <div class="card-drawer" id="peggy">
          <div class="collab-badge mb-3" style="background: rgba(255, 215, 0, 0.15); border-color: rgba(255, 215, 0, 0.4);">
            <span>📌 Lead Manager: Peggy's Granddaughter Jewel (Reunion Master Strategist)</span>
            <a href="https://photos.app.goo.gl/pAtZvpKgwM2pL3HZ7" target="_blank" class="btn-card-photo" style="background: #ffd700; color: #08070b; font-weight: bold;">📷 Album</a>
          </div>

          <div class="nested-cards">
            <!-- Derrick Owens -->
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

            <!-- Debra Profitt -->
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

          <button class="btn-add-descendant mt-3" style="background: rgba(255, 215, 0, 0.2); border-color: #ffd700; color: #ffd700;" onclick="openMemberModal('Peggy Owens Branch', 'Gen 3')">➕ Add Child / Family Member</button>
        </div>
      </div>'''

# Replace old Mozell & Peggy blocks with updated detailed branches including Johnnie Watson!
old_mozell_pattern = re.compile(r'<!-- Mozell -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
old_peggy_pattern = re.compile(r'<!-- Peggy Darden \(Matriarch Highlighted\) -->.*?</div>\s*</div>\s*</div>', re.DOTALL)

# Insert Mozzell, Johnnie Watson, and Peggy Owens branches
combined_branches = mozzell_html + '\n\n' + johnnie_html + '\n\n' + peggy_html

if '<!-- Mozell -->' in html:
    html = old_mozell_pattern.sub(combined_branches, html, count=1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated darden_family_tree.html with complete verified lineage!')
