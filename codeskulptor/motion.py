'''
motion
    car 25mph   velocity
    0:  0
    1:  25 miles
    2:  50 miles
    .
    .
    .
'''

import simplegui

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [5, 3]
time = 0

# define event handlers
def tick():
    global time
    time += 1
    
def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]
    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
        
# crate frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()