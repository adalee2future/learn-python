def f():
    print "this is f"
    
def g():
    print "Wow, i am g"
    
dd = {1: f, 2: g}

dd[1]()
dd[2]()
print dd[1]
print dd[2]