import os
from ftplib import FTP
from time import sleep

IS_SURROGATE = True

SURROGATE_PORT = '9999'
SURROGATE_HOST = 'localhost'

if not IS_SURROGATE:

    ftp = FTP()   # connect to host, default port
    ftp.connect(SURROGATE_HOST, port=SURROGATE_PORT)
    ftp.sendcmd('USER anonymous')
    ftp.sendcmd('PASS ')
    ftp.login()
    while True:
        sleep(0.001)
        for root, dirs, files in os.walk(os.getcwd() + '/files'):
            for file in files:
                if file.endswith('.py'):
                    script = open(file)
                    fileName = script.readline()[1:]
                    ftp.storbinary('STOR fileName')
                    ftp.storbinary('STOR file')
else:
    while True:
        sleep(0.001)
        for root, dirs, files in os.walk(os.getcwd() + '/files'):
            for file in files:
                if file.endswith('.py'):
                    exec file

