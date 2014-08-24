import urllib
import time

img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'w')
size = 0

while True:
    # In this example, we read only 100,000 characters at a time
    # and write those characters to the cover.jpg file before
    # retrieving the next 100,000 characters of data from the web
    info = img.read(100000)
    if len(info) < 1:
            break
    time.sleep(0.25)
    size += len(info)
    fhand.write(info)
print size, 'characters copied'
fhand.close()
    