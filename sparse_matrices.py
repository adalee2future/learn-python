matrix1 = [ [0, 0, 0, 1, 0],
		   [0, 0, 0, 0, 0],
		   [0, 2, 0, 0, 0],
		   [0, 0, 0, 0, 0],
		   [0, 0, 0, 3, 0] ]
		   
matrix2 = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print matrix2[0, 3]
try:
	print matrix2[1, 3]
except:
	print "Do not have this element"

print matrix2.get((0, 3), 0)
print matrix2.get((1, 3), 0)