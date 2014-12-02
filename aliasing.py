a = [1, 2, 3]
b = a
c = a[:]
print "b is a?", b is a    # True
print "c is a?", c is a    # False

b[0] = 17
print 'a: ', a