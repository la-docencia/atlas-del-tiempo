"""Servidor de revisión local. Solo escucha en este equipo."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
import webbrowser
root = Path(__file__).resolve().parent / 'dist'
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(root)))
url = 'http://127.0.0.1:' + str(server.server_port)
print('Atlas: ' + url + '\nDeja esta ventana abierta. Para terminar, pulsa Ctrl+C.', flush=True)
threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
