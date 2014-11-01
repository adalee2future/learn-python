'''
Sprite and sprite sheets
    Two dimensional image animation integrated into a larger scene, usually treated as a graphical overlay
    
    In 1970/1980's, doing 2D graphics was computationally expensive. Sprite were 2D images provided to
    special hardware accelerators that overlaid the images onto the display.
    
    Now, sprite are logical entities used to organize/represent images that add visual complexity to a game
    
    Sprite sheets consisted a collection of sprites organized as a single image. Note that the individual sprites
    need not be regularly spaced on the sprite sheet.
    
    We will prefer to load sprites as individual images to provide more flexibility in modifying the art assets 
    for Spaceship and RiceRocks. 
'''
'''
Color and transparency
    Color - up to now, "White", "Black", "Red"
        RGB model - three red, green, blue channels
        Stored channel values as numerical intensities in the range 0-255
        HTML string - "rgb(255, 0, 0)" - equivalent to "Red"
        http://www.w3schools.com/html/html_colors.asp
        
    Challenge - would lie to draw irregular shapes (like an asteroid or spaceship)
    that like in rectangular images
    
    Transparency - up to now, always opaque
        Add alpha channel to RGB model - channel stores transparency
        HTML string - "rgba(255, 0, 0, 0.5)" - (1 is opaque, 0 is transparent)
        
        Create image with transparent alpha channel in photoshop, GIMP, paint.net, etc.
        RGN image format is popular choice
'''

# Sprite class demo
import simplegui
import math

# helper class to organize image information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
            
    def get_center(self):
        return self.center
        
    def get_size(self):
        return self.size
        
    def get_radius(self):
        return self.radius
        
    def get_lifespan(self):
        return self.lifespan
        
    def get_animated(self):
        return self.animated
        
# load ship image
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# Sprite class
class Sprite():
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
def draw(canvas):
    
    # draw ship and sprites
    a_rock.draw(canvas)
    
    # update ship and sprites
    a_rock.update()
    
# initialize frame
frame = simplegui.create_frame("Sprite demo", 800, 600)

# initialize ship and two sprites
a_rock = Sprite([400, 300], [0.3, 0.4], 0, 0.1, asteroid_image, asteroid_info)

# register handlers
frame.set_draw_handler(draw)

# get things rolling
frame.start()