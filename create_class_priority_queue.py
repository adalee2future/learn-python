class Node:
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next
	def __str__(self):
		return str(self.cargo)
		
class Queue:
	def __init__(self):
		self.length = 0
		self.head = None
		self.last = None
		
	def isEmpty(self):
		return self.length == 0
		
	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.head == None:
			self.head = node
		else:
			last = self.last
			last.next = node
			self.last = node
		self.length = self.length + 1
	
	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length = self.length - 1
		if self.length == 0:
			self.last = None
		return cargo

class PriorityQueue:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def insert(self, item):
		self.items.append(item)
		
	def remove(self):
		if len(self.items) == []:
			return
		maxi = 0
		for i in range(1, len(self.items)):
			if self.items[i] > self.items[maxi]:
				maxi = i
		item = self.items[maxi]
		self.items[maxi: maxi + 1] = []
		return item

class Golfer:
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def __str__(self):
		return "%-16s: %d" % (self.name, self.score)
		
	def __cmp__(self, other):
		if self.score < other.score: return 1  # less is more
		if self.score > other.score: return -1
		return 0
		
q = PriorityQueue()
q.insert(11)
q.insert(12)
q.insert(14)
q.insert(13)
while not q.isEmpty(): print q.remove()

tiger = Golfer("tiget Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)
while not pq.isEmpty(): print pq.remove()		
	
	