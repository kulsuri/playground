from http.server import BaseHTTPRequestHandler, HTTPServer

class test_HTTP_Server_Request_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello from Python!", "utf8"))
        return

def run():
    httpd = HTTPServer( ('0.0.0.0', 8080), test_HTTP_Server_Request_Handler)
    httpd.serve_forever()

run()
