import thread
import time

# define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print threadName, time.ctime(time.time())
        
# create two threads
try:
    thread.start_new_thread(print_time, ('Thread-1', 2, ))
    thread.start_new_thread(print_time, ('Thread-2', 4, ))
except:
    print 'Error: unable to start thread'

   