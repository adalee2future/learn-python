import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # match lines that start with the string "From:"
        print line