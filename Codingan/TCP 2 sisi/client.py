
import time,socket,sys

print("\nSelamat bergabung pada Chatroom\n")
print("Inisialisasi...")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Masukan alamat IP server: "))
name = input(str("\nMasukan Username:"))
port = 1234
print("\nMencoba terkoneksi pada", host, "(", port, ")\n")
time.sleep(1)
s.connect((host,port))
print("Tersambung...")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "Telah bergabung pada Chatroom\nKetikan [e] untuk keluar dari chatroom\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me:"))
    if message == "[e]":
        message = "Meninggalkan Chatroom!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())