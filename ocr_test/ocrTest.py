from pytesser import *
from time import time

for i in range(0,20):
    start = time()
    image = Image.open('testFile.bmp')
    str =  image_to_string(image)
    elapsed = time() - start
    print(elapsed)