#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from datetime import datetime


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print ""
        print "%s - %s\t%s" % (
            datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            self.client_address[0],
            self.headers['user-agent'])
        print "-------------------"*6
        for k, v in query_components.items():
            print "%s\t\t\t%s" % (k.strip(), v)

        return

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    try:
        server = HTTPServer(('0.0.0.0', 8888), MyHandler)
        print(' HTTP Server ON')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C recivido, apagando el servidor')
        server.socket.close()
