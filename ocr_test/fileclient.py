import socket
from threading import Thread
import time
import os

serverList = ['192.168.29.132', '192.168.29.133', '192.168.29.134']
PORT = 9999
FLAG = False



def downloadFile(server, port, file):
    global FLAG
    global start
    s = socket.socket()
    s.connect((server, port))

    l = 1
    while(l):
        s.send(file)
        l = s.recv(1024)
        buffer = ''
        while l:
            buffer += l
            l = s.recv(1024)
    print server + '\t' + str(time.time()-start)
    if not FLAG:
        FLAG = True
        print server
        f = open('testFile.jpg', 'wb')  # open in binary
        f.write(buffer)
        f.close()

    s.close()

start = time.time()
for server in serverList:
    Thread(target=downloadFile, args=(server, PORT, 'knowledge-doubling.jpg')).start()
