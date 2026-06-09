"""Fix footnotes: hover tooltip, heading rename, TOC entry."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir, walk_html

# Injected script: disable popover on footnote refs, add native tooltip
FOOTNOTE_FIX_JS = """<script>(function(){document.querySelectorAll('[data-footnote-ref]').forEach(function(e){e.setAttribute("data-no-popover","true");var id=e.getAttribute("href");if(id){var fn=document.querySelector(id);if(fn){var c=fn.cloneNode(true);var br=c.querySelector("[data-footnote-backref]");if(br)br.remove();e.setAttribute("title",c.textContent.trim())}}});document.querySelectorAll('[data-footnote-backref]').forEach(function(e){e.setAttribute("data-no-popover","true")})})()</script>"""

# Old script that should be removed (no cloneNode)
OLD_FOOTNOTE_SCRIPT = '<script>(function(){document.querySelectorAll(\'[data-footnote-ref]\').forEach(function(e){e.setAttribute("data-no-popover","true");var id=e.getAttribute("href");if(id){var fn=document.querySelector(id);if(fn)e.setAttribute("title",fn.textContent.trim())}});document.querySelectorAll(\'[data-footnote-backref]\').forEach(function(e){e.setAttribute("data-no-popover","true")})})()</script>'

def run():
    base = public_dir()
    # Step A: Inject footnote hover fix
    injected = 0
    for path, html in walk_html(base):
        if FOOTNOTE_FIX_JS in html:
            continue
        if "</body>" in html:
            html = html.replace("</body>", FOOTNOTE_FIX_JS + "\n</body>")
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            injected += 1
    print(f"  Footnote hover fix injected into {injected} pages")

    # Step B: Rename heading, add TOC entry, clean duplicates
    patched = 0
    for path, html in walk_html(base):
        modified = False
        # Remove old duplicate script
        if OLD_FOOTNOTE_SCRIPT in html:
            html = html.replace(OLD_FOOTNOTE_SCRIPT, '')
            modified = True
        # Rename sr-only heading to visible Chinese heading
        if '<h2 class="sr-only" id="footnote-label">Footnotes' in html:
            html = html.replace(
                '<h2 class="sr-only" id="footnote-label">Footnotes',
                '<h2 id="参考资料与注释">参考资料与注释'
            )
            modified = True
        # Add TOC entry
        toc_entry = '<li class="depth-0"><a href="#参考资料与注释" data-for="参考资料与注释">参考资料与注释</a></li>'
        if toc_entry not in html and '<li class="overflow-end">' in html:
            html = html.replace(
                '<li class="overflow-end">',
                toc_entry + '\n<li class="overflow-end">'
            )
            modified = True
        if modified:
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            patched += 1
    print(f"  Footnotes heading renamed and TOC entry added to {patched} pages")

if __name__ == "__main__":
    run()
