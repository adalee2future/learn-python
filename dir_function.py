hello = 'Hello, world'

print type(hello)

hello_dir = dir(hello)
print type(hello_dir)
print hello_dir
print type(hello_dir[0])

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
        
ada = Employee("Ada Lee")
print type(ada)
print dir(ada)

import math
print dir(math)