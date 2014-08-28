filename = raw_input('Enter the file name: ')
try:
    fhand = open(filename)
except:
    print 'File cannot be opened:', filename
    exit()