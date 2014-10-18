# Simple task list

import simplegui

tasks = []

# Handler for button
def clear():
    tasks = []

# Handler for new task    
def new(task):
    tasks.append(task)
    
# Handler for removing number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n - 1)

# Handler for removing name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)

# Handler to draw on canvas
def draw(canvas):
    pass
        

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_num, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
    
