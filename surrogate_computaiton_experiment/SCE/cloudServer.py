from threading import Thread

import node

try:
    cloudServer = Thread(target = node.receiver, args = (9999, False,))
    cloudServer.start()

    cloudSurrogate = Thread(target = node.receiver, args = (9998, True))
    cloudSurrogate.start()
except:
    pass