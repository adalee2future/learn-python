def exists(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except IOError:
		return False
		
def inputNumber():
	x = input('Pick a number: ')
	if x == 17:
		raise ValueError, '17 is a bas number'
	return x
	
print exists("a.txt")
x = inputNumber()
print "x =", x
print type(x)
