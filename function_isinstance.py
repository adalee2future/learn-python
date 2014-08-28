def factorial(n):
	if not isinstance(n, int):
		print "Factorial is only defined for integers."
		return -1
	elif n < 0:
		print "Factorial is only defined for positive integers."
		return 0
	elif n == 0:
		return 1
	else:
		return n * factorial(n - 1)
		
print factorial(-5)
print factorial(0)
print factorial(10)
print factorial(2.4)
print factorial("Hello")