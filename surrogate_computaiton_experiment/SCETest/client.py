from ftplib import FTP

SERVER_PORT = '9999'
SERVER_HOST = 'pl2.rcc.uottawa.ca'

ftp = FTP()   # connect to host, default port
ftp.connect(SERVER_HOST, port=SERVER_PORT)
ftp.sendcmd('USER anonymous')
ftp.sendcmd('PASS ')
ftp.login()

with open('testFile.bmp', 'rb') as f:
    ftp.storbinary('STOR ' + 'testFile.bmp', f)
with open('surrogate.py', 'rb') as f:
    ftp.storbinary('STOR ' + 'surrogateCode.py', f)

ftp.quit()