student = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print student

del student['Class']
print student

student.clear();
print student

del student
try:
    print student
except:
    print 'student has been deleted by Ada.'