class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan:
        else:
            self.animated = animated
            
    def get_center(self):
        return self.center
        
    def get_size(self):
        return self.size
        
    def get_radius(self):
        return self.radius
        
    def get_lifespan(self):
        return self.lifespan
        
    def get_animate(self):
        return self.animated
        

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = infor.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        canvas.draw_circle(self.po, self.radius, 1, "White", "White")
        
    def update(self):
        pass