import socket
import sys
s = socket.socket()
s.bind(("0.0.0.0",9999))
s.listen(10)


while True:
    sc, address = s.accept()
    print address

    a = 0
    for i in range(0,5000000):
        a += 1	

    fileName = sc.recv(100)
    print fileName

    f = open(fileName, "rb")
    l = f.read(1024)
    while l:
        sc.send(l)
        l = f.read(1024)

    sc.close()

s.close()
