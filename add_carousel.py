import re

with open('darden_family_tree.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for Horizontal Carousel
carousel_css = '''
    /* Horizontal Swipe Carousel Engine */
    .carousel-container {
      display: flex;
      gap: 1rem;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding-bottom: 1rem;
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
    }

    .carousel-container::-webkit-scrollbar {
      height: 6px;
    }
    .carousel-container::-webkit-scrollbar-track {
      background: rgba(8, 7, 11, 0.8);
      border-radius: 10px;
    }
    .carousel-container::-webkit-scrollbar-thumb {
      background: var(--primary-gold);
      border-radius: 10px;
    }

    .carousel-card {
      flex: 0 0 320px;
      scroll-snap-align: start;
      min-width: 290px;
    }

    .chevron-btn {
      background: rgba(229, 185, 92, 0.15);
      border: 1px solid var(--primary-gold);
      color: var(--primary-gold);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-weight: bold;
      transition: all 0.2s ease;
    }
    .chevron-btn:hover {
      background: var(--primary-gold);
      color: #08070b;
    }
'''

# Insert Carousel CSS into <style>
if '</style>' in html and 'carousel-container' not in html:
    html = html.replace('</style>', carousel_css + '\n</style>', 1)

# Upgrade Gen 3 Section Header with Horizontal Swipe & Chevron Navigation
gen3_header_old = '''    <!-- Generation 3 & Subsequent Lineages (Collapsible Cards for Every Line) -->
    <div class="gen-group">
      <div class="gen-label">
        <span>Generation 3 & Subsequent Lineages</span>
        <span style="font-size: 0.72rem; opacity: 0.8;">Tap any name to collapse / expand children</span>
      </div>'''

gen3_header_new = '''    <!-- Generation 3 & Subsequent Lineages (Horizontal Swipe Carousel Engine) -->
    <div class="gen-group">
      <div class="gen-label flex justify-between items-center">
        <div>
          <span>Generation 3 · Household Lines</span>
          <span style="font-size: 0.72rem; opacity: 0.8;" class="block mt-0.5">👈 SWIPE HORIZONTALLY OR CLICK CHEVRONS ◄ ► TO EXPLORE BRANCHES 👉</span>
        </div>
        <!-- Chevron Controls -->
        <div class="flex gap-2">
          <button onclick="scrollCarousel('gen3-carousel', -340)" class="chevron-btn" title="Swipe Left">◄</button>
          <button onclick="scrollCarousel('gen3-carousel', 340)" class="chevron-btn" title="Swipe Right">►</button>
        </div>
      </div>'''

html = html.replace(gen3_header_old, gen3_header_new, 1)

# Add JavaScript helper scrollCarousel
js_helper = '''
    function scrollCarousel(containerId, distance) {
      const container = document.getElementById(containerId);
      if (container) {
        container.scrollBy({ left: distance, behavior: 'smooth' });
      }
    }
'''

if '</script>' in html and 'scrollCarousel' not in html:
    html = html.replace('</script>', js_helper + '\n</script>', 1)

with open('darden_family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully added Horizontal Carousel Engine to darden_family_tree.html!')
