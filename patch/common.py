"""Shared utilities for post-build patch scripts."""
import os

def public_dir():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")

def rel_prefix(path, base):
    """Compute depth-corrected relative path prefix (./, ../, ../../, etc.)"""
    rel = os.path.relpath(path, base)
    depth = len(os.path.dirname(rel).split(os.sep)) if os.path.dirname(rel) else 0
    return "./" if depth == 0 else "../" * depth

def walk_html(base):
    """Yield (path, html_content) for every HTML file under base."""
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                yield path, fh.read()
