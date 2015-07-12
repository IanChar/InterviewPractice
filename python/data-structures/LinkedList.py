import random
class Node:
	def __init__(self, data, prev = None, nxt = None):
		self.data = data
		self.prev = prev
		self.nxt = nxt

	def get_next(self):
		return self.nxt

	def get_prev(self):
		return self.prev

	def get_data(self):
		return self.data

	def set_next(self, node):
		self.nxt = node

	def set_prev(self, node):
		self.prev = node

	def set_data(self, data):
		self.data = data

	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self, firstData = 0):
		self.root = None
		self.end = self.root
		self.size = 0

	def addNode(self, data):
		if self .size == 0:
			self.root = Node(data)
			self.end = self.root
		else:
			self.end.nxt = Node(data, prev = self.end)
			self.end = self.end.nxt
		self.size += 1

	def removeAtPosn(self, posn):
		if posn == 0 and self.size == 1:
			self.root = None
			self.end = None
			self.size -= 1
			return True
		if posn >= self.size:
			print "Position out of bounds."
			return False
		if posn == 0:
			self.root = self.root.nxt
			self.root.prev = None
			self.size -= 1
			return True
		if posn == self.size - 1:
			self.end = self.end.prev
			self.end.nxt = None
			self.size -= 1
			return True
		tempNode = self.root
		for i in range(posn):
			tempNode = tempNode.nxt
		tempNode.prev.nxt = tempNode.nxt
		tempNode.nxt.prev = tempNode.prev
		self.size -= 1
		return True

	def removeNode(self, data):
		posn = self.findNode(data)
		if posn >= 0:
			self.removeAtPosn(posn)
			return True
		return False

	def findNode(self, data):
		if self.size == 0:
			print "No nodes"
			return
		iterNode = self.root
		posn = None
		for i in range(self.size):
			if iterNode.data == data:
				posn = i
				break
			else:
				iterNode = iterNode.nxt
		if posn >= 0:
			return posn
		else:
			print "Not Found"

	def change_node_data(self, posn, data):
		if posn >= self.size or posn < 0:
			return False
		iterNode = self.root
		for i in range(posn):
			iterNode = iterNode.nxt
		iterNode.data = data
		return True

	def get_head(self):
		return self.root

	def set_head(self, node):
		self.root = node

	def get_tail(self):
		return self.end

	def set_tail(self, node):
		self.end = node

	def __str__(self):
		if self.size == 0:
			return "Empty"
		iterNode = self.root
		finString = str(iterNode.data)
		while iterNode.nxt:
			iterNode = iterNode.nxt
			finString = finString + " " + str(iterNode.data)
		return finString


if __name__ == '__main__':
	lList = LinkedList(random.randint(0,9))
	for i in range(1, 10):
		lList.addNode(random.randint(0,9))
	print lList
	for i in range(10):
		print "\nRemoving " + str(i) + "s..."
		while lList.removeNode(i):
			pass
		print lList
	print lList