t = ('a', 'b', 'c', 'd', 'e')

t1 = ('a', )
s1 = ('a')
print type(t1)
print type(s1)

t = tuple()
print t
t = tuple('lupins')
print t
t = tuple([1,2,3,4,5,6,7])
print t
print t[1]
print t[1:3]

print (0, 1, 2) < (0, 3, 4)