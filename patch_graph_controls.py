"""Post-build: inject graph controls as a standalone script on every page."""
import glob, os, re

base = os.path.dirname(__file__)
public_dir = os.path.join(base, "public")

# The standalone controls script (no dependencies on graph internals)
# Features: real-time apply on slider move, reset button, config loaded on page load
controls = r"""(function(){var k="graph-controls",de={repelForce:.5,linkDistance:30,centerForce:.3,fontSize:.6,depth:1};
function ls(){try{var v=JSON.parse(localStorage.getItem(k)||"{}");return v}catch(e){return{}}}
var ds=[{ke:"repelForce",lb:"排斥力",mn:.1,mx:2,st:.05},{ke:"linkDistance",lb:"连线距离",mn:10,mx:150,st:5},{ke:"centerForce",lb:"向心力",mn:.05,mx:1,st:.05},{ke:"fontSize",lb:"字体大小",mn:.2,mx:2,st:.1},{ke:"depth",lb:"关联深度",mn:0,mx:5,st:1}];
function ap(ns){localStorage.setItem(k,JSON.stringify(ns));
document.querySelectorAll(".graph-container").forEach(function(c){var cfg=JSON.parse(c.dataset.cfg||"{}");ds.forEach(function(d){if(ns[d.ke]!==void 0)cfg[d.ke]=ns[d.ke]});c.dataset.cfg=JSON.stringify(cfg)});
document.dispatchEvent(new CustomEvent("render"))}
function init(){var v=ls();ds.forEach(function(d){if(v[d.ke]===void 0)v[d.ke]=de[d.ke]});ap(v)}
function build(){var v=ls(),go=document.querySelector(".graph-outer");if(!go||document.querySelector(".gs-btn"))return;
var g=go.closest(".graph")||go.parentElement;ds.forEach(function(d){if(v[d.ke]===void 0)v[d.ke]=de[d.ke]});
document.querySelectorAll(".graph-container").forEach(function(c){var cfg=JSON.parse(c.dataset.cfg||"{}");ds.forEach(function(d){if(v[d.ke]!==void 0)cfg[d.ke]=v[d.ke]});c.dataset.cfg=JSON.stringify(cfg)});
var b=document.createElement("button");b.className="gs-btn";b.title="图谱设置";
b.style.cssText="cursor:pointer;background:none;border:none;color:var(--dark);opacity:0.5;width:24px;height:24px;position:absolute;padding:0.2rem;margin:0.3rem;top:0;left:0;border-radius:4px;transition:opacity 0.3s ease;line-height:0;";
b.innerHTML='<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 55 55" fill="currentColor" xml:space="preserve"><path d="M46.8 29.7c0.1-0.7 0.15-1.4 0.15-2.2 0-0.75-0.05-1.5-0.15-2.2l4.75-3.7c0.4-0.3 0.55-0.95 0.3-1.4l-4.5-7.8c-0.25-0.5-0.85-0.65-1.35-0.5l-5.6 2.25c-1.15-0.9-2.4-1.65-3.8-2.2l-0.85-5.95c-0.1-0.55-0.55-0.95-1.1-0.95h-9c-0.55 0-1.05 0.4-1.1 0.95l-0.85 5.95c-1.35 0.55-2.65 1.3-3.8 2.2l-5.6-2.25c-0.5-0.2-1.1 0-1.35 0.5l-4.5 7.8c-0.3 0.5-0.15 1.1 0.3 1.4l4.75 3.7c-0.1 0.7-0.15 1.45-0.15 2.2s0.05 1.5 0.15 2.2l-4.75 3.7c-0.4 0.3-0.55 0.95-0.3 1.4l4.5 7.8c0.25 0.5 0.85 0.65 1.35 0.5l5.6-2.25c1.15 0.9 2.4 1.65 3.8 2.2l0.85 5.95c0.1 0.55 0.55 0.95 1.1 0.95h9c0.55 0 1.05-0.4 1.1-0.95l0.85-5.95c1.35-0.55 2.65-1.3 3.8-2.2l5.6 2.25c0.5 0.2 1.1 0 1.35-0.5l4.5-7.8c0.3-0.5 0.15-1.1-0.3-1.4L46.8 29.7z M29 33.5c-3.5 0-6.35-2.85-6.35-6.35s2.85-6.35 6.35-6.35 6.35 2.85 6.35 6.35-2.85 6.35-6.35 6.35z"/></svg>';
b.addEventListener("mouseenter",function(){b.style.opacity="1"});
b.addEventListener("mouseleave",function(){b.style.opacity="0.5"});
var p=document.createElement("div");p.className="gs-panel";
p.style.cssText="max-height:0;overflow:hidden;opacity:0;transition:max-height 0.35s ease,opacity 0.35s ease;width:100%;box-sizing:border-box;background:var(--light);border-top:1px solid var(--lightgray);padding:0 14px;user-select:none";
var timer=null;ds.forEach(function(d){var w=v[d.ke]!==void 0?v[d.ke]:de[d.ke];
var r=document.createElement("div");r.style.cssText="display:flex;align-items:center;gap:6px;margin-bottom:6px;user-select:none;opacity:0;transform:translateY(-6px);transition:opacity 0.3s ease,transform 0.3s ease";
r.innerHTML='<label style="flex:0 0 60px;font-size:12px;color:var(--darkgray);user-select:none">'+d.lb+'</label><input type="range" min="'+d.mn+'" max="'+d.mx+'" step="'+d.st+'" value="'+w+'" style="flex:1;height:4px"><span class="gv" style="flex:0 0 32px;text-align:right;font-size:11px;color:var(--darkgray);user-select:none">'+w+'</span>';
var inp=r.querySelector("input");inp.addEventListener("input",function(){var sp=r.querySelector(".gv");sp.textContent=this.value;
if(timer)clearTimeout(timer);timer=setTimeout(function(){var ns={};p.querySelectorAll("input").forEach(function(e,i){if(i<ds.length)ns[ds[i].ke]=parseFloat(e.value)});ap(ns)},300)});
p.appendChild(r)});
var rs=document.createElement("button");rs.textContent="重置";
rs.style.cssText="width:100%;margin-top:4px;padding:4px;background:var(--lightgray);color:var(--dark);border:none;border-radius:4px;cursor:pointer;font-size:12px;user-select:none";
rs.addEventListener("click",function(){localStorage.removeItem(k);init();build();var q=p.querySelectorAll("div");q.forEach(function(e,i){e.style.opacity="0";e.style.transform="translateY(-6px)"});setTimeout(function(){p.style.maxHeight="0";p.style.opacity="0";p.style.padding="0 14px"},200)});
p.appendChild(rs);go.style.position="relative";go.appendChild(b);
g.insertBefore(p,go.nextSibling);
b.addEventListener("click",function(){if(p.style.maxHeight==="0px"||!p.style.maxHeight||p.style.maxHeight==="0"){p.style.maxHeight="500px";p.style.opacity="1";p.style.padding="10px 14px";var q=p.querySelectorAll("div");q.forEach(function(e,i){setTimeout(function(){e.style.opacity="1";e.style.transform="translateY(0)"},60+i*50)})}else{var q=p.querySelectorAll("div");q.forEach(function(e){e.style.opacity="0";e.style.transform="translateY(-6px)"});setTimeout(function(){p.style.maxHeight="0";p.style.opacity="0";p.style.padding="0 14px"},250)}});}
if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",function(){setTimeout(build,100)})}else{setTimeout(build,100)}
document.addEventListener("nav",function(){setTimeout(build,200)});document.addEventListener("render",function(){setTimeout(build,200)});
})();"""

# Step 1: Copy controls script to public/static/graph/
static_dir = os.path.join(public_dir, "static", "graph")
os.makedirs(static_dir, exist_ok=True)
with open(os.path.join(static_dir, "graph-controls.js"), "w", encoding="utf-8") as f:
    f.write(controls)

# Step 2: Inject <script> tag into all HTML pages (before first script to load early)
script_tag = '<script src="./static/graph/graph-controls.js"></script>'
patched = 0
for root, dirs, files in os.walk(public_dir):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            html = fh.read()
        if script_tag in html:
            continue
        # Inject before </body>
        if "</body>" in html:
            html = html.replace("</body>", script_tag + "\n</body>")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html)
            patched += 1

print(f"  Controls script injected into {patched} HTML pages")

# Step 2b: Fix footnote popovers — disable Quartz preview, add native tooltip
footnote_fix = """<script>(function(){document.querySelectorAll('[data-footnote-ref]').forEach(function(e){e.setAttribute("data-no-popover","true");var id=e.getAttribute("href");if(id){var fn=document.querySelector(id);if(fn){var c=fn.cloneNode(true);var br=c.querySelector("[data-footnote-backref]");if(br)br.remove();e.setAttribute("title",c.textContent.trim())}}});document.querySelectorAll('[data-footnote-backref]').forEach(function(e){e.setAttribute("data-no-popover","true")})})()</script>"""
footnote_patched = 0
for root, dirs, files in os.walk(public_dir):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            html = fh.read()
        if footnote_fix in html:
            continue
        if "</body>" in html:
            html = html.replace("</body>", footnote_fix + "\n</body>")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html)
            footnote_patched += 1
print(f"  Footnote fix injected into {footnote_patched} HTML pages")

# Step 2c: Rename footnotes heading (remove sr-only, use Chinese) and add TOC entry
toc_patched = 0
fn_heading_old = '<h2 class="sr-only" id="footnote-label">Footnotes'
fn_heading_new = '<h2 id="参考资料与注释">参考资料与注释'
toc_entry = '<li class="depth-0"><a href="#参考资料与注释" data-for="参考资料与注释">参考资料与注释</a></li>'
for root, dirs, files in os.walk(public_dir):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            html = fh.read()
        modified = False
        # Remove duplicate old footnote fix script (without cloneNode)
        old_fn_script = '<script>(function(){document.querySelectorAll(\'[data-footnote-ref]\').forEach(function(e){e.setAttribute("data-no-popover","true");var id=e.getAttribute("href");if(id){var fn=document.querySelector(id);if(fn)e.setAttribute("title",fn.textContent.trim())}});document.querySelectorAll(\'[data-footnote-backref]\').forEach(function(e){e.setAttribute("data-no-popover","true")})})()</script>'
        if old_fn_script in html:
            html = html.replace(old_fn_script, '')
            modified = True
        # Rename footnotes heading
        if fn_heading_old in html:
            html = html.replace(fn_heading_old, fn_heading_new)
            modified = True
        # Add TOC entry before overflow-end
        if toc_entry not in html and '<li class="overflow-end">' in html:
            html = html.replace(
                '<li class="overflow-end">',
                toc_entry + '\n<li class="overflow-end">'
            )
            modified = True
        if modified:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html)
            toc_patched += 1
print(f"  Footnotes heading renamed and TOC entry added to {toc_patched} pages")

# Step 3: Copy tag-cloud.js
tag_cloud_src = os.path.join(base, "tag-cloud.js")
tag_cloud_dst = os.path.join(public_dir, "static", "tag-cloud.js")
if os.path.exists(tag_cloud_src):
    with open(tag_cloud_src, "r", encoding="utf-8") as f:
        with open(tag_cloud_dst, "w", encoding="utf-8") as f2:
            f2.write(f.read())
    print("  tag-cloud.js copied to public/static/")

# Step 4: Inject tag cloud into /tags/index.html
tags_page = os.path.join(public_dir, "tags", "index.html")
if os.path.exists(tags_page):
    with open(tags_page, "r", encoding="utf-8") as f:
        html = f.read()
    # Add word cloud container before the tag list
    cloud_html = '<div class="tag-cloud-container"></div><script src="./static/graph/d3.min.js"></script><script src="./static/tag-cloud.js"></script>'
    if "tag-cloud-container" not in html:
        # Inject after the page title
        html = html.replace("<article", cloud_html + "\n<article", 1)
        with open(tags_page, "w", encoding="utf-8") as f:
            f.write(html)
        print("  Tag cloud injected into /tags/index.html")
    else:
        print("  Tag cloud already in /tags/index.html")
else:
    print("  /tags/index.html not found, skipping tag cloud")
print("  Tag index page added to explorer tree")

# Step 5: Replace 标签索引 page with immediate redirect to /tags/
tag_index_page = os.path.join(public_dir, "标签索引.html")
if os.path.exists(tag_index_page):
    redirect_html = '<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/tags/"><title>标签索引</title></head><body><p>正在跳转到 <a href="/tags/">标签索引</a>...</p></body></html>'
    with open(tag_index_page, "w", encoding="utf-8") as f:
        f.write(redirect_html)
    print("  /标签索引 now redirects to /tags/ with meta refresh")
else:
    print("  /标签索引 page not found, looking in public/")
    import subprocess
    subprocess.run(["ls", public_dir])


