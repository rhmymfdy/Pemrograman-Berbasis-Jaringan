import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 12345

new_socket.bind((host_name,port))
print("Binding Berhasil")
print("Alamat IP : ", s_ip)
name = input("masukan Username :")
new_socket.listen(1)

conn, add = new_socket.accept()
print("Menerima Koneksi dari ", add[0])
print("Connection established. Terkoneksi dari : ", add[0])

client = (conn.recv(1024)).decode()
print(client + "Sudah Terhubung")

conn.send(name.encode())
while True :
    message = input("Pesan : ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)