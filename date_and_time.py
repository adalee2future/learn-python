import time; # This is required to include time module.
import calendar

# time
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

# localtime
localtime = time.localtime(ticks)
print localtime

# asctime
print time.asctime(localtime)

# calendar
cal = calendar.month(2014, 8)
print cal

# altzone
print time.altzone

# clock
def sleep3seconds():
    time.sleep(3)

start_time = time.clock()
sleep3seconds()
end_time = time.clock()
print end_time - start_time, 'seconds process time'

start_time = time.time()
sleep3seconds()
end_time = time.time()
print end_time - start_time, 'seconds wall time'

# ctime
# converts a time expressed in seconds since the epoch to a string representing local time
print time.ctime()

# gmtime
print time.gmtime()

# mktime
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
seconds = time.mktime(t)
my_time = time.asctime(time.localtime(seconds))
print my_time

# strftime
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime())

# for more see Python Data & Time in Python Tutorial




