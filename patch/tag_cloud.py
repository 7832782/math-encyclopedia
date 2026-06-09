"""Copy tag-cloud.js + D3 and inject into /tags/index.html."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir

def run():
    base = public_dir()

    # Copy tag-cloud.js
    src = os.path.join(os.path.dirname(base), "tag-cloud.js")
    dst = os.path.join(base, "static", "tag-cloud.js")
    if os.path.exists(src):
        with open(src, "r", encoding="utf-8") as f:
            with open(dst, "w", encoding="utf-8") as f2:
                f2.write(f.read())
        print("  tag-cloud.js copied")

    # Inject into /tags/index.html
    tags_page = os.path.join(base, "tags", "index.html")
    if not os.path.exists(tags_page):
        print("  /tags/index.html not found, skipping")
        return

    with open(tags_page, "r", encoding="utf-8") as f:
        html = f.read()

    cloud_html = '<div class="tag-cloud-container"></div><script src="../static/graph/d3.min.js"></script><script src="../static/tag-cloud.js"></script>'
    if "tag-cloud-container" not in html:
        html = html.replace("<article", cloud_html + "\n<article", 1)
        with open(tags_page, "w", encoding="utf-8") as f:
            f.write(html)
        print("  Tag cloud injected into /tags/index.html")
    else:
        print("  Tag cloud already in /tags/index.html")

if __name__ == "__main__":
    run()
