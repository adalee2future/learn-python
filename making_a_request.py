from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
# kittens = urlopen("http://placekitten.com")
kittens = urlopen("https://youtube.com/")
response = kittens.read()
body = response[559:1000]

print body # Add your 'print' statement here!
http://placekitten.com/
