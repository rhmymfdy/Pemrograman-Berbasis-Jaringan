
import socket
import threading

#Choosing Nickname
nickname = input("Masukkan Nickname anda :")

#Connecting To Server 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.99.254",8080))

#Listening to server and Sending Nickname
def receive():
    while True:
        try:
            #Receive Message From Server
            # If "NICK" send Nickname
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            #Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Message To Server
def write():
    while True:
        message = "{} : {}".format(nickname,input("pesan :"))
        client.send(message.encode("ascii"))

#Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()