import os
from time import sleep

while True:
    sleep(0.001)
    for root, dirs, files in os.walk(os.getcwd() + '/files'):
        for file in files:
            if file.endswith('.py'):
                exec file