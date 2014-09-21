'''
Calculator logic

    Data
        Store
        Operand
    
    Operations
        Print
        Swap
        Add
        Subtract
        Multiple
        Divide
        
    Basic calculator computation
    
    Store = store operation operand
'''

# start point for calculator
import simplegui

# initialize globals
store = 12
operand = 3

# define functions that manipulate store and operand
def output():
    '''prints contens of store and operand'''
    print "Store =", store
    print "Operand =", operand
    print
    
def swap():
    '''swap contents of store and operand'''
    global store, operand
    store, operand = operand, store
    output()

'''
Calculator logic

    Data
        Store
        Operand
    
    Operations
        Print
        Swap
        Add
        Subtract
        Multiple
        Divide
        
    Basic calculator computation
    
    Store = store operation operand
'''

# start point for calculator
import simplegui

# initialize globals
store = 0
operand = 0

# define functions that manipulate store and operand
def output():
    '''prints contens of store and operand'''
    print "Store =", store
    print "Operand =", operand
    print
    
def swap():
    '''swap contents of store and operand'''
    global store, operand
    store, operand = operand, store
    output()

def add():
    '''add operand to store'''
    global store, operand
    store += operand
    output()
    
def sub():
    '''subtract operand from store'''
    global store, operand
    store -= operand
    output()

def mult():
    '''multiply store by operand'''
    global store, operand
    store *= operand
    output()
       
def div():
    '''divide store by operand'''
    global store, operand
    try:
        store /= operand
    except:
        print "fail to divide!"
    output()

def enter(inp):
    global operand
    operand = float(inp)
    output()

# Create a frame
frame = simplegui.create_frame("Calculator", 300, 300)

# Register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button('Div', div, 100)
frame.add_input('Enter operand', enter, 100)

# Start frame   
frame.start()