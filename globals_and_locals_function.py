x = 1

def plus(x, y):
	print "globals inside plus function", globals()
	print "------------------------------"
	
	print "locals inside plus function",locals()
	print "----------plus function ends-------------------------"
	return x + y
	
	
print "globals outide plus function", globals()
print "--------------------------------------------"
print plus(8, 9)