from socket import *

s = socket(AF_INET,SOCK_DGRAM)
host ="localhost"
port = 9999
buf =1024
addr = (host,port)

f=open ('images\knowledge-doubling.jpg', "rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print "sending ..."
        data = f.read(buf)
s.close()

