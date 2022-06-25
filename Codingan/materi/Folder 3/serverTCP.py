import socket
import threading

server=socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
port = 2222
ip="" 
server.bind((ip,port))
server.listen()

def ad(session, addr):
    print(addr)
    session.send("Server connected".encode())
    while True:
         data=session.recv(100)
         print(addr[0]+":"+data.decode())
while True:
        session , addr = server.accept()
        t = threading.Thread(target=ad, args=(session,addr))
        t.start()