import socket

server=socket.socket()
ip="192.168.11.64"
port = 2222
server.connect((ip,port))
c=(server.recv(100))
print(c.decode())
while(True):
    a=input()
    b=str.encode(a)
    server.send(b)