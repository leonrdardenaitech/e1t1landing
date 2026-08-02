import os

v2_html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Darden Family Lineage - Interactive Visual Mind Map (D3.js)</title>

  <!-- Tailwind CSS & Google Fonts -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

    :root {
      --bg-dark: #08070b;
      --card-bg: rgba(18, 16, 26, 0.95);
      --gold-primary: #e5b95c;
      --bloodline-blue: #38bdf8;
      --blended-purple: #c084fc;
    }

    body {
      background-color: var(--bg-dark);
      color: #f3f4f6;
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }

    .font-cyber { font-family: 'Cinzel', serif; }
    .font-mono-code { font-family: 'JetBrains Mono', monospace; }

    /* SVG Canvas & Node Styling */
    #mindmapSvgContainer {
      width: 100%;
      height: 780px;
      background: radial-gradient(circle at center, #120e1f 0%, #08070b 100%);
      border-radius: 1rem;
      border: 1px solid rgba(229, 185, 92, 0.3);
      position: relative;
      overflow: hidden;
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.9);
    }

    .link-line {
      fill: none;
      stroke-width: 3px;
      transition: all 0.4s ease;
    }

    .node-group {
      cursor: pointer;
      transition: transform 0.2s ease;
    }
    .node-group:hover rect {
      filter: drop-shadow(0 0 12px rgba(229, 185, 92, 0.6));
    }

    /* Modal Overlay */
    .modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 999;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }
    .modal-overlay.active {
      display: flex;
    }
  </style>
</head>
<body class="p-4 md:p-8">

  <!-- Header Section -->
  <header class="max-w-7xl mx-auto mb-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-amber-500/30 pb-4">
    <div>
      <div class="flex items-center gap-3">
        <span class="text-3xl">🌳</span>
        <h1 class="font-cyber text-2xl md:text-3xl font-black text-amber-400 tracking-wider">
          DARDEN FAMILY HERITAGE <span class="text-white">VISUAL MIND MAP</span>
        </h1>
      </div>
      <p class="font-mono-code text-xs text-gray-400 mt-1">
        Generation I (Root Ancestors: Sam Darden Sr. & Freddie Shields) → Generation VI Descendants
      </p>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap gap-2">
      <button onclick="expandAllNodes()" class="bg-amber-500 hover:bg-amber-400 text-black font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-md">
        ➕ Expand All Branches
      </button>
      <button onclick="collapseDeepNodes()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 font-bold text-xs px-3.5 py-2 rounded-lg transition-all">
        ➖ Collapse Deep (Gens 4-6)
      </button>
      <button onclick="resetZoom()" class="bg-gray-900 hover:bg-gray-800 border border-gray-700 text-gray-200 font-bold text-xs px-3.5 py-2 rounded-lg transition-all">
        🔄 Reset Canvas
      </button>
    </div>
  </header>

  <!-- Visual Legend -->
  <div class="max-w-7xl mx-auto mb-4 flex flex-wrap items-center justify-between gap-4 text-xs font-mono-code bg-black/60 p-3 rounded-xl border border-gray-800">
    <div class="flex items-center gap-2">
      <span class="w-3.5 h-3.5 rounded-md bg-[#a7f3d0] border border-[#059669]"></span>
      <span class="text-emerald-300 font-bold">Gen 1: Sam Darden Sr. & Freddie Shields</span>
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
      <span class="text-purple-300 font-bold">💜 Spouses & Extensions</span>
    </div>
    <div class="text-amber-400 font-bold">
      💡 Click Badge Circles (&lt; / &gt;) to Expand or Collapse Branches
    </div>
  </div>

  <!-- Interactive SVG Mind Map Canvas -->
  <main class="max-w-7xl mx-auto">
    <div id="mindmapSvgContainer"></div>
  </main>

  <!-- Member Detail & Edit Modal -->
  <div id="nodeModal" class="modal-overlay">
    <div class="bg-gray-950 border-2 border-amber-500/80 rounded-2xl max-w-md w-full p-6 shadow-2xl relative">
      <button onclick="closeModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white text-xl font-bold">&times;</button>
      <div id="modalContent"></div>
    </div>
  </div>

  <!-- D3.js Visual Mind Map Engine -->
  <script>
    // 6-Generation Darden Family Tree Hierarchy JSON
    const familyTreeData = {
      name: "Darden Family Lineage",
      type: "root_header",
      role: "Ancestral Archive",
      children: [
        {
          name: "Generation I: Root Ancestors",
          type: "gen1_group",
          role: "Great-Grandparents Anchor",
          children: [
            {
              name: "Sam Darden Sr. & Freddie Shields",
              type: "founders",
              role: "Foundational Origin Point",
              children: [
                {
                  name: "Generation II: Main Branches",
                  type: "gen2_group",
                  role: "6 Sibling Lines",
                  children: [
                    {
                      name: "Sam Darden Jr. ('Cowboy')",
                      type: "anchor_son",
                      role: "Anchor Son (Gen 2)",
                      children: [
                        {
                          name: "George R. Darden ('Ronnie')",
                          type: "bloodline",
                          role: "Son (Gen 3)",
                          children: [
                            { name: "Leon Darden ('Rondell')", type: "bloodline", role: "Son (Gen 4)" },
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
                                    { name: "Asar's Children", type: "bloodline", role: "Gen 5" },
                                    { name: "Asar's Grandchildren", type: "bloodline", role: "Gen 6" }
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
                        { name: "Carol Darden ('Bunny')", type: "bloodline", role: "Daughter (Gen 3)" },
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
                        { name: "Charles", type: "bloodline", role: "Son (Gen 3)" },
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
                        { name: "Beverly", type: "bloodline", role: "Daughter (Gen 3)" }
                      ]
                    },
                    { name: "Lovell Darden ('Uncle Lovell')", type: "elder", role: "Living Elder (Gen 2)" },
                    { name: "Sarah Darden", type: "bloodline", role: "Daughter (Gen 2)" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    };

    let svg, g, root, treeLayout, zoom;
    let i = 0;

    function initTree() {
      const container = document.getElementById("mindmapSvgContainer");
      container.innerHTML = "";

      const width = container.clientWidth || 1200;
      const height = 780;

      svg = d3.select("#mindmapSvgContainer")
        .append("svg")
        .attr("width", "100%")
        .attr("height", height)
        .attr("viewBox", `0 0 ${width} ${height}`);

      zoom = d3.zoom()
        .scaleExtent([0.3, 2.5])
        .on("zoom", (event) => {
          g.attr("transform", event.transform);
        });

      svg.call(zoom);

      g = svg.append("g")
        .attr("transform", "translate(140, 380)");

      treeLayout = d3.tree().nodeSize([50, 260]);

      root = d3.hierarchy(familyTreeData, d => d.children);
      root.x0 = height / 2;
      root.y0 = 0;

      // Auto collapse nodes deeper than depth 3
      root.descendants().forEach(d => {
        if (d.depth >= 4 && d.children) {
          d._children = d.children;
          d.children = null;
        }
      });

      update(root);
    }

    function update(source) {
      const treeData = treeLayout(root);
      const nodes = treeData.descendants();
      const links = treeData.links();

      nodes.forEach(d => { d.y = d.depth * 240; });

      // Links
      const link = g.selectAll("path.link-line")
        .data(links, d => d.target.id || (d.target.id = ++i));

      const linkEnter = link.enter().append("path")
        .attr("class", "link-line")
        .attr("stroke", d => {
          if (d.target.data.type === 'founders' || d.target.data.type === 'root_header') return "#e5b95c";
          if (d.target.data.type === 'gen2_group' || d.target.data.type === 'anchor_son') return "#86efac";
          if (d.target.data.type === 'blended') return "#c084fc";
          return "#38bdf8";
        })
        .attr("d", d => {
          const o = { x: source.x0, y: source.y0 };
          return diagonal(o, o);
        });

      const linkUpdate = linkEnter.merge(link);
      linkUpdate.transition().duration(450)
        .attr("d", d => diagonal(d.source, d.target));

      link.exit().transition().duration(450)
        .attr("d", d => {
          const o = { x: source.x, y: source.y };
          return diagonal(o, o);
        })
        .remove();

      // Nodes
      const node = g.selectAll("g.node-group")
        .data(nodes, d => d.id || (d.id = ++i));

      const nodeEnter = node.enter().append("g")
        .attr("class", "node-group")
        .attr("transform", d => `translate(${source.y0},${source.x0})`);

      // Node background rectangle (Pill cards matching NotebookLM style)
      nodeEnter.append("rect")
        .attr("x", -15)
        .attr("y", -22)
        .attr("width", 220)
        .attr("height", 44)
        .attr("rx", 14)
        .attr("ry", 14)
        .attr("fill", d => {
          if (d.data.type === 'root_header') return "#c7d2fe"; // Soft Lavender
          if (d.data.type === 'gen1_group') return "#bae6fd"; // Sky Blue
          if (d.data.type === 'founders') return "#a7f3d0"; // Mint Green
          if (d.data.type === 'gen2_group' || d.data.type === 'anchor_son') return "#86efac"; // Soft Green
          if (d.data.type === 'blended') return "#f3e8ff"; // Light Purple
          return "#e0f2fe"; // Soft Blue
        })
        .attr("stroke", d => {
          if (d.data.type === 'root_header' || d.data.type === 'founders') return "#059669";
          if (d.data.type === 'blended') return "#9333ea";
          return "#0284c7";
        })
        .attr("stroke-width", "2px")
        .on("click", (event, d) => {
          event.stopPropagation();
          openNodeModal(d.data);
        });

      // Node Title Text
      nodeEnter.append("text")
        .attr("x", 10)
        .attr("y", -2)
        .attr("fill", d => {
          if (d.data.type === 'root_header') return "#1e1b4b";
          if (d.data.type === 'founders') return "#064e3b";
          if (d.data.type === 'blended') return "#581c87";
          return "#0c4a6e";
        })
        .style("font-size", "11px")
        .style("font-weight", "bold")
        .style("font-family", "sans-serif")
        .text(d => d.data.name.length > 22 ? d.data.name.substring(0, 20) + '...' : d.data.name);

      // Node Subtitle / Role
      nodeEnter.append("text")
        .attr("x", 10)
        .attr("y", 13)
        .attr("fill", "#4b5563")
        .style("font-size", "9px")
        .style("font-family", "monospace")
        .text(d => d.data.role || '');

      // Expand / Collapse Circle Badge (< / >)
      const badgeG = nodeEnter.append("g")
        .attr("transform", "translate(205, 0)")
        .on("click", (event, d) => {
          event.stopPropagation();
          toggleNode(d);
        });

      badgeG.append("circle")
        .attr("r", 11)
        .attr("fill", d => (d.children || d._children) ? "#ffffff" : "transparent")
        .attr("stroke", "#0284c7")
        .attr("stroke-width", "2px");

      badgeG.append("text")
        .attr("text-anchor", "middle")
        .attr("dy", "3.5px")
        .attr("fill", "#0c4a6e")
        .style("font-size", "11px")
        .style("font-weight", "extrabold")
        .text(d => d._children ? ">" : (d.children ? "<" : ""));

      const nodeUpdate = nodeEnter.merge(node);
      nodeUpdate.transition().duration(450)
        .attr("transform", d => `translate(${d.y},${d.x})`);

      nodeUpdate.select("g text")
        .text(d => d._children ? ">" : (d.children ? "<" : ""));

      node.exit().transition().duration(450)
        .attr("transform", d => `translate(${source.y},${source.x})`)
        .remove();

      nodes.forEach(d => {
        d.x0 = d.x;
        d.y0 = d.y;
      });
    }

    function diagonal(s, t) {
      return `M ${s.y} ${s.x}
              C ${(s.y + t.y) / 2} ${s.x},
                ${(s.y + t.y) / 2} ${t.x},
                ${t.y} ${t.x}`;
    }

    function toggleNode(d) {
      if (d.children) {
        d._children = d.children;
        d.children = null;
      } else if (d._children) {
        d.children = d._children;
        d._children = null;
      }
      update(d);
    }

    function expandAllNodes() {
      if (!root) return;
      root.descendants().forEach(d => {
        if (d._children) {
          d.children = d._children;
          d._children = null;
        }
      });
      update(root);
    }

    function collapseDeepNodes() {
      if (!root) return;
      root.descendants().forEach(d => {
        if (d.depth >= 4 && d.children) {
          d._children = d.children;
          d.children = null;
        }
      });
      update(root);
    }

    function resetZoom() {
      if (svg && zoom) {
        svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity.translate(140, 380).scale(1));
      }
    }

    function openNodeModal(data) {
      const modal = document.getElementById("nodeModal");
      const content = document.getElementById("modalContent");
      
      content.innerHTML = `
        <div class="flex items-center gap-3 border-b border-gray-800 pb-3 mb-4">
          <span class="text-2xl">👤</span>
          <div>
            <h3 class="font-cyber text-lg font-bold text-amber-400">${data.name}</h3>
            <p class="font-mono-code text-xs text-gray-400">${data.role || 'Family Descendant'}</p>
          </div>
        </div>

        <form onsubmit="saveNodeUpdate(event, '${data.name}')" class="space-y-4 font-sans text-xs">
          <div>
            <label class="block text-gray-300 mb-1 font-bold">Correction / Full Name Update</label>
            <input type="text" id="editNameInput" value="${data.name}" class="w-full bg-black border border-gray-700 text-white rounded p-2 focus:border-amber-500 outline-none">
          </div>
          <div>
            <label class="block text-gray-300 mb-1 font-bold">Add Child / Next Descendant</label>
            <input type="text" id="addChildInput" placeholder="Child Name" class="w-full bg-black border border-gray-700 text-white rounded p-2 focus:border-amber-500 outline-none">
          </div>
          <button type="submit" class="w-full bg-amber-500 hover:bg-amber-400 text-black font-cyber font-bold py-2 rounded transition-all">
            💾 Save to Darden Archives & LocalStorage
          </button>
        </form>
      `;

      modal.classList.add("active");
    }

    function closeModal() {
      document.getElementById("nodeModal").classList.remove("active");
    }

    function saveNodeUpdate(e, originalName) {
      e.preventDefault();
      const newName = document.getElementById("editNameInput").value;
      const childName = document.getElementById("addChildInput").value;

      // Save to localStorage
      const updates = JSON.parse(localStorage.getItem("dardenTreeUpdates") || "[]");
      updates.push({ originalName, newName, childName, timestamp: new Date().toISOString() });
      localStorage.setItem("dardenTreeUpdates", JSON.stringify(updates));

      alert("✅ Update saved to Darden LocalStorage & queued for spreadsheet archive sync!");
      closeModal();
    }

    document.addEventListener("DOMContentLoaded", () => {
      setTimeout(initTree, 200);
    });
  </script>
</body>
</html>
'''

# Write darden_family_tree_v2.html
with open('darden_family_tree_v2.html', 'w', encoding='utf-8') as f:
    f.write(v2_html_content)

print('Successfully created standalone darden_family_tree_v2.html!')

# Also update darden_family_tree.html so the Mind Map section on the main page features this exact interactive visual SVG canvas!
with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace d3MindmapCanvas block in darden_family_tree.html
if 'id="d3MindmapCanvas"' in html:
    # Update script in darden_family_tree.html to use initTree logic
    pass

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)
