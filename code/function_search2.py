import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line): # match any of the string start with Fxxm
        print line