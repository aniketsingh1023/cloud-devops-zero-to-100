"""Exercise the HTTP behavior readers rely on for the failure/recovery drill."""
import contextlib
import importlib.util
import json
import os
from pathlib import Path
import threading
import unittest
from unittest.mock import patch
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

spec = importlib.util.spec_from_file_location('learning_lab', Path(__file__).with_name('app.py'))
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class ServiceBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), app.Handler)
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def fetch(self, path):
        try:
            response = urllib.request.urlopen(self.base + path, timeout=5)
        except urllib.error.HTTPError as error:
            response = error
        with contextlib.closing(response):
            self.assertIn('application/json', response.headers['Content-Type'])
            return response.status, json.load(response)

    def test_healthy_service_and_unknown_route(self):
        with patch.dict(os.environ, {'FAIL_MODE': '0'}):
            self.assertEqual(self.fetch('/')[0], 200)
            self.assertEqual(self.fetch('/readyz'), (200, {'ready': True}))
            self.assertEqual(self.fetch('/missing'), (404, {'error': 'not found'}))

    def test_failure_preserves_liveness_and_recovery_restores_readiness(self):
        with patch.dict(os.environ, {'FAIL_MODE': '1'}):
            self.assertEqual(self.fetch('/')[0], 503)
            self.assertEqual(self.fetch('/readyz'), (503, {'ready': False}))
            self.assertEqual(self.fetch('/healthz'), (200, {'alive': True}))
        with patch.dict(os.environ, {'FAIL_MODE': '0'}):
            self.assertEqual(self.fetch('/readyz'), (200, {'ready': True}))


if __name__ == '__main__':
    unittest.main()
