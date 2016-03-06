from ftplib import FTP
 
ftp = FTP()   # connect to host, default port

ftp.connect('pl2.rcc.uottawa.ca', port=9997)

ftp.sendcmd('USER anonymous')
ftp.sendcmd('PASS ')
ftp.login()

#FTP.retrbinary(command, callback[, maxblocksize[, rest]])




def callback(data):
    print data

ftp.retrbinary('RETR treadmill-desk.jpg', callback)