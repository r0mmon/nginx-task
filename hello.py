# -*- coding: utf-8 -*-
import string
def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    str = (environ['QUERY_STRING'])
    body = string.replace(str, '&', '\n')
    start_response(status, headers )
    return [ body ]
