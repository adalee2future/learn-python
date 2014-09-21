# global vs. local examples

# num1 is a global variable

num1 = 1
print "in the global scope num1 =", num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print "in the fun function, num1 =", num1
    print "int the fun function, num2 =", num2
    
fun()

# the scope of global is the whole program, num1 remains defined
print "in the globlal scope now num1 =", num1

# the scope of the variable num2 is fun(), num2 is now undefined
try:
    print num2
except:
    print "num2 is not in this global scope"
    
# why use local variables?
# given a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin
    
print fahren_to_kelvin(0)

num = 4

def fun1():
    global num
    num = 5
    num = 999999
    
def fun2():
    global num
    num = 6
    
print num

fun1()
print "After calling fun1, num =", num

fun2()
print "After calling fun2, num =", num

num1, num2 = 1, 2
def swap():
    global num1, num2
    num1, num2 = num2, num1
    
print num1, num2
swap()
print num1, num2


