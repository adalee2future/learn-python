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

def printTreePostorder(tree):
	if tree == None: return
	printTreePostorder(tree.left)
	printTreePostorder(tree.right)
	print tree.cargo,
	
def printTreeInorder(tree):
	if tree == None: return
	printTreePostorder(tree.left)
	print tree.cargo,
	printTreePostorder(tree.right)
	
def printTreeIndented(tree, level = 0):
	if tree == None: return
	printTreeIndented(tree.right, level + 1)
	print '  ' * level + str(tree.cargo)
	printTreeIndented(tree.left, level + 1)
	
def getToken(tokenList, expected):
	if tokenList[0] == expected:
		del tokenList[0]
		return True
	else:
		return False
		
def getNumber(tokenList):
	if getToken(tokenList, '('):
		x = getSum(tokenList)
		if not getToken(tokenList, ')'):
			raise ValueError, 'missing parenthesis'
		getToken(tokenList, ')')
		return x
	else:
		x = tokenList[0]
		if not isinstance(x, int): return None
		tokenList[0:1] = []
		return Tree(x)
		
def getProduct(tokenList):
	a = getNumber(tokenList)
	if getToken(tokenList, '*'):
		b = getProduct(tokenList)
		return Tree('*', a, b)
	else:
		return a

def getSum(tokenList):
	a = getProduct(tokenList)
	if getToken(tokenList, '+'):
		b = getSum(tokenList)
		return Tree('+', a, b)
	else:
		return a
		
def animal():
	# start with a singleton
	root = Tree('bird')
	# loop until the user quits
	while True:
		print
		if not yes("Are you thinking of an animal?"):
			break
		# walk the tree
		tree = root
		while tree.getLeft() != None:
			prompt = tree.getCargo() + '?'
			if yes(prompt):
				tree = tree.getRight()
			else:
				tree = tree.getLeft()
		# make a guess
		guess = tree.getCargo()
		prompt = "It is a " + guess + "?"
		if yes(prompt):
			print "I rule!"
			continue
		# get new information
		prompt = "What is the animal's name?"
		animal = raw_input(prompt)
		prompt = "What question would distinguish a %s from a %s"
		question = raw_input(prompt % (animal, guess))
		# add new information to the tree
		tree.setCargo(question)
		prompt = "If the animal were %s the answer would be?"
		if yes(prompt % animal):
			tree.seeLeft(Tree(guess))
			tree.setRight(Tree(animal))
		else:
			tree.setLeft(Tree(animal))
			tree.setRight(Tree(guess))
def yes(ques):
	from string import lower
	ans = lower(raw_input(ques))
	return (ans[0] == 'y')

	
three = Tree('3')
seven = Tree('7')
plus = Tree('+', three, seven)
nine = Tree('9')
star = Tree('*', plus, nine)

printTree(star)
print
printTreePostorder(star)
print
printTreeInorder(star)
print
printTreeIndented(star)

tokenList = [9, '+', 11, 'end']
tree = getProduct(tokenList)
printTreeIndented(tree)
print
tokenList = [9, '*', 11, 'end']
tree = getProduct(tokenList)
printTreeIndented(tree)
print
tokenList = [2, '*', 3, '*', 5, '*', 7, 'end']
tree = getProduct(tokenList)
printTreeIndented(tree)
print
tokenList = [9, '*', 11, '+', 5, '*', 7, 'end']
tree = getSum(tokenList)
printTreeIndented(tree)
print
tokenList = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
tree = getSum(tokenList)
printTreeIndented(tree)





