import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add D3.js script CDN if not present
d3_cdn = '<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>'
if 'd3@7' not in html and '</head>' in html:
    html = html.replace('</head>', f'  {d3_cdn}\n</head>', 1)

# 2. D3 Interactive Mind Map Section HTML
d3_section_html = '''  <!-- ============================================================ -->
  <!-- D3.JS DYNAMIC INTERACTIVE VISUAL MIND MAP ENGINE (GEN 1 → 6) -->
  <!-- ============================================================ -->
  <section class="w-full max-w-7xl mx-auto my-10 px-4">
    <div class="scrim-box p-6 md:p-8 rounded-2xl border-2 border-amber-500/60 shadow-[0_0_50px_rgba(245,158,11,0.3)] relative overflow-hidden bg-black/95">
      
      <!-- Mind Map Header & Interactive Controls -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-amber-500/30 pb-4 mb-6 gap-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl text-amber-400">🧠</span>
          <div>
            <h3 class="font-cyber text-2xl text-white font-black uppercase tracking-wider">
              DARDEN FAMILY HERITAGE <span class="text-amber-400">D3 VISUAL MIND MAP</span>
            </h3>
            <p class="font-mono-code text-xs text-amber-300/80 tracking-wider mt-0.5">
              Click Any Node Badge (+) to Expand / Collapse Generational Branches (Gen 1 → Gen 6)
            </p>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-2">
          <button onclick="expandAllD3Nodes()" class="bg-amber-950 hover:bg-amber-900 border border-amber-500/60 text-amber-300 px-3 py-1.5 rounded font-mono-code text-xs">
            ➕ Expand All
          </button>
          <button onclick="collapseAllD3Nodes()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 px-3 py-1.5 rounded font-mono-code text-xs">
            ➖ Collapse Deep
          </button>
          <button onclick="resetD3View()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 px-3 py-1.5 rounded font-mono-code text-xs">
            🔄 Reset Zoom
          </button>
          <button onclick="openMindmapModal()" class="bg-gradient-to-r from-amber-600 to-yellow-500 hover:from-amber-500 hover:to-yellow-400 text-black font-cyber font-bold text-xs px-4 py-1.5 rounded uppercase tracking-wider shadow-lg">
            ⛶ Fullscreen SVG View
          </button>
        </div>
      </div>

      <!-- Legend Indicator Bar -->
      <div class="flex flex-wrap gap-4 items-center justify-between text-xs font-mono-code mb-4 p-3 bg-black/80 rounded-xl border border-gray-800">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-yellow-400 border border-yellow-200 inline-block shadow-[0_0_10px_#f59e0b]"></span>
          <span class="text-yellow-300">👑 Founders &amp; Matriarchs</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-blue-500 border border-blue-300 inline-block shadow-[0_0_10px_#3b82f6]"></span>
          <span class="text-blue-300">💙 Direct Bloodline</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-purple-500 border border-purple-300 inline-block shadow-[0_0_10px_#a855f7]"></span>
          <span class="text-purple-300">💜 Spouses &amp; Extensions</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-amber-400 font-bold">(+) / (-)</span>
          <span class="text-gray-400">Click Circle Badge to Toggle Branch</span>
        </div>
      </div>

      <!-- D3 SVG Viewport Canvas -->
      <div id="d3MindmapCanvas" class="w-full h-[650px] bg-black/95 rounded-xl border border-amber-500/40 relative overflow-hidden cursor-grab active:cursor-grabbing"></div>
    </div>
  </section>'''

# Replace Mind Map block with D3.js SVG Visual Engine
old_mindmap_pattern = re.compile(r'<!-- DARDEN FAMILY HERITAGE MIND MAP COMPONENT -->.*?<!-- FULLSCREEN MIND MAP POP-UP MODAL -->', re.DOTALL)
if 'DARDEN FAMILY HERITAGE MIND MAP COMPONENT' in html:
    html = old_mindmap_pattern.sub(d3_section_html + '\n\n  <!-- FULLSCREEN MIND MAP POP-UP MODAL -->', html, count=1)

# 3. D3 Tree Script Engine
d3_script_code = '''
  <script>
    // D3.js Dynamic Mind Map Tree Engine
    const dardenTreeData = {
      name: "Sam Darden Sr. & Freddie Shields",
      type: "root",
      role: "Gen 1 Founders",
      children: [
        {
          name: "Sam Darden Jr. ('Cowboy')",
          type: "bloodline",
          role: "Anchor Son (Gen 2)",
          children: [
            {
              name: "George R. Darden ('Ronnie')",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                {
                  name: "Leon Darden ('Rondell')",
                  type: "bloodline",
                  role: "Son (Gen 4)"
                },
                {
                  name: "Bikila Darden",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    {
                      name: "Asar Lineage",
                      type: "bloodline",
                      role: "Gen 5/6",
                      children: [
                        { name: "Asar Children", type: "bloodline", role: "Gen 5" },
                        { name: "Asar Grandchildren", type: "bloodline", role: "Gen 6" }
                      ]
                    },
                    { name: "Sariah", type: "bloodline", role: "Daughter (Gen 5)" },
                    { name: "Khalil", type: "bloodline", role: "Son (Gen 5)" }
                  ]
                }
              ]
            },
            {
              name: "William Darden ('Bobby/Bill')",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                { name: "Billy Darden", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Kim Darden", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Darrell Darden",
              type: "blended",
              role: "Son (Gen 3)",
              children: [
                { name: "Darrell Darden Jr.", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Harold", type: "blended", role: "Family Extension" },
                { name: "Keisha", type: "blended", role: "Family Extension" }
              ]
            },
            {
              name: "Pattie Darden",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                { name: "Keith Darden", type: "bloodline", role: "Son (Gen 4)" }
              ]
            },
            {
              name: "Sharon Darden",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                { name: "Sherron Darden", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Stephon Darden", type: "bloodline", role: "Son (Gen 4)" }
              ]
            }
          ]
        },
        {
          name: "Mozzell Darden",
          type: "bloodline",
          role: "First Son (Gen 2)",
          children: [
            {
              name: "Bernard Darden",
              type: "bloodline",
              role: "Oldest Son (Gen 3)",
              children: [
                { name: "Beverly", type: "bloodline", role: "Daughter (Gen 4)" },
                { name: "Latasha", type: "bloodline", role: "Daughter (Gen 4)" },
                { name: "Larry", type: "bloodline", role: "Son (Gen 4)" }
              ]
            },
            {
              name: "Mozzell Darden Jr.",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                { name: "Mozzell 3rd", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Kattely Darden", type: "bloodline", role: "Daughter (Gen 4)" },
                { name: "Lisa Darden", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Derrick Darden",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                { name: "Derrick Jr.", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Brianna", type: "bloodline", role: "Daughter (Gen 4)" },
                { name: "Kamal", type: "bloodline", role: "Son (Gen 4)" }
              ]
            },
            {
              name: "Carol Darden ('Bunny')",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                { name: "Jovonda", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Sheila Darden",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                {
                  name: "Diamond",
                  type: "bloodline",
                  role: "Daughter (Gen 4)",
                  children: [
                    { name: "Carter", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                }
              ]
            },
            {
              name: "Mary Washington",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                { name: "Charles Jr.", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Deshaun", type: "bloodline", role: "Son (Gen 4)" },
                {
                  name: "Kevin",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Maddison", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Dillion", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Daniel", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                }
              ]
            },
            {
              name: "Lolita Darden",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                {
                  name: "Che",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Che Jr.", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Aniyah", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                },
                { name: "Brittney", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            }
          ]
        },
        {
          name: "Peggy Darden (Owens)",
          type: "matriarch",
          role: "Family Matriarch (Gen 2)",
          children: [
            {
              name: "Derrick Owens",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                {
                  name: "Aaron",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Aaron Owens Jr.", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                },
                { name: "Marques", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Stephan", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Darnielle", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Debra Profitt",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                {
                  name: "Jamila",
                  type: "bloodline",
                  role: "Daughter (Gen 4)",
                  children: [
                    { name: "Raevon Profitt", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                },
                {
                  name: "Jewels (Reunion Lead)",
                  type: "bloodline",
                  role: "Daughter (Gen 4)",
                  children: [
                    { name: "Ashley", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Alani", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                }
              ]
            }
          ]
        },
        {
          name: "Johnnie Darden (Watson)",
          type: "bloodline",
          role: "Daughter (Gen 2)",
          children: [
            {
              name: "Irving",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                {
                  name: "Erika",
                  type: "bloodline",
                  role: "Daughter (Gen 4)",
                  children: [
                    { name: "Alisyah Watson", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Hailie", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Sebastion", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Naomi", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                },
                {
                  name: "Joel",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Elaine", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Adriana", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Genisis Watson", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                }
              ]
            },
            {
              name: "Louis",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                { name: "Louis Jr.", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Nadine", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Charles",
              type: "bloodline",
              role: "Son (Gen 3)",
              children: [
                { name: "Jenean", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            {
              name: "Darlene",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                {
                  name: "Ronyelle Stallworth",
                  type: "bloodline",
                  role: "Daughter (Gen 4)",
                  children: [
                    { name: "Nyalla", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Aden", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                },
                { name: "Eric", type: "bloodline", role: "Son (Gen 4)" },
                { name: "Melinda", type: "bloodline", role: "Daughter (Gen 4)" }
              ]
            },
            { name: "Donald", type: "bloodline", role: "Son (Gen 3)" },
            {
              name: "Donna",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                {
                  name: "Thomas Earl Watkins",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Thomas Jr.", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Skylar", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Archer", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Ace", type: "bloodline", role: "Grandson (Gen 5)" }
                  ]
                },
                {
                  name: "Jason",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Devin", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Amya", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Alexander", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Joy", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                },
                { name: "Joy", type: "bloodline", role: "Daughter (Gen 4)" },
                {
                  name: "Jeremy",
                  type: "bloodline",
                  role: "Son (Gen 4)",
                  children: [
                    { name: "Jayson", type: "bloodline", role: "Grandson (Gen 5)" },
                    { name: "Myrikal", type: "bloodline", role: "Granddaughter (Gen 5)" },
                    { name: "Malayah", type: "bloodline", role: "Granddaughter (Gen 5)" }
                  ]
                }
              ]
            },
            {
              name: "Beverly",
              type: "bloodline",
              role: "Daughter (Gen 3)",
              children: [
                { name: "Jonathan", type: "bloodline", role: "Son (Gen 4)" }
              ]
            }
          ]
        },
        { name: "Lovell Darden ('Uncle Lovell')", type: "elder", role: "Living Elder (Gen 2)" },
        { name: "Sarah Darden", type: "bloodline", role: "Daughter (Gen 2)" }
      ]
    };

    let d3Svg, d3G, d3Root, d3TreeLayout, d3Zoom;
    let d3NodeId = 0;

    function initD3Mindmap() {
      const container = document.getElementById('d3MindmapCanvas');
      if (!container) return;
      container.innerHTML = '';

      const width = container.clientWidth || 1100;
      const height = 650;

      d3Svg = d3.select("#d3MindmapCanvas")
        .append("svg")
        .attr("width", "100%")
        .attr("height", height)
        .attr("viewBox", `0 0 ${width} ${height}`);

      d3Zoom = d3.zoom()
        .scaleExtent([0.4, 2.5])
        .on("zoom", (event) => {
          d3G.attr("transform", event.transform);
        });

      d3Svg.call(d3Zoom);

      d3G = d3.svg.append("g")
        .attr("transform", "translate(120, 50)");

      d3TreeLayout = d3.tree().nodeSize([45, 240]);

      d3Root = d3.hierarchy(dardenTreeData, d => d.children);
      d3Root.x0 = height / 2;
      d3Root.y0 = 0;

      // Auto-collapse nodes at Generation 3 or deeper initially
      d3Root.descendants().forEach(d => {
        if (d.depth >= 2 && d.children) {
          d._children = d.children;
          d.children = null;
        }
      });

      updateD3Tree(d3Root);
    }

    function updateD3Tree(source) {
      const treeData = d3TreeLayout(d3Root);
      const nodes = treeData.descendants();
      const links = treeData.links();

      // Normalize depth spacing
      nodes.forEach(d => { d.y = d.depth * 220; });

      // Links update
      const link = d3G.selectAll("path.d3-link")
        .data(links, d => d.target.id || (d.target.id = ++d3NodeId));

      const linkEnter = link.enter().append("path")
        .attr("class", "d3-link")
        .attr("fill", "none")
        .attr("stroke", d => {
          if (d.target.data.type === 'root' || d.target.data.type === 'matriarch') return "#f59e0b";
          if (d.target.data.type === 'blended') return "#c084fc";
          return "#3b82f6";
        })
        .attr("stroke-width", "2px")
        .attr("stroke-opacity", "0.7")
        .attr("d", d => {
          const o = { x: source.x0, y: source.y0 };
          return d3LinkHorizontal(o, o);
        });

      const linkUpdate = linkEnter.merge(link);
      linkUpdate.transition().duration(400)
        .attr("d", d => d3LinkHorizontal(d.source, d.target));

      link.exit().transition().duration(400)
        .attr("d", d => {
          const o = { x: source.x, y: source.y };
          return d3LinkHorizontal(o, o);
        })
        .remove();

      // Nodes update
      const node = d3G.selectAll("g.d3-node")
        .data(nodes, d => d.id || (d.id = ++d3NodeId));

      const nodeEnter = node.enter().append("g")
        .attr("class", "d3-node")
        .attr("transform", d => `translate(${source.y0},${source.x0})`)
        .style("cursor", "pointer");

      // Node background card
      nodeEnter.append("rect")
        .attr("x", -10)
        .attr("y", -20)
        .attr("width", 195)
        .attr("height", 40)
        .attr("rx", 10)
        .attr("ry", 10)
        .attr("fill", d => {
          if (d.data.type === 'root' || d.data.type === 'matriarch') return "#211a0d";
          if (d.data.type === 'blended') return "#161b22";
          return "#0d1117";
        })
        .attr("stroke", d => {
          if (d.data.type === 'root' || d.data.type === 'matriarch') return "#f59e0b";
          if (d.data.type === 'blended') return "#c084fc";
          return "#38bdf8";
        })
        .attr("stroke-width", "2px")
        .on("click", (event, d) => {
          event.stopPropagation();
          openMemberModal(d.data.name, d.data.role || 'Mindmap Node');
        });

      // Node text name
      nodeEnter.append("text")
        .attr("x", 10)
        .attr("y", -3)
        .attr("fill", "#ffffff")
        .style("font-size", "11px")
        .style("font-weight", "bold")
        .style("font-family", "monospace")
        .text(d => d.data.name.length > 20 ? d.data.name.substring(0, 18) + '...' : d.data.name);

      // Node subtitle / role
      nodeEnter.append("text")
        .attr("x", 10)
        .attr("y", 12)
        .attr("fill", "#9ca3af")
        .style("font-size", "9px")
        .style("font-family", "sans-serif")
        .text(d => d.data.role || '');

      // Expand / Collapse Badge (+) / (-) Button
      const badgeG = nodeEnter.append("g")
        .attr("transform", "translate(185, 0)")
        .on("click", (event, d) => {
          event.stopPropagation();
          toggleD3Node(d);
        });

      badgeG.append("circle")
        .attr("r", 10)
        .attr("fill", d => (d.children || d._children) ? "#f59e0b" : "transparent")
        .attr("stroke", "#f59e0b")
        .attr("stroke-width", "1.5px");

      badgeG.append("text")
        .attr("text-anchor", "middle")
        .attr("dy", "3.5px")
        .attr("fill", "#000000")
        .style("font-size", "11px")
        .style("font-weight", "bold")
        .text(d => d._children ? "+" : (d.children ? "−" : ""));

      const nodeUpdate = nodeEnter.merge(node);
      nodeUpdate.transition().duration(400)
        .attr("transform", d => `translate(${d.y},${d.x})`);

      // Update badge text dynamically
      nodeUpdate.select("g text")
        .text(d => d._children ? "+" : (d.children ? "−" : ""));

      node.exit().transition().duration(400)
        .attr("transform", d => `translate(${source.y},${source.x})`)
        .remove();

      nodes.forEach(d => {
        d.x0 = d.x;
        d.y0 = d.y;
      });
    }

    function d3LinkHorizontal(s, t) {
      return `M ${s.y} ${s.x}
              C ${(s.y + t.y) / 2} ${s.x},
                ${(s.y + t.y) / 2} ${t.x},
                ${t.y} ${t.x}`;
    }

    function toggleD3Node(d) {
      if (d.children) {
        d._children = d.children;
        d.children = null;
      } else if (d._children) {
        d.children = d._children;
        d._children = null;
      }
      updateD3Tree(d);
    }

    function expandAllD3Nodes() {
      if (!d3Root) return;
      d3Root.descendants().forEach(d => {
        if (d._children) {
          d.children = d._children;
          d._children = null;
        }
      });
      updateD3Tree(d3Root);
    }

    function collapseAllD3Nodes() {
      if (!d3Root) return;
      d3Root.descendants().forEach(d => {
        if (d.depth >= 2 && d.children) {
          d._children = d.children;
          d.children = null;
        }
      });
      updateD3Tree(d3Root);
    }

    function resetD3View() {
      if (d3Svg && d3Zoom) {
        d3Svg.transition().duration(500).call(d3Zoom.transform, d3.zoomIdentity.translate(120, 50).scale(1));
      }
    }

    document.addEventListener("DOMContentLoaded", () => {
      setTimeout(initD3Mindmap, 400);
    });
  </script>
'''

if '</script>' in html:
    html = html.replace('</script>', d3_script_code + '\n</script>', 1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Also save standalone single-file HTML document darden_family_tree_v2.html!
with open('darden_family_tree_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully created D3.js SVG Visual Interactive Mind Map in darden_family_tree.html and darden_family_tree_v2.html!')
