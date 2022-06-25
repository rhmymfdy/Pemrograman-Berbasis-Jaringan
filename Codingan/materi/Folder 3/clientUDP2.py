import socket
import threading

import time
myp= socket.SOCK_DGRAM
afn=socket.AF_INET
s=socket.socket(afn,myp)
ip="192.168.11.64"
port=1234
s.bind((ip,port))
def func():
        x=s.recvfrom(1024)
        ip = x[1][0]
        data = x[0].decode()
        print(ip + " : " + data)
        time.sleep(int(data))
        print(ip + " : " + data)

while True:
        t=threading.Thread(target=func)
        t.start()