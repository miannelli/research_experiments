import node
from threading import Thread

cloudServer = Thread(target = node.receiver, args = (9999, False,))
#cloudServer.start()

server = 'pl2.rcc.uottawa.ca'

#node.send(server, 9999, 'testFile.bmp')
#node.send(server, 9999, 'treadmill-desk.jpg')
node.send(server, 9999, 'testtext.txt')
#node.send(server, 9999, 'surrogateFile.py')
#node.request(server, 9999, 'output.txt')
