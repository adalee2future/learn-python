class Node:
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next
	def __str__(self):
		return str(self.cargo)
		
def printList(node):
	while node:
		print node,
		node = node.next
	print

def printBackward(list):
	if list == None: return
	head = list
	tail = list.next
	printBackward(tail)
	print head,
	
def printBackwardNicely(list):
	print "[",
	printBackward(list)
	print "]"
def removeSecond(list):
	if list == None: return
	first = list
	second = list.next
	if second == None: return
	# make the first node refer to the third
	first.next = second.next
	# separate the second node from the rest of the list
	second.next = None
	return second

node = Node("test")
print node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
printList(node)
printList(node1)
printList(node2)
printList(node3)
printBackward(node1)
print
printBackwardNicely(node1)
printList(node1)
removed = removeSecond(node1)
printList(node1)
print removed

		