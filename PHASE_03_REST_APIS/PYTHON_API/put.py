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
        "name" : "phone",
        "price" : 25000
    }
]
class myserver(BaseHTTPRequestHandler):

    def do_PUT(self):

        # get product id from the url

        parts = self.path.split("/products")

        product_id = int(parts[2])

        # Read the request body

        length = int(self.headers["Content-Length"])

        data = self.rfile.read(length)


        #convert bytes to string

        data = data.decode()

        #convert JSON String to python dictionary

        data = json.loads(data)

        #Find the product

        for i in range(len(products)):

            if products[i]["id"] == product_id:

                products[i] ={

                    "id" : product_id,
                    "name" : data["name"],
                    "price" : data["price"]
                }

                self.send_response(200)
                self.send_header("Content-Type","application/json")
                self.end_headers()

                self.wfile.write(
                    json.dumps(products[id].encode())
                )

                return


            # product not found

            self.send_response(404)
            self.send_header("Content-Type","application/json")
            self.end_header()

            self.wfile.write(
                json.dumps({
                    "error" : "product not found"
                }).encode()
            )


server = HTTPServer(("localhost",8000),myserver)

print("Server running on port 8000")

server.serve_forever()