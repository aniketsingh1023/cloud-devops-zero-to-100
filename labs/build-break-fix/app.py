"""A deliberately tiny HTTP service for local learning, not production hosting."""
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        started = time.monotonic()
        path = urlsplit(self.path).path
        failing = os.environ.get('FAIL_MODE', '0') == '1'
        if path == '/healthz':
            status, payload = 200, {'alive': True}
        elif path == '/readyz':
            status = 503 if failing else 200
            payload = {'ready': not failing}
        elif path == '/':
            status = 503 if failing else 200
            payload = {'message': 'simulated dependency unavailable' if failing else 'Build. Break. Fix. Explain.'}
        else:
            status, payload = 404, {'error': 'not found'}
        body = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        print(json.dumps({'event': 'request', 'method': 'GET', 'path': path,
                          'status': status, 'duration_ms': round((time.monotonic() - started) * 1000, 3)}), flush=True)

    def log_message(self, format, *args):
        # The structured request log above avoids a second unstructured log entry.
        pass


if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '8080'))
    server = ThreadingHTTPServer((host, port), Handler)
    print(json.dumps({'event': 'started', 'host': host, 'port': port}), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
