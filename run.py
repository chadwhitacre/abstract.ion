#!/usr/bin/env python
# -*- coding: utf-8 -*-
from http import server


class Handler(server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith('/n'):
            return 'text/html'
        else:
            return server.SimpleHTTPRequestHandler.guess_type(self, path)


server.HTTPServer(('', 8000), Handler).serve_forever()
