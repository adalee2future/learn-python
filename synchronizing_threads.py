# import
import threading
import time

# exitFlag
exitFlag = 0

# class myThread
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        print 'Starting', self.name
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        threadLock.release()
        print 'Exiting', self.name
        
        
# print_time
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        
        time.sleep(delay)
        print threadName, time.ctime(time.time())
        counter -= 1
 
# Lock
threadLock = threading.Lock()

threads = []
        
# create new threads
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# start new threads
thread1.start()
thread2.start()

# add thread to list
threads.append(thread1)
threads.append(thread2)

# wait for all threads to complete
for t in threads:
    t.join()


print 'Exiting Main Thread'


















