import Image
import time


img = Image.open("LARGE_elevation.jpg")

start = time.time()

img = img.convert('RGBA')
r, g, b, alpha = img.split()
img = Image.merge( "RGBA", (g, r, b, alpha))
hist = img.histogram()

print time.time()-start

img.save('colorSwapped.jpg')
print hist

