"""Inject graph-controls.js into every HTML page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir, rel_prefix, walk_html

# The standalone controls script
CONTROLS_JS = r"""(function(){var k="graph-controls",de={repelForce:.5,linkDistance:30,centerForce:.3,fontSize:.6,depth:1};
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

def run():
    base = public_dir()
    # Write controls.js
    static_dir = os.path.join(base, "static", "graph")
    os.makedirs(static_dir, exist_ok=True)
    with open(os.path.join(static_dir, "graph-controls.js"), "w", encoding="utf-8") as f:
        f.write(CONTROLS_JS)
    print("  graph-controls.js written")

    # Inject script tag into every HTML page
    injected = 0
    for path, html in walk_html(base):
        prefix = rel_prefix(path, base)
        tag = '<script src="' + prefix + 'static/graph/graph-controls.js"></script>'
        if tag in html:
            continue
        if "</body>" in html:
            html = html.replace("</body>", tag + "\n</body>")
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            injected += 1
    print(f"  Injected into {injected} HTML pages")

if __name__ == "__main__":
    run()
