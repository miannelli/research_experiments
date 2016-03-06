import socket
import sys
s = socket.socket()
s.bind(("0.0.0.0",9999))
s.listen(10)


while True:
    sc, address = s.accept()
    print address

    fileName = sc.recv(100)
    print fileName

    f = open(fileName, "rb")
    l = f.read(1024)
    while l:
        sc.send(l)
        l = f.read(1024)

    sc.close()

s.close()