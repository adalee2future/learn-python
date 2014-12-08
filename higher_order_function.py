map(lambda x: x ^ 2, [1, 2, 3, 4, 5])

def speak(topic):
	print "My speech is " + topic
	
def timer(fn):
	from time import time
	def inner(*args, **kwargs):
		t = time()
		fn(*args, **kwargs)
		print "took {time}".format(time = time() - t)
		
	return inner

speaker = timer(speak)
speaker("FP with Python")