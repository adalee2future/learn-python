x = set('spam')
y = set('ham')

print 'x & y', x & y   # intersection
print 'x | y', x | y   # union
print 'x - y', x - y   # difference
print 'x ^ y', x ^ y   # symmetric difference

print x.union(y)
print x.intersection(y)
print x.difference(y)
print x.symmetric_difference(y)

# remove duplication
a = [11, 22, 33, 44, 11, 22]
b = set(a)
c = [i for i in b]
print 'c =', c

# add elements to a set
t = set()
t.add(1)  # add one element
print 't =', t
t.update([2, 3]) # add more than one element
print 't =', t

# remove elements from a set
t.remove(3)
print 't =', t

# output length of a set
print len(t)

print 1 in t
print 2 not in t
print 3 not in t

print x.issubset(y)
print x <= y

print x.issuperset(y)
print x >= y

# clear a set
x.clear()
print 'x =', x


