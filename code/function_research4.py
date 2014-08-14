import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    # Find numbers on lines that start with the string "X-" such as
    # X-DSPAM-Confidence: 0.8475
    if re.search('^X\S*: [0-9.]+', line): 
        print line