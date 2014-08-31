# class Employee
class Employee:
    'Common base class for all employees' 
    empCount = 0
    
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary 
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        
    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

# instantiation        
emp1 = Employee('Ada', 3400)
emp2 = Employee('Zara', 2000)

# remove or modify attributes
emp1.age = 23
del emp1.age

# hasattr
print hasattr(emp1, 'age')

# setattr
setattr(emp1, 'age', 23)

# getattr
try:
    print getattr(emp1, 'age')
except:
    print "emp1 has not attribute of age. You can add if you want."
    
try:
    print getattr(emp1, 'age')
except:
    print "emp2 has not attribute of age. You can add if you want."

# delattr
try:
    delattr(emp1, 'age')
    print "Attribute age deleted successfully."
except:
    print "You can not delete age since emp1 has not attribute age."
    
try:
    print emp1.age
except:
    print "emp1 has not age attribute"




