# class Parent
class Parent:
    parentAttr = 100
    
    def __init__(self):
        print 'Calling parent constructor'
    
    def parentMethod(self):
        print 'Calling parent method'
    
    def setAttr(self, attr):
        self.parentAttr = attr
    
    def getAttr(self):
        print "Parrent attribute:", Parent.parentAttr
        
# class Child
class Child(Parent):
    def __init__(self):
        print 'Calling child constructor'
        
    def childMethod(self):
        print 'Calling child method'
    
# instantiation
child = Child()
child.childMethod()
child.parentMethod()
child.setAttr(200)
child.getAttr()

# issubclass
print issubclass(Child, Parent)

# isinstance
print isinstance(child, Child)

    

        