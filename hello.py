# -*- coding: utf-8 -*-
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    d = parse_qs(environ['QUERY_STRING'])
    body = ''
    for key, value in d.items():
        print(key, value[0])
        body += key + '=' + value[0] +'\n'
    start_response(status, headers )
    return [ body ]
