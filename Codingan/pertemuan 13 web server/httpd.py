import socket

server_host = "127.0.0.1"
server_port = 8080

#create socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server_socket.bind((server_host,server_port))
server_socket.listen()
print("Listening on host & port : http://%s:%s"%(server_host,server_port))
print("Press ctrl+c to exit")

while True:
    client_connection,client_address = server_socket.accept()
    #Request
    request = client_connection.recv(1024).decode()
    print(request)

    response_line = "HTTP/1.1 200 OK".encode()
    entity_header = "Content-Type : text/html".encode()

    #Baca File HTML
    file = open("beranda.html","r")
    body = file.read().encode()
    file.close()
    enter = "\r\n".encode()

    #response
    response = b"".join([response_line,enter,entity_header,enter,enter,body])
    client_connection.send(response)
    client_connection.close()

#end while  
server_socket.close()

