from http.server import HTTPServer,BaseHTTPRequestHandler
import json

products = [
    {"id":1,"name":"Laptap","price":50000},
    {"id":2,"name":"phone","price":25000}
]

class myserver(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/products":

            data = json.dumps(products)

            self.send_response(200)

            self.send_header("Content-Type","application/json")

            self.end_headers()

            self.wfile.write(data.encode())

        else :

            self.send_response(404)

            self.end_headers()


server = HTTPServer(("localhost",8000),myserver)

print("Server running  on http://localhost:8000")


server.serve_forever()


