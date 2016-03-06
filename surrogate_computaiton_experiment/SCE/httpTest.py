import httplib

images = ['img1.png', 'img2.png', 'img3.png']

conn = httplib.HTTPConnection('pl2.rcc.uottawa.ca', 9997)

for image in images:
    conn.request('GET', 'testtext.txt')
    resp = conn.getresponse()
    data = resp.read()
    with open('textfortest', 'wb') as f:
        f.write(data)

conn.close()