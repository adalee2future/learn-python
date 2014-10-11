import simplegui

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1]

    
def draw(canvas):
    # update ball position
    # calculate ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
        
# crate frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()
