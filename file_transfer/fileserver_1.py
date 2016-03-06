import time
import socket
import os

class fileServer:
    def start(self):
        self.isRunning = True

        for filename in os.listdir('images'):
            s = socket.socket()
            s.bind((self.host, self.port))
            s.listen(10)
            sc, address = s.accept()
            file = open('images\\'+filename,'rb')
            l = file.read(1024)
            while l:
                sc.send(l)
                l = file.read(1024)
            file.close()
            print(filename + ' sent.')
            sc.close()
            s.close()
        self.isRunning = False


    def __init__(self, port):
        self.host = "localhost"
        self.port = port
        self.isRunning = False

s = fileServer(9999)
s.start()







