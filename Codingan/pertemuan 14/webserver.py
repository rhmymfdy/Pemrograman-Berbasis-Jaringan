import socket
import os
import mimetypes
from template import Template

#from htdocs import proses login

def tcp_server():
    server_host = '127.0.0.1'
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind((server_host,server_port))
    server_socket.listen()
    print('Listen on http://127.0.0.1:8080')
    while True:
        client_connection, client_address = server_socket.accept()
        #Request
        request = client_connection.recv(1024).decode()
        print('Request : %s'%(request))
        #handle request
        if(request and request.strip()):
            respone = handle_request(request)
            #respone
            client_connection.sendall(respone)
        client_connection.close()
    server_socket.close()

def handle_request(request):
    request_massage = str(request).split('\r\n')
    request_line = request_massage[0]
    words = request_line.split()
    method = words[0]
    uri = words[1].strip('/')

    http_version = words[2]
    if(uri == ''):
        uri = 'index.html'
    if method == 'GET':
        respone = handle_get(uri,http_version)
    if method == 'POST':
        data = request_massage[len(request_massage)-1]
        respone = handle_post(uri,http_version,data)
    return respone

def handle_get(uri,http_version):
    uri = 'htdocs/%s'%(uri)
    if os.path.exists(uri) and not os.path.isdir(uri):
        respone_line = b''.join([http_version.encode(),b'200', b'OK'])
        content_type = mimetypes.guess_type(uri)[0] or 'text/html'
        entity_header = b''.join([b'Content-type :', content_type.encode()])
        file = open(uri, 'rb')
        massage_body = file.read()
        file.close()
    else:
        respone_line = b''.join([http_version.encode(), b'404', b'Not Found'])
        entity_header = b'Content-Type : text/html'
        massage_body = b'<h1> 404 Not Found </h1>'
    crlf = b'\r\n'
    respone = b''.join([respone_line,crlf,entity_header,crlf,crlf,massage_body])
    #print(respone)
    return respone

def handle_post(uri,http_version,data):
    uri = 'htdocs/%s'%(uri)
    if os.path.exists(uri) and not os.path.isdir(uri):
        respone_line = b''.join([http_version.encode(),b'200', b'OK'])
        content_type = mimetypes.guess_type(uri)[0] or 'text/html'
        entity_header = b''.join([b'Content-type : ', content_type.encode()])

        file = open(uri, 'r')
        html = file.read()
        file.close()

        _post = {}
        for i in data.split('&'):
            x = i.split('=')
            _post[x[0]] = x[1]

        context = {
            '_post' : _post
        }
        t = Template(html)
        massage_body = t.render(context).encode()
    
    else:
        respone_line = b''.join([http_version.encode(), b'404', b'Not Found'])
        entity_header = b'Content-Type : text/html'
        massage_body = b'<h1> 404 Not Found </h1>'
    crlf = b'\r\n'
    respone = b''.join([respone_line,crlf,entity_header,crlf,crlf,massage_body])
    #print(respone)
    return respone

if __name__ == '__main__':
    tcp_server()