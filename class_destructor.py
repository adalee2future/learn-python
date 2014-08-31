class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    # destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, 'destroyed' 

# instantiation
p = Point()
del p      # would print 'Point destroyed'

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1) == id(pt2) == id(pt3) # True 
del pt1
del pt2
del pt3    # would print 'Point destroyed'
