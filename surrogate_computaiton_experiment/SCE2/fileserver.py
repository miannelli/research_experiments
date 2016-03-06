import socket
import sys
s = socket.socket()
s.bind(("0.0.0.0",9999))
s.listen(10)


while True:
    sc, address = s.accept()
    print address


    fileCommand = sc.recv(1024)
    if fileCommand[1] == '#':
        exec(fileCommand)
        f = open('output.txt', "rb")
        l = f.read(1024)
        while l:
            sc.send(l)
            l = f.read(1024)
    else:
        f = open('testFile.bmp', "rb")
        l = f.read(1024)
        while l:
            sc.send(l)
            l = f.read(1024)

    sc.close()

s.close()
