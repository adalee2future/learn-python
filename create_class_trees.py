class Tree:
	def __init__(self, cargo, left = None, right = None):
		self.cargo = cargo
		self.left = left
		self.right = right
	
	def __str__(self):
		return str(self.cargo)
		
def total(tree):
	if tree == None: return 0
	return total(tree.left) + total(tree.right) + tree.cargo

def printTree(tree):
	if tree == None: return
	print tree.cargo,
	printTree(tree.left)
	printTree(tree.right)
	
left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)


	
print left
print right
print tree
print total(tree)
printTree(tree)
