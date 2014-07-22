greeting = 'Hello, world!'

try:
    greeting[0] = 'J'
except:
    print "String is immutable, thus you can not change the value."
    
new_greeting = 'J' + greeting[1:]
print new_greeting