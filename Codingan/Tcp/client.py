from email.errors import MessageError
import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 12345

print("Alamat IP Client :", ip)
server_host = input("Masukan Alamat IP Client Lain :")
name = input("Masukan Username :")


socket_server.connect((server_host,sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, "Telah bergabung...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("pesan : ")
    socket_server.send(message.encode())
    