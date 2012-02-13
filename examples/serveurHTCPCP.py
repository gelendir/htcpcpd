import SimpleHTTPServer
import SocketServer

PORT = 8000

class HTTPImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Ceci est une requête GET")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Ceci est une requête POST")

    def do_BREW(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Ceci est une requête BREW")

httpd = SocketServer.TCPServer(("localhost", PORT), HTTPImpl)

print "Disponible sur le port ", PORT
httpd.serve_forever()
