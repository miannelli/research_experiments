import socket
from threading import Thread
import time

addressTable = ['localhost', '192.168.0.7']
PORT = 23000

def request(address):
    start = time.time()
    try:
        clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        clisock.connect((address, PORT))
        clisock.send("Hello World")
        print clisock.recv(100)
    except Exception:
        print "Request timed out"

    print(time.time()-start)
    clisock.close()

for address in addressTable:
    Thread(target=request, args=(address,)).start()
