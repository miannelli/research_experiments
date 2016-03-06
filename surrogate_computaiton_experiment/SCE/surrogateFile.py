dependencies = ['testFile.bmp']

import os

os.system('sudo yum install -y tesseract')
os.system('tesseract testFile.bmp output')
os.system('sudo yum remove -y tesseract')