import string

print string.lowercase
print string.uppercase
print string.digits
print string.whitespace
def isLower1(ch):
	return ch in string.lowercase
	
def isLower2(ch):
	return 'a' <= ch <= 'z'

