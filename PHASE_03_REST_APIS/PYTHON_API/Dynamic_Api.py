from http.server import HTTPServer,BaseHTTPRequestHandler
import json

products = [
    {
       "id" : 1,
       "name" : "Laptop",
       "price" : 50000 
     },

     {

        "id" : 2,
        "name" : "Phone",
        "price" : 25000
     }
]


class myserver(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/products":

            data = json.dumps(products)

            self.send_response(200)

            self.send_header("Content-Type","application/json")

            self.end_headers()

            self.wfile.write(data.encode())


        #GET products/1
        #GET products/2
        #Get products/25

        elif self.path.startswith("/products/"):

            parts = self.path.split("/")

            product_id = int(parts[2])

            found = False

            for product in products:

                if product["id"] == product_id : 

                    found = True

                    data = json.dumps(product)

                    self.send_response(200)
                    self.send_header("Content-Type","application/json")

                    self.end_headers()


                    self.wfile.write(data.encode())

                    break

            if not found :

                self.send_response(404)

                self.end_headers()

                self.wfile.write(b"File is not found ")


server = HTTPServer(("localhost",8000),myserver)

print("The server is run on the https://localhost:8000")

server.serve_forever()
