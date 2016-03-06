import socket
from threading import Threadimp
import time

addressTable = ['localhost', '192.168.0.7']
PORT = 9999



def getFile(address,port,file,id):
    start = time.time() #Try and catch blocks in case connection times out
    s = socket.socket()
    s.connect((address,port))
    f=open(file + '_'+id, "rb")


    s.close()
    print(address + '\t' + time.time()-start)

for address in addressTable:

import test

test.

