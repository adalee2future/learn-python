from urllib2 import urlopen

kittens = urlopen('https://d1z850dzhxs7de.cloudfront.net/topics/ml/small-icon.hover.png')

f = open('machine learning.jpg', 'wb')
f.write(kittens.read())
f.close()