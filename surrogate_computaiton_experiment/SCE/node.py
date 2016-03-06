import socket




surrogateAddress = '0.0.0.0'
surrogatePort = 9998

def receiver(port, isSurrogate):
    DEFAULT_PORT = 9999
    s = socket.socket()
    try:
        s.bind(("0.0.0.0",port))
    except:
        s.bind(("0.0.0.0",DEFAULT_PORT))
    s.listen(10)

    while True:
        sc, address = s.accept()
        print(address)
        fileName = sc.recv(100)
        sc.close()
        sc, address = s.accept()

        if fileName[:3] == 'GET':
            try:
                send(address, 9999, fileName, False)
            except:
                print("Error 1")
        else:
            print("Receiving " + fileName)
            try:
                f = open(fileName, "wb")
                print "file opened"
            except:
                print fileName + " not opened"


            try:
                l = sc.recv(1024)
                print l
                print "first bytes received"
            except:
                pass

            while l:
                f.write(l)
                print "writing file"
                l = sc.recv(1024)
            sc.close()
            f.close()
            print "file closed"

            if fileName[-2:] == "py":
                if isSurrogate:
                    try:
                        exec(fileName)
                        send(address, port, 'output.txt', False)
                    except:
                        print("Could not execute surrogate file")
                else:
                    send(surrogateAddress, surrogatePort, fileName)

    s.close()

def send(host, port, filename):
    s = socket.socket()
    s.connect((host, port))
    s.send(filename)
    s.close()

    s = socket.socket()
    s.connect((host, port))
    s.send(filename)
    f = open(filename, 'rb')

    f.seek(0)
    l = f.read(1024)
    while l:
        l = f.read(1024)
        s.send(l)
    s.close()


def request(host, port, filename):


    s.send("GET " + filename)





