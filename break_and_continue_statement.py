while True:
    line = raw_input('> ')
    if line == 'done':
        break
    if line[0] == '#':
        continue
    print line
print 'done'