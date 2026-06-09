"""Footnotes: heading rename, hover tooltip, TOC entry, data-no-popover."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir, walk_html

# Injected script: disable popover, add native tooltip on hover
FOOTNOTE_FIX_JS = """<script>(function(){document.querySelectorAll('[data-footnote-ref]').forEach(function(e){e.setAttribute("data-no-popover","true");var id=e.getAttribute("href");if(id){var fn=document.querySelector(id);if(fn){var c=fn.cloneNode(true);var br=c.querySelector("[data-footnote-backref]");if(br)br.remove();e.setAttribute("title",c.textContent.trim())}}});document.querySelectorAll('[data-footnote-backref]').forEach(function(e){e.setAttribute("data-no-popover","true")})})()</script>"""

def run():
    base = public_dir()

    # Rename sr-only heading to visible Chinese heading
    patched = 0
    for path, html in walk_html(base):
        if '<h2 class="sr-only" id="footnote-label">Footnotes' in html:
            html = html.replace(
                '<h2 class="sr-only" id="footnote-label">Footnotes',
                '<h2 id="参考资料与注释">参考资料与注释'
            )
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            patched += 1
    print(f"  Footnotes heading renamed on {patched} pages")

    # Inject hover/fix script
    injected = 0
    for path, html in walk_html(base):
        if FOOTNOTE_FIX_JS in html:
            continue
        if "</body>" in html:
            html = html.replace("</body>", FOOTNOTE_FIX_JS + "\n</body>")
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            injected += 1
    print(f"  Footnote fix injected into {injected} pages")

    # Add TOC entry
    toc_entry = '<li class="depth-0"><a href="#参考资料与注释" data-for="参考资料与注释">参考资料与注释</a></li>'
    toc_patched = 0
    for path, html in walk_html(base):
        if toc_entry in html:
            continue
        if '<li class="overflow-end">' in html:
            html = html.replace(
                '<li class="overflow-end">',
                toc_entry + '\n<li class="overflow-end">'
            )
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            toc_patched += 1
    print(f"  TOC entry added to {toc_patched} pages")

if __name__ == "__main__":
    run()
