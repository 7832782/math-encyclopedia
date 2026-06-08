import http.server
import socketserver
import os, socket
from urllib.parse import unquote

PORT = 31415
DIR = os.path.join(os.path.dirname(__file__), "public")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def translate_path(self, path):
        path = super().translate_path(path)
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        elif not path.endswith(".html"):
            html = path + ".html"
            if os.path.exists(html):
                path = html
        return path

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("=" * 50)
print(f"  Serving at http://{local_ip}:{PORT}")
print(f"  Local:  http://localhost:{PORT}")
print("  Ctrl+C to stop")
print("=" * 50)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
