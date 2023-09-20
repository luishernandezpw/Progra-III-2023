from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import crud_alumnos
import json

crud_alumnos = crud_alumnos.crud_alumnos()
port = 3000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path=="/alumnos":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(crud_alumnos.consultar_alumnos()).encode('utf-8'))
            
    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos= self.rfile.read(longitud)
        datos = datos.decode()
        datos = parse.unquote(datos)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(datos.encode())
        
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()