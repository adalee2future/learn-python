class Time:
	pass

def printTime(time):
	print time.hours, ":", time.minutes, ":", time.seconds
	
# This is called a pure function because
# it does not modify any of the objects passed to it
# as arguments and it has no side effects, such as
# displaying a value or getting user input.
def addTime(t1, t2):
	sum = Time()
	sum.hours = t1.hours + t2.hours
	sum.minutes = t1.minutes + t2.minutes
	sum.seconds = t1.seconds + t2.seconds
	return sum

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30

breadTime = Time()
breadTime.hours = 3
breadTime.minutes = 35
breadTime.seconds = 0

doneTime = addTime(currentTime, breadTime)
printTime(doneTime)

def convertToSeconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

def makeTime(seconds):
	time = Time()
	time.hours = seconds // 3600
	time.minutes = (seconds % 3600) // 60
	time.seconds = seconds % 60
	return time
	
print convertToSeconds(doneTime)
printTime(makeTime(5678))
	

	
