def hello_counter(name):
	count = [0]  # a bug in python 2, so use [0] instead of 0
	def counter():
		count[0] += 1
		print 'Hello, ' + name + ', ' + str(count[0]) + ' access!'
	return counter