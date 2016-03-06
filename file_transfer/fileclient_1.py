import socket

s = socket.socket()
s.connect(("localhost",9999))



s.accept()

f = open('imagesReceived\\file.jpg','rb')

l = 1

l = s.recv(1024)
while (l):
    f.write(l)
    l = s.recv(1024)
f.close()



s.close()