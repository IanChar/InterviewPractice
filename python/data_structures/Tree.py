import random

class Node:
	def __init__(self, data = 0):
		self.data = data
		self.left_node = None
		self.right_node = None
		self.parent = None

	def add_right(self, data):
		if self.right_node == None:
			self.right_node = Node(data)
			return True
		return False
		
	def add_left(self, data):
		if self.left_node == None:
			self.left_node = Node(data)
			return True
		return False

	def set_right(self, node):
		if isinstance(node, Node) or node == None:
			self.right_node = node
			return True
		return False

	def set_left(self, node):
		if isinstance(node, Node) or node == None:
			self.left_node = node
			return True
		return False

	def get_right(self):
		return self.right_node

	def get_left(self):
		return self.left_node

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data
		return True

	def set_parent(self, node):
		self.parent = node

	def get_parent(self):
		return self.parent

	def rotate_left(self):
		root = self.right_node
		if root is None:
			return None
		self.right_node = root.get_left()
		root.set_left(self)
		if self.parent:
			if self.parent.get_left() is self:
				self.parent.set_left(root)
			else:
				self.parent.set_right(root)
		root.set_parent(self.parent)
		self.parent = root
		return root

	def rotate_right(self):
		root = self.left_node
		if root is None:
			return None
		self.left_node = root.get_right()
		root.set_right(self)
		if self.parent:
			if self.parent.get_left() is self:
				self.parent.set_left(root)
			else:
				self.parent.set_right(root)
		root.set_parent(self.parent)
		self.parent = root
		return root	

	def __str__(self):
		return str(self.data)

class BinaryTree:
	def __init__(self, data = None):
		if data is not None:
			self.root = Node(data)
			self.size = 1
		else:
			self.root = None
			self.size = 0

	def get_root(self):
		return self.root

	def get_size(self):
		return self.size

	def add_node(self, data, curr_node = None, curr_level = 0):
		if curr_node == None:
			curr_node = self.root
		next_level = 0
		curr_size = self.size + 1
		while curr_size > 1:
			curr_size = curr_size >> 1
			next_level += 1

		if next_level == 0:
			self.root = Node(data)
			self.size += 1
			return True

		if curr_level + 1 == next_level: 
			if curr_node.get_left() == None:
				curr_node.add_left(data)
				curr_node.get_left().set_parent(curr_node)
				self.size += 1
				return True
			elif curr_node.get_right() == None:
				curr_node.add_right(data)
				curr_node.get_right().set_parent(curr_node)
				self.size += 1
				return True
			else:
				return False
		if curr_node.get_left() != None and curr_level < next_level:
			if self.add_node(data, curr_node = curr_node.get_left(), curr_level = curr_level + 1):
				return True
		if curr_node.get_right() != None and curr_level < next_level:
			if self.add_node(data, curr_node = curr_node.get_right(), curr_level = curr_level + 1):
				return True
		return False

	def find_node(self, data):
		found_parent = self.find_parent(data)
		if found_parent:
			left_node = found_parent.get_left()
			right_node = found_parent.get_right()
			if left_node and left_node.get_data() == data:
				return left_node
			else:
				return right_node
		return None

	def find_parent(self, data, curr_node = None):
		if curr_node == None:
			curr_node = self.root

		left_node = curr_node.get_left()
		right_node = curr_node.get_right()
		if left_node:
			if left_node.get_data() == data:
				return curr_node
		if right_node:
			if right_node.get_data() == data:
				return curr_node
			
		if left_node:
			found_node = self.find_parent(data, left_node)
			if found_node:
				return found_node

		if right_node:
			found_node = self.find_parent(data, right_node)
			if found_node:
				return found_node
		return None

	def get_leftmost(self, curr_node = None):
		if curr_node == None:
			curr_node = self.root
		if curr_node == None:
			return None
		left_node = curr_node.get_left()
		if left_node:
			return self.get_leftmost(left_node)
		else:
			return curr_node

	def get_rightmost(self, curr_node = None):
		if curr_node == None:
			curr_node = self.root
		if curr_node == None:
			return None
		right_node = curr_node.get_right()
		if right_node:
			self.get_rightmost(right_node)
		else:
			return curr_node

	def remove_node(self, data):
		if self.size == 0:
			return False
		
		parent = self.find_parent(data)
		if parent == None:
			if self.root.get_data() == data:
				left = self.root.get_left()
				right = self.root.get_right()
				self.size -= 1
				if not left and not right:
					self.root = None
					return True
				elif not left:
					self.root = right
					return True
				elif not right:
					self.root = left
					return True
				self.root = right
				leftmost = self.get_leftmost(right)
				leftmost.set_left(left)
				return True
			else:
				return False

		node = None
		is_left = True
		parent_left = parent.get_left()
		parent_right = parent.get_right()
		if parent_left and parent_left.get_data() == data:
			node = parent_left
		else:
			node = parent_right
			is_left = False

		left = node.get_left()
		right = node.get_right()
		self.size -= 1
		if not right and not left:
			if is_left:
				parent.set_left(None)
			else:
				parent.set_right(None)
			return True

		if not right:
			if is_left:
				parent.set_left(left)
			else:
				parent.set_right(left)
			return True

		if not left:
			if is_left:
				parent.set_left(right)
			else:
				parent.set_right(right)
			return True

		leftmost = self.get_leftmost(right)
		leftmost.set_left(left)
		if is_left:
			parent.set_left(right)
		else:
			parent.set_right(right)
		return True

	def preorder(self, curr_node = None, l = None):
		if l is None:
			l = []
		if curr_node == None:
			if self.root == None:
				print "Empty Tree"
				return
			else:
				curr_node = self.root

		print curr_node.get_data(),
		l.append(curr_node.get_data())

		left = curr_node.get_left()
		right = curr_node.get_right()

		if left:
			self.preorder(left, l)
		if right:
			self.preorder(right, l)

		if curr_node == self.root:
			print "\n"
			return l

	def inorder(self, curr_node = None, l = None):
		if l is None:
			l = []
		if curr_node == None:
			if self.root == None:
				print "Empty Tree"
				return
			else:
				curr_node = self.root

		left = curr_node.get_left()	
		right = curr_node.get_right()

		if left:
			self.inorder(left, l)
		print curr_node.get_data(),
		l.append(curr_node.get_data())
		if right:
			self.inorder(right, l)

		if curr_node == self.root:
			print "\n"
			return l

	def postorder(self, curr_node = None, l = None):
		if l is None:
			l = []
		if curr_node == None:
			if self.root == None:
				print "Empty Tree"
				return
			else:
				curr_node = self.root

		left = curr_node.get_left()	
		right = curr_node.get_right()

		if left:
			self.postorder(left, l)
		if right:
			self.postorder(right, l)
		print curr_node.get_data(),
		l.append(curr_node.get_data())

		if curr_node == self.root:
			print "\n"
			return l
		
	def __str__(self, curr_node = None):
		if curr_node == None:
			curr_node = self.root
		curr_string = ""
		if curr_node == None:
			return "Empty Tree"
		curr_string += "Node: " + str(curr_node.get_data()) + "\n"
		if curr_node.get_left() == None:
			curr_string += "Left Node: None\n"
		else:
			curr_string += "Left Node: " + str(curr_node.get_left().get_data()) + "\n"
		if curr_node.get_right() == None:
			curr_string += "Right Node: None\n"
		else:
			curr_string += "Right Node: " + str(curr_node.get_right().get_data()) + "\n"
		curr_string += "Parent Node: " + str(curr_node.get_parent()) + "\n\n"

		if curr_node.get_left() != None:
			curr_string += self.__str__(curr_node.get_left())

		if curr_node.get_right() != None:
			curr_string += self.__str__(curr_node.get_right())

		return curr_string

class BinarySearchTree(BinaryTree):
	def add_node(self, data, curr_node = None):
		if self.size == 0:
			self.root = Node(data)
			self.size += 1
			return True
		if curr_node == None:
			curr_node = self.root

		if curr_node.get_data() >= data:
			left = curr_node.get_left()
			if left:
				return self.add_node(data, left)
			else:
				curr_node.add_left(data)
				curr_node.get_left().set_parent(curr_node)
				self.size += 1
				return True
		if curr_node.get_data() < data:
			right = curr_node.get_right()
			if right:
				return self.add_node(data, right)
			else:
				curr_node.add_right(data)
				curr_node.get_right().set_parent(curr_node)
				self.size += 1
				return True
		return False

if __name__ == '__main__':
	# tree = BinaryTree(50)
	# tree_nodes = [50]
	# for i in range(10):
	# 	node_data = random.randint(0,100)
	# 	tree.add_node(node_data)
	# 	tree_nodes.append(node_data)
	# print tree
	# for i in range(11):
	# 	print tree_nodes
	# 	index = random.randint(0, len(tree_nodes) - 1)
	# 	remove_num = tree_nodes.pop(index)
	# 	print "Popping ", remove_num, "..."
	# 	while tree.remove_node(remove_num):
	# 		print "Node removed!"
	# 		print tree

	# print "*********************** BST *********************"
	# bst = BinarySearchTree(50)
	# bst_nodes = [50]
	# for i in range(10):
	# 	node_data = random.randint(0,100)
	# 	bst.add_node(node_data)
	# 	bst_nodes.append(node_data)
	# print bst
	# for i in range(11):
	# 	print bst_nodes
	# 	index = random.randint(0, len(bst_nodes) - 1)
	# 	remove_num = bst_nodes.pop(index)
	# 	print "Popping ", remove_num, "..."
	# 	while bst.remove_node(remove_num):
	# 		print "Node removed!"
	# 		print bst
	bst = BinarySearchTree()
	bst.add_node(4)
	bst.add_node(1)
	bst.add_node(7)
	bst.add_node(0)
	bst.add_node(2)
	bst.add_node(6)
	bst.add_node(9)
	bst.add_node(3)
	bst.add_node(8)
	bst.add_node(10)
	print bst
	root = bst.get_root()
	seven = root.get_right()
	seven.rotate_left()
	print bst

