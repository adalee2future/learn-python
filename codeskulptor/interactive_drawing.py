# interactive application to convert a float in dollars and cents

import simplegui

# define global value
value = 3.12
# Handle single quantity
def convert_units(num, unit):
    result = str(num) + ' ' + unit
    
    if num > 1:
        result += 's'
     
    return result
# convert xx.yy to xx dollars and yy cnets
def convert(val):
    # Split into dillars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))
    
    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    
    # Retruen composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
        
# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [10, 100], 24, "White")

# define an input field handler
def input_handler(text):
    global value
    value = float(text)

# create frame
frame = simplegui.create_frame("Converter", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("enter value", input_handler, 100)

# start frame
frame.start()
