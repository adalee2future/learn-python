def find(str, ch, start = 0):
	index = start
	while index < len(str):
		if str[index] == ch:
			return index
		index = index + 1
	return -1
	
apple = "apple"
print find(apple, "p")
print find(apple, "p", 2)
print find(apple, "p", 4)