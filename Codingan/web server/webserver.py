from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path='./beranda.html'
        elif self.path == '/berita-indonesia':
            self.path = './indonesia.html'

        try:
            file_to_open=open(self.path).read()
            self.send_response(200)
        except:
            file_to_open = "File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))

httpd=HTTPServer(('localhost',8000), Serv)
httpd.serve_forever()
