import socket




surrogateAddress = '0.0.0.0'
surrogatePort = '9998'

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

        if fileName[:3] == 'GET':
            send(address, 9999, fileName, False)
        else:
            print("Receiving " + fileName)
            f = open(fileName, "rb")
            l = sc.recv(1024)
            while l:
                f.write(l)
                l = f.recv(1024)
            sc.close()
            f.close()

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

    f = open(filename, 'rb')

    l = f.read(1024)
    while l:
        l = f.read(1024)
        s.send(l)


def request(host, port, filename):
    s = socket.socket()
    s.connect((host, port))
    s.send("GET " + filename)





