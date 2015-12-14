from socketserver import (
    StreamRequestHandler,
    TCPServer,
)
from json import dumps, loads

class AddHandler(StreamRequestHandler):
    def handle(self):
        self.data = loads(self.rfile.readline().decode())
        self.wfile.write(dumps(
            sum(self.data)
        ).encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = TCPServer((HOST, PORT), AddHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
