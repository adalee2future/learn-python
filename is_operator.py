a = 'banana'
b = 'banana'
c = 'orange'

print "a is b?", a is b
print "b is c?", b is c

b = 'orange'
print "a is b?", a is b
print "b is c?", b is c

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list2
print "list1 is list2?", list1 is list2
print "list2 is list3?", list2 is list3

