
import time, socket,sys


print("\nSelamat bergabung pada Chatroom\n")
print("Inisialisasi...")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((ip,port))
print(host, "(", ip, ")\n")
name = input(str("masukan Username :"))

s.listen(1)
print("\nMenunggu koneksi masuk...\n")
conn, addr = s.accept()
print("Menerima koneksi dari", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Sudah terkoneksi kedalam chatroom\nKetik [e] untuk keluar dari chatroom\n")
conn.send(name.encode())

while True:
    message = input(str("Me:"))
    if message == "Meninggalkan Chatroom":
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)