import copy

class Point:
	pass

p1 = Point()
p1.x = 3.4
p1.y = 4.0
# To copy a simple object like a Point,
# which doesn¡¯t contain any embedded objects,
# copy is sufficient. This is called shallow copying.
p2 = copy.copy(p1)
print "id(p1) =", id(p1)
print "id(p2) =", id(p2)

class Rectangle:
	pass
	
rect1 = Rectangle()
rect1.width = 10
rect1.height = 8
rect1.corner = p1

rect2 = rect1
rect3 = copy.copy(rect1)
rect4 = copy.deepcopy(rect1)

print "id(rect1) =", id(rect1)
print "id(rect2) =", id(rect2)
print "id(rect3) =", id(rect3)
print "id(rect4) =", id(rect4)
print "id(rect1.corner) =", id(rect1.corner)
print "id(rect2.corner) =", id(rect2.corner)
print "id(rect3.corner) =", id(rect3.corner)
print "id(rect4.corner) =", id(rect4.corner)




