# interactive application to convert a float in dollars and cents

import simplegui


        
# define draw handler
def draw(canvas):
    canvas.draw_line((300, 0), (0, 200), 10, "Green")

# define an input field handler
def input_handler(text):
    global value
    value = float(text)

# create frame
frame = simplegui.create_frame("Converter", 200, 300)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()