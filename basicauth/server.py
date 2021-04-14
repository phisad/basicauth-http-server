"""
A simple authenticated web server handler
"""
import urllib.parse
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class SimpleHTTPAuthHandler(SimpleHTTPRequestHandler):
    """ Main class to present webpages and authentication. """
    KEY = ''

    def do_HEAD(self):
        """ head method """
        print("send header")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_authhead(self):
        """ do authentication """
        print("send header")
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ Present frontpage with user authentication. """
        auth_header = self.headers.get("Authorization")
        auth_code = None
        if auth_header:
            if auth_header == f"Basic {self.KEY}":
                SimpleHTTPRequestHandler.do_GET(self)
            else:
                self.send_error(code=401, message="not authenticated")
        else:  # try to check query parameter
            split_path = self.path.split("?")
            if len(split_path) > 1:
                query = split_path[1]
                o = urllib.parse.parse_qs(query)
                if "code" in o:
                    auth_code = o["code"][0]
                if auth_code == self.KEY:
                    SimpleHTTPRequestHandler.do_GET(self)
                else:
                    self.send_error(code=401, message="not authenticated")


def serve(https_port=80, start_dir=None, handler_class=SimpleHTTPAuthHandler):
    """ setting up server """
    httpd = TCPServer(("", https_port), handler_class)

    if start_dir:
        print("Changing dir to {cd}".format(cd=start_dir))
        os.chdir(start_dir)

    socket_addr = httpd.socket.getsockname()
    print("Serving HTTP on", socket_addr[0], "port", socket_addr[1], "...")
    httpd.serve_forever()
