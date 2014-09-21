'''
Event-driven drawing
    Computer monitor -2D grid of pixels stored in frame buffer
    
    Computers update the monitor based on the frame buffer at rate of 
    around 60-72 times a second - refresh rate
    
    Many applications will register a special function called a "draw
    handler."
    
    In Codeskulptor, register the draw handler using a simpleGUI command.
    CodeSkulptor calls the draw handler at around 60 times per seconds.
    
    Draw handler updates the canvas using a collection of draw commands
    that include draw_text, draw_line, draw_circle
'''

# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!", [100, 100], 40, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Test", 300, 200)

# register draw handler
frame.set_draw_handler(draw)
# start frame
frame.start() 