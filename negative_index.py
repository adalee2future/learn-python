fruit = 'orange'

positive_index = range(len(fruit))
negative_index = range(len(fruit) - 1, -1, -1)

print "print positive index of fruit"
for index in positive_index:
    print fruit[index]

print "print negative index of fruit"
for index in negative_index:
    print fruit[index]