from http.server import HTTPServer,BaseHTTPRequestHandler

class Myserver(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request Received !")

        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()


        self.wfile.write(b"Hello chaitu , happy backend learning ! ")

server = HTTPServer(("localhost",8000),Myserver)

print("Server started at http://localhost:8000")

server.serve_forever()