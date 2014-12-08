L = [1, 2, 3]
it = iter(L)
print it
print it.next()
print it.next()
print it.next()
try:
	print it.next()
except:
	print "end iteration"
	
for i in iter(L):
	print i
