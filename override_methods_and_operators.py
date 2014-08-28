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
	
		
p1 = Point(3, 4)
p2 = Point(5, 7)
print p1 + p2
print p1 * p2