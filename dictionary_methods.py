student = {'Name': 'Zara', 'Age': 7};

# clear 
print student
student.clear()
print student

student = {'Name': 'Zara', 'Age': 7};

# copy
student1 = student
print student1
print id(student), id(student1)
student2 = student.copy()
print student2
print id(student), id(student2)

# fromkeys
properties = ('name', 'age', 'sex')
person = dict.fromkeys(properties)
print person
person = dict.fromkeys(properties, 'unknown')
print person

# get
print student.get('Name')

# has_key
print student.has_key('Age')
print student.has_key('Major')

# items
print student.items()

# keys
print student.keys()

# values
print student.values()

# update
sex_property = {'Sex': 'female'}
student.update(sex_property)
print student
