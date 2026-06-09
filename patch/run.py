#!/usr/bin/env python
"""Run all post-build patches."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from graph_controls import run as patch_graph_controls
from graph_fixes import run as patch_graph_fixes
from footnotes import run as patch_footnotes
from tag_cloud import run as patch_tag_cloud
from redirect import run as patch_redirect

def main():
    print("Post-build patches:")
    patch_graph_controls()
    patch_graph_fixes()
    patch_footnotes()
    patch_tag_cloud()
    patch_redirect()
    print("Done.")

if __name__ == "__main__":
    main()
