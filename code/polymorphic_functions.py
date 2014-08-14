class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	# override str
	def __str__(self):
		return '(' + str(self.x) + ',' + str(self.y) + ')'
	# override operator '+'
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	def __mul__(self, other):
		return self.x * other.x + self.y * other.y
	def reverse(self):
		self.x, self.y = self.y, self.x
		
# If all of the operations inside the function
# can be applied to the type,
# the function can be applied to the type.
def multadd(x, y, z):
	return x * y + z

p1 = Point(3, 4)
p2 = Point(5, 7)
print multadd(3, 2, 1)
print multadd(p1, p2, 1)

# If all of the operations inside the function
# can be applied to the type,
# the function can be applied to the type.
def frontAndBack(front):
	import copy
	back = copy.copy(front)
	back.reverse()
	print str(front) + str(back)

frontAndBack([1,2,3,4])
frontAndBack(p1)
