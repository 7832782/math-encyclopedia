"""Patch graph script: Fu() decodeURIComponent + fix /static/graph/ paths."""
import os, sys, glob
sys.path.insert(0, os.path.dirname(__file__))
from common import public_dir

def run():
    base = public_dir()
    for script_path in glob.glob(os.path.join(base, "static/scripts/script-4-*.js")):
        with open(script_path, "r", encoding="utf-8") as f:
            jscode = f.read()
        name = os.path.basename(script_path)

        # Patch Fu() to decode URI-encoded slugs
        old_fn = 'function Fu(u){let e=_t(ft(u,"index"),!0);return e.length===0?"/":e}'
        new_fn = 'function Fu(u){try{u=decodeURIComponent(u)}catch(e){}let e=_t(ft(u,"index"),!0);return e.length===0?"/":e}'
        if old_fn in jscode:
            jscode = jscode.replace(old_fn, new_fn)
            print(f"  Patched Fu() in {name}")
        else:
            import re
            match = re.search(r'function Fu\([a-z]\)\{let [a-z]=_t\(ft\([a-z],"index"\),!\d\);return [a-z]\.length===\d\?"/":[a-z]', jscode)
            if match:
                jscode = jscode[:match.start()] + new_fn + jscode[match.end():]
                print(f"  Patched Fu() in {name} (regex match)")

        # Fix hardcoded /static/graph/ paths
        jscode = jscode.replace('"/static/graph/d3.min.js"', '"../graph/d3.min.js"')
        jscode = jscode.replace('"/static/graph/pixi.js"', '"../graph/pixi.js"')

        with open(script_path, "w", encoding="utf-8") as f:
            f.write(jscode)
        print(f"  Fixed /static/graph/ paths in {name}")

if __name__ == "__main__":
    run()
