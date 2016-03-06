import socket
from threading import Thread
import time
import os

serverList = ['planetlab2.tsuniv.edu', 'pl2.rcc.uottawa.ca', 'planetlab1.cs.colorado.edu']
PORT = 9999
FLAG = False

results = {}

for server in serverList:
    results[server] = []


script = """
#

import os

os.system('sudo yum -q install -y -q tesseract')
os.system('tesseract testFile.bmp output')
os.system('sudo yum -q remove -y -q tesseract')
"""

script2 = """
#

import os

os.system('sudo apt-get -q install -y -q 10 tesseract-ocr')
os.system('tesseract testFile.bmp output2')
os.system('sudo apt-get -q remove -y -q 10 tesseract-ocr')
"""



def downloadFile(server, port, file):
    global FLAG
    global start
    try:
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
        results[server].append(str(time.time()-start))
        if not FLAG:
            FLAG = True
            print server
            f = open('testFile.txt', 'wb')  # open in binary
            f.write(buffer)
            f.close()

        s.close()
    except:
        print "Could not establish connection with " + server

for i in range(0,10):
    start = time.time()
    threadArray = {}
    print "Image OCR Test\n"
    start = time.time()
    for server in serverList:
        threadArray[server] = Thread(target=downloadFile, args=(server, PORT, script))
        threadArray[server].start()
    for server in serverList:
        threadArray[server].join()


#for i in range(0,10):
#    threadArray = {}
#    FLAG = False
#    start = time.time()
#    print "\nImage Transfer Test"
#    for server in serverList:
#        threadArray[server] = Thread(target=downloadFile, args=(server, PORT, "testFile.bmp"))
#        threadArray[server].start()
#    print threadArray
#    for server in serverList:
#        threadArray[server].join()


for server in results:
    print '\n' + server
    for time in results[server]:
        print time

#results = []

#for i in range(0,20):
#    start = time.time()
#    exec(script2)
#    finish = time.time() - start
#    results.append(finish)

#for result in results:
#    print result

