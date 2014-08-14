# method 1: use iteration
def fibonacci1(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci1(n-1) + fibonacci1(n-2)

# method2: store every previous result into a dictionary
previous = {0: 1, 1: 1}
def fibonacci2(n):
	if previous.has_key(n):
		return previous[n]
	else:
		newValue = fibonacci2(n - 1) + fibonacci2(n-2)
		previous[n] = newValue
		return newValue