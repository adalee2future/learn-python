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

# doc
print Employee.__doc__

# name
print Employee.__name__

# module
print Employee.__module__

# bases
print Employee.__bases__

# dict
print Employee.__dict__