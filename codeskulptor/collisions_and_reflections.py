import simplegui

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0, 5.0 / 60.0]

    
def draw(canvas):
    # update ball position
    # calculate ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off left hand aside of canvas
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] > WIDTH - BALL_RADIUS:
        vel[0] = -vel[0]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        vel[1] = -vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
        
# crate frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()

