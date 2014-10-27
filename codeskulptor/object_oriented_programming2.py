width = 600
height = 400

# Ball traits
radius = 20
color = "White"

# math helper function
def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]

class RectangularDomain:
    def __init__(self, width, height):
        pass
    
    # return if bounding circle is inside the domain
    def normal(self, center):
        pass
    
    # return random location
    def random_pos(self, canvas):
        pass
    
class CircularDomain:
    pass
class Ball:
    def __init__(self, radius, color, domain):
        self.radius = radius
        self.color = color
        self.domain = domain
            
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .1, random.random() + .1]
            
    # bounce
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
            
    # update ball position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()
                
    # draw
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1,
                           self.color, self.color)
                               
    # generic update code for ball physics
    def draw(canvas):
        ball.update()
        field.draw(canvas)
        ball.draw(canvas)
    
# field = RectangularDomain(width, height)
field = CircularDomain(width / 2, height / 2)
ball = Ball(radius, color, field)

frame = simplegui.create_frame("Ball physics", width, height)

frame.set_draw_handler(draw)

frame.start()
    
