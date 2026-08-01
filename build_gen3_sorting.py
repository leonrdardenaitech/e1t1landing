import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

gen3_carousel_new = '''    <!-- Generation 3 & 4 Drill-Down Ancestry Engine (4 Branch Sorting Portals) -->
    <div class="gen-group">
      <div class="gen-label flex justify-between items-center mb-3">
        <div>
          <span>Generation 3 &amp; 4 · Branch Sorting Portals</span>
          <span style="font-size: 0.72rem; opacity: 0.8;" class="block mt-0.5">👈 SWIPE HORIZONTALLY OR CLICK CHEVRONS ◄ ► TO SELECT BRANCH &amp; DRILL DOWN 👉</span>
        </div>
        <div class="flex gap-2">
          <button onclick="scrollCarousel('gen3-carousel', -360)" class="chevron-btn" title="Swipe Left">◄</button>
          <button onclick="scrollCarousel('gen3-carousel', 360)" class="chevron-btn" title="Swipe Right">►</button>
        </div>
      </div>

      <div id="gen3-carousel" class="carousel-container">
        
        <!-- PORTAL 1: Sam Jr. ("Cowboy") Lineage -->
        <div class="family-card carousel-card" data-card>
          <div class="card-header" onclick="toggleDrawer('portal-sam-jr')">
            <div>
              <div class="card-title-text font-black text-amber-300">🤠 Sam Darden Jr. Lineage</div>
              <div class="card-subtitle">5 Household Lines (Ronnie, Bobby, Darrell, Pattie, Sharon)</div>
            </div>
            <span class="badge-tag badge-blood">Gen 3 Portal</span>
          </div>
          <div class="card-drawer" id="portal-sam-jr">
            <div class="nested-cards space-y-2">
              
              <!-- Ronnie -->
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('ronnie-subdrawer')">
                  <span>George R. Darden ("Ronnie")</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ Gen 4 Descendants</span>
                </div>
                <div class="nested-drawer" id="ronnie-subdrawer">
                  <div class="space-y-2 p-1">
                    <div class="nested-card">
                      <div class="nested-header" onclick="toggleNested('bikila-subkids')">
                        <span>Bikila Darden</span>
                        <span style="font-size: 0.75rem; color: var(--primary-gold);">▼ 3 Children</span>
                      </div>
                      <div class="nested-drawer" id="bikila-subkids">
                        <div class="p-2 space-y-1.5 text-xs font-mono-code text-gray-300">
                          <div>• Asar Lineage <small class="text-emerald-400">(Children &amp; Grandchildren)</small></div>
                          <div>• Sariah</div>
                          <div>• Khalil</div>
                        </div>
                      </div>
                    </div>

                    <div class="nested-card">
                      <div class="nested-header">
                        <span>Leon Darden ("Rondell")</span>
                        <span style="font-size: 0.75rem; color: var(--color-bloodline);">Son</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- William ("Bobby/Bill") -->
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('william-subdrawer')">
                  <span>William Darden ("Bobby/Bill")</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
                </div>
                <div class="nested-drawer" id="william-subdrawer">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👦 Billy Darden</div>
                    <div>👧 Kim Darden</div>
                  </div>
                </div>
              </div>

              <!-- Darrell -->
              <div class="nested-card blended-card">
                <div class="nested-header" onclick="toggleNested('darrell-subdrawer')">
                  <span style="color: var(--color-blended);">Darrell Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-blended);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="darrell-subdrawer">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div style="color: var(--color-bloodline);">👦 Darrell Darden Jr.</div>
                    <div style="color: var(--color-blended);">👦 Harold</div>
                    <div style="color: var(--color-blended);">👧 Keisha</div>
                  </div>
                </div>
              </div>

              <!-- Pattie -->
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('pattie-subdrawer')">
                  <span>Pattie Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
                </div>
                <div class="nested-drawer" id="pattie-subdrawer">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👦 Keith Darden</div>
                </div>
              </div>

              <!-- Sharon -->
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('sharon-subdrawer')">
                  <span>Sharon Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
                </div>
                <div class="nested-drawer" id="sharon-subdrawer">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👦 Sherron Darden</div>
                    <div>👦 Stephon Darden</div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- PORTAL 2: Mozzell Darden Lineage -->
        <div class="family-card carousel-card" data-card>
          <div class="card-header" onclick="toggleDrawer('portal-mozzell')">
            <div>
              <div class="card-title-text font-black text-amber-300">👴 Mozzell Darden Lineage</div>
              <div class="card-subtitle">7 Primary Lines &amp; Descendants</div>
            </div>
            <span class="badge-tag badge-blood">Gen 3 Portal</span>
          </div>
          <div class="card-drawer" id="portal-mozzell">
            <div class="nested-cards space-y-2">
              
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-bernard')">
                  <span>👨 Bernard Darden <small class="text-amber-400 font-normal">(Oldest Son)</small></span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="moz-bernard">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👧 Beverly</div><div>👧 Latasha</div><div>👦 Larry</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-jr')">
                  <span>👨 Mozzell Darden Jr.</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="moz-jr">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👦 Mozzell Darden 3rd</div><div>👧 Kattely Darden</div><div>👧 Lisa Darden</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-derrick')">
                  <span>👨 Derrick Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="moz-derrick">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👦 Derrick Darden Jr.</div><div>👧 Brianna</div><div>👦 Kamal</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-carol')">
                  <span>👩 Carol Darden ("Bunny")</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
                </div>
                <div class="nested-drawer" id="moz-carol">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jovonda</div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-sheila')">
                  <span>👩 Sheila Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child (1 Grandchild)</span>
                </div>
                <div class="nested-drawer" id="moz-sheila">
                  <div class="p-2 text-xs font-mono-code text-gray-300">
                    <div>👧 Diamond</div>
                    <div class="ml-4 text-emerald-400">└─ 👦 Carter</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-mary')">
                  <span>👩 Mary Washington</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="moz-mary">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👦 Charles Jr.</div><div>👦 Deshaun</div><div>👨 Kevin (Maddison, Dillion, Daniel)</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('moz-lolita')">
                  <span>👩 Lolita Darden</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
                </div>
                <div class="nested-drawer" id="moz-lolita">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👨 Che (Che Jr., Aniyah)</div><div>👧 Brittney</div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- PORTAL 3: Peggy Darden (Peggy Owens) Lineage -->
        <div class="family-card matriarch-card carousel-card" data-card>
          <div class="card-header" onclick="toggleDrawer('portal-peggy')">
            <div>
              <div class="card-title-text matriarch-title">👵 Peggy Darden Lineage</div>
              <div class="card-subtitle" style="color: #ffe066;">Derrick Owens &amp; Debra Profitt Lines</div>
            </div>
            <span class="badge-tag badge-matriarch">Gen 3 Portal</span>
          </div>
          <div class="card-drawer" id="portal-peggy">
            <div class="nested-cards space-y-2">
              <div class="nested-card" style="border-left-color: #ffd700;">
                <div class="nested-header" onclick="toggleNested('peg-derrick')">
                  <span>👨 Derrick Owens</span>
                  <span style="font-size: 0.75rem; color: #ffd700;">▼ 4 Children</span>
                </div>
                <div class="nested-drawer" id="peg-derrick">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👨 Aaron (Aaron Owens Jr.)</div><div>👨 Marques</div><div>👨 Stephan</div><div>👩 Darnielle</div>
                  </div>
                </div>
              </div>

              <div class="nested-card" style="border-left-color: #ffd700;">
                <div class="nested-header" onclick="toggleNested('peg-debra')">
                  <span>👩 Debra Profitt</span>
                  <span style="font-size: 0.75rem; color: #ffd700;">▼ 2 Daughters</span>
                </div>
                <div class="nested-drawer" id="peg-debra">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👩 Jamila (Raevon Profitt)</div>
                    <div>👩 Jewels <small class="text-amber-400">(Reunion Lead: Ashley, Alani)</small></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- PORTAL 4: Johnnie Darden (Johnnie Watson) Lineage -->
        <div class="family-card carousel-card" data-card>
          <div class="card-header" onclick="toggleDrawer('portal-johnnie')">
            <div>
              <div class="card-title-text font-black text-amber-300">👵 Johnnie Darden Lineage</div>
              <div class="card-subtitle">7 Children Household Lines &amp; Descendants</div>
            </div>
            <span class="badge-tag badge-blood">Gen 3 Portal</span>
          </div>
          <div class="card-drawer" id="portal-johnnie">
            <div class="nested-cards space-y-2">
              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-irving')">
                  <span>👨 Irving</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
                </div>
                <div class="nested-drawer" id="j-irving">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👩 Erika (Alisyah, Hailie, Sebastion, Naomi)</div>
                    <div>👨 Joel (Elaine, Adriana, Genisis)</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-louis')">
                  <span>👨 Louis</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 2 Children</span>
                </div>
                <div class="nested-drawer" id="j-louis">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👦 Louis Jr., 👧 Nadine</div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-charles')">
                  <span>👨 Charles</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
                </div>
                <div class="nested-drawer" id="j-charles">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👧 Jenean</div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-darlene')">
                  <span>👩 Darlene</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 3 Children</span>
                </div>
                <div class="nested-drawer" id="j-darlene">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👩 Ronyelle Stallworth (Nyalla, Aden), 👨 Eric, 👩 Melinda</div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header">
                  <span>👨 Donald</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">Son</span>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-donna')">
                  <span>👩 Donna</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 4 Children</span>
                </div>
                <div class="nested-drawer" id="j-donna">
                  <div class="p-2 space-y-1 text-xs font-mono-code text-gray-300">
                    <div>👨 Thomas Earl Watkins (Thomas Jr., Skylar, Archer, Ace)</div>
                    <div>👨 Jason (Devin, Amya, Alexander, Joy)</div>
                    <div>👩 Joy</div>
                    <div>👨 Jeremy (Jayson, Myrikal, Malayah)</div>
                  </div>
                </div>
              </div>

              <div class="nested-card">
                <div class="nested-header" onclick="toggleNested('j-beverly')">
                  <span>👩 Beverly</span>
                  <span style="font-size: 0.75rem; color: var(--color-bloodline);">▼ 1 Child</span>
                </div>
                <div class="nested-drawer" id="j-beverly">
                  <div class="p-2 text-xs font-mono-code text-gray-300">👦 Jonathan</div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div><!-- end gen3-carousel -->
    </div>'''

gen3_pattern = re.compile(r'<!-- Generation 3 & Subsequent Lineages \(Horizontal Swipe Carousel Engine\) -->.*?<!-- Add Family Member Modal -->', re.DOTALL)
html = gen3_pattern.sub(gen3_carousel_new + '\n\n  <!-- Add Family Member Modal -->', html, count=1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully updated Gen 3 & 4 with 4 Branch Sorting Portals!')
