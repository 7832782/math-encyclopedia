"""Replace 标签索引 page with a redirect to /tags/."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir

def run():
    base = public_dir()
    path = os.path.join(base, "标签索引.html")
    if not os.path.exists(path):
        print("  /标签索引.html not found, skipping")
        return
    html = '<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=./tags/"><title>标签索引</title></head><body><p>正在跳转到 <a href="./tags/">标签索引</a>...</p></body></html>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  /标签索引 now redirects to /tags/")

if __name__ == "__main__":
    run()
