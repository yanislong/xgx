#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
from html import escape
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
         yield '<tr><th>{0}</th><td>{1}</td></tr>'.format(
             escape(k), escape(v))
    yield '</table>'

WSGIServer(app).run()
