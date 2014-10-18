import simplegui
import math

# initialize globals
WIDTH = 450
HEIGHT = 300
ball_list = []
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < BALL_RADIUS:
            remove.append(ball)
            
    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.remove(ball)
    
    

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle(ball, BALL_RADIUS, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()