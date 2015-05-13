from Tree import BinaryTree as BT
from Tree import BinarySearchTree as BST
from Tree import Node
from Graph import Vertex
from Graph import Graph
from StackAndQueue import Stack
from StackAndQueue import Queue
from LinkedList import LinkedList
import random
#Implement code to check if binary tree is balanced
#AKA tree has subtrees such that heights never differ
#by more than 1

#O(n) time since must touch every node
#O(logn) mem since recursive
def q1(tree):
	root = tree.get_root()
	return q1_helper(root) != -1

def q1_helper(head):
	if head is None:
		return 0
	right = head.get_right()
	left = head.get_left()	
	right_length = q1_helper(right)
	left_length = q1_helper(left)
	if right_length == -1 or left_length == -1:
		return -1
	elif abs(right_length - left_length) > 1:
		return -1
	else:
		if right_length > left_length:
			bigger = right_length
		else:
			bigger = left_length
		return bigger + 1

def q1_test():
	test1 = BT()
	for i in range(10):
		test1.add_node(i)
	print "Testing ", str(test1), "..."
	print q1(test1)

	test2 = BST(5)
	for i in range(10):
		test2.add_node(random.randint(0,9))
	print "Testing ", str(test2), "..."
	print q1(test2)

#Given a directed graph, design an algorithm to find
#out whether there is a route between two nodes

#At worst O(n) time and touches every node
#O(1) memory
def q2(node1, node2):
	#By traversal can also do by adjacency matrix
	if len(node1.get_edges()) == 0 and len(node2.get_edges()) == 0:
		return False
	#We will do DFS but can also do BFS
	curr = node1
	stack = Stack()
	visited = [node1]
	edges = node1.get_edges().keys()
	for edge in edges:
		if edge is node2:
			return True
		stack.push(edge)
	while not stack.is_empty():
		curr = stack.pop()
		while curr in visited:
			curr = stack.pop()
		if curr is None:
			break
		visited.append(curr)
		edges = curr.get_edges().keys()
		for edge in edges:
			if edge is node2:
				return True
			stack.push(edge)
	return False

def q2_test():
	graph = Graph()
	graph.sample_graph()
	v1 = graph.get_vertex('A')
	v2 = graph.get_vertex('E')
	print "Path from A to E?", q2(v1, v2)

	v1 = graph.get_vertex('F')
	v2 = graph.get_vertex('C')
	print "Path from F to C?", q2(v1, v2)

#Given sorted integer array with unique elements,
#Write an algorithm to create BST with min height

#O(n) time because must touch every node
#O(n) memory (also logn for recursion)
def q3(arr):
	lower = 0
	upper = len(arr) - 1
	mid = upper // 2
	tree = BST(arr[mid])
	node = tree.get_root()
	q3_helper(arr, lower, mid - 1, node)
	q3_helper(arr, mid + 1, upper, node)
	print tree
	return tree

def q3_helper(arr, lower, upper, node):
	if lower == upper:
		data = arr[upper]
		new_node = Node(data)
		if data > node.get_data():
			node.set_right(new_node)
		else:
			node.set_left(new_node)
		return
	if upper < lower:
		return
	mid = (upper - lower) // 2 + lower
	data = arr[mid]
	new_node = Node(data)
	if data > node.get_data():
		node.set_right(new_node)
	else:
		node.set_left(new_node)
	q3_helper(arr, lower, mid - 1, new_node)
	q3_helper(arr, mid + 1, upper, new_node)

def q3_test():
	arr = range(10)
	tree = q3(arr)
	print "Is it balanced?", q1(tree)

#Given a binary tree, design algorithm which creates
#a linked list of all the nodes at each depth 
def q4(tree):
	#Using a dict....
	lvls = {}
	root = tree.get_root()
	make_dict(root, 1, lvls)
	for level, link in lvls.iteritems():
		print link

	#You can also use an altered version of BFS
	#However, both run in O(n) time and each
	#return O(n) amount of data. This one 
	#creates O(logn) data because of stacks
	#but that is dwarfed by O(n)

def make_dict(root, level, lvls):
	if root is None:
		return
	if not level in lvls.keys():
		lvls[level] = LinkedList()
	lvls[level].addNode(root.get_data())
	make_dict(root.get_right(), level + 1, lvls)
	make_dict(root.get_left(), level + 1, lvls)


def q4_test():
	arr = range(10)
	tree = q3(arr)
	q4(tree)

#Check if a BT is also a BST

#O(n) time must touch every node
#O(logn) mem for recursion
def q5(root, lowest = None, highest = None):
	#Could also do in order transversal then
	#check to see if in order. Keep track of
	#last element found and compare to current
	#element. Can't account for doubles though
	if root is None:
		return True
	right = root.get_right()
	left = root.get_left()
	if right is None and left is None:
		return True
	data = root.get_data()
	if right:
		data2 = right.get_data()
		if data2 <= data:
			return False
		if not highest is None and data2 > highest:
			return False
		if not lowest is None and data2 <= lowest:
			return False
	if left:
		data2 = left.get_data()
		if data2 > data:
			return False
		if not highest is None and data2 > highest:
			return False
		if not lowest is None and data2 <= lowest:
			return False

	bool1 = q5(right, data, highest)
	bool2 = q5(left, lowest, data)
	return bool1 and bool2

def q5_test():
	bt = BT(5)
	bt.add_node(4)
	bt.add_node(6)
	bt.add_node(1)
	bt.add_node(6)
	bt.add_node(3)
	bt.add_node(7)
	print "False =", q5(bt.get_root())

	bst = BST(5)
	for i in range(10):
		bst.add_node(random.randint(0,9))
	print "True =", q5(bst.get_root())

#Write an algorithm to find next node (in-order succesor)
#given a node in a BST. You may assume each node has link
#to parent

#O(n) time very worst case would have to touch every node
#O(1) mem
def q6(node):
	parent = node.get_parent()
	if parent is None:
		right = node.get_right()
		if right is None:
			return
		leftmost = right.get_left()
		if leftmost is None:
			return leftmost.get_data()
		while leftmost.get_left():
			leftmost = leftmost.get_left()
		return leftmost.get_data()
	elif parent.get_left() is node:
		return parent.get_data()
	else:
		grand_parent = parent.get_parent()
		if grand_parent is None:
			return
		if grand_parent.get_left() is parent:
			return grand_parent.get_data()
		while grand_parent and not grand_parent.get_left() is parent:
			parent = grand_parent
			grand_parent = parent.get_parent()
		if grand_parent is None:
			return 
		else:
			return grand_parent.get_data()


def q6_test():
	test1 = BST(4)
	test1.add_node(1)
	test1.add_node(7)
	test1.add_node(0)
	test1.add_node(2)
	test1.add_node(5)
	test1.add_node(8)
	test1.add_node(3)
	test1.add_node(6)
	test1.add_node(9)
	three = test1.get_root().get_left().get_right().get_right()
	print "After", three, "comes", q6(three)
	four = test1.get_root()
	print "After", four, "comes", q6(four)
	nine = test1.get_root().get_right().get_right().get_right()
	print "After", nine, "comes", q6(nine)

#Design algorithm to write code to find the first common
#ancestor of two nodes in a binary tree. No additional data strucs
def q7(root, node1, node2):
	#Initial Solution...
	#Time is O(nlogn) I think... JK O(n)
	#Mem is O(lognlogn) I think because recursion in recursion
	ancestor = find_ancestor(root, node1, node2)
	print "Initial solution says...", ancestor

	#Optimal Solution...
	ancestor = get_ancestor(root, node1, node2)
	if ancestor is node1 or ancestor is node2:
		ancestor = None
	print "Optimal solution says...", ancestor, '\n'

def get_ancestor(root, node1, node2):
	if root is None or root is node1 or root is node2:
		return root
	left = get_ancestor(root.get_left(), node1, node2)
	if not left is None and not left is node1 and not left is node2:
		return left
	right = get_ancestor(root.get_right(), node1, node2)
	if not right is None and not right is node1 and not right is node2:
		return right
	if (left is node1 and right is node2) or (right is node1 and left is node2):
		return root
	if left:
		return left
	else:
		return right
	return None


def find_ancestor(root, node1, node2):
	if root is None:
		return None
	if is_parent(root, node1) and is_parent(root, node2):
		left_ancestor = find_ancestor(root.get_left(), node1, node2)
		right_ancestor = find_ancestor(root.get_right(), node1, node2)
		if left_ancestor is None and right_ancestor is None:
			return root
		elif left_ancestor:
			return left_ancestor
		else:
			return right_ancestor
	else:
		return None


def is_parent(root, node):
	if root is None:
		return False
	right = root.get_right()
	left = root.get_left()
	if right is None and left is None:
		return False
	if right is node or left is node:
		return True
	return is_parent(left, node) or is_parent(right, node)

def q7_test():
	test1 = BST(4)
	test1.add_node(1)
	test1.add_node(7)
	test1.add_node(0)
	test1.add_node(2)
	test1.add_node(5)
	test1.add_node(8)
	test1.add_node(3)
	test1.add_node(6)
	test1.add_node(9)
	zero = test1.get_root().get_left().get_left()
	three = test1.get_root().get_left().get_right().get_right()
	four = test1.get_root()
	six = test1.get_root().get_right().get_left().get_right()
	nine = test1.get_root().get_right().get_right().get_right()
	print "Common ancestor for", three, "and", nine, "is..." 
	q7(four, three, nine)
	print "Common ancestor for", zero, "and", three, "is..." 
	q7(four, zero, three)
	print "Common ancestor for", six, "and", nine, "is..." 
	q7(four, six, nine)
	print "Common ancestor for", four, "and", nine, "is..." 
	q7(four, four, nine)

#Given a very large BT t1 and a large tree t2 decide if t2 is 
#a syubtree of t1

#O(n + km) time where n is for t1, m is for k2 and k is for potential subtrees
#	really on average it is even lower because it will catch a mistake early on
#O(logn + logm) memory for each recursive process
def q8(t1, t2):
	#Besides this way you can see if T2's pre order is substring
	# of T1's pre order and T2's in order is substring of T1's in order
	#This would have O(n + m) mem and O(n + m) time
	if t1 is None or t2 is None:
		return False
	if t1.get_data() == t2.get_data():
		if check_subtree(t1, t2):
			return True
	return q8(t1.get_left(), t2) or q8(t1.get_right(), t2)

def check_subtree(t1, t2):
	if t1 is None and t2 is None:
		return True
	if (t1 is None and not t2 is None) or (t2 is None and not t1 is None):
		return False
	if t1.get_data() != t2.get_data():
		return False
	else:
		return check_subtree(t1.get_right(), t2.get_right()) and check_subtree(t1.get_left(), t1.get_left())

def q8_test():
	arr = range(10)
	tree = q3(arr)

	subtree1 = BST(7)
	subtree1.add_node(5)
	subtree1.add_node(8)
	subtree1.add_node(6)
	subtree1.add_node(9)

	subtree2 = BST(1)
	subtree2.add_node(0)
	subtree2.add_node(2)
	subtree2.add_node(1)

	print "Is 1 a subtree?", q8(tree.get_root(), subtree1.get_root())
	print "Is 2 a subtree?", q8(tree.get_root(), subtree2.get_root())

#Given a BT find all paths that sum to a given value

#O(n^2) time at worst (n + (n-1) + (n-3) + (n-7))
#	JK I guess that is O(nlogn)
#O(k + logn) mem where k is number of paths
def q9(tree, num):
	paths = []
	traverse_paths(tree.get_root(), num, paths)
	return paths

def traverse_paths(root, num, paths):
	if root is None:
		return
	find_paths(root, root, 0, paths, num)
	left = root.get_left()
	traverse_paths(left, num, paths)
	right = root.get_right()
	traverse_paths(right, num, paths)

def find_paths(curr, start, s, paths, num):
	if curr is None:
		return
	data = curr.get_data()
	if data >= num:
		return
	s += data
	if s == num:
		paths.append((start, curr))
		return
	if s > num:
		return
	find_paths(curr.get_left(), start, s, paths, num)
	find_paths(curr.get_right(), start, s, paths, num)

def q9_test():
	tree = BT(5)
	for i in range(14):
		tree.add_node(random.randint(0,9))
	print tree
	paths = q9(tree, 15)
	for path in paths:
		print "Start:", path[0], "End:", path[1]

if __name__ == '__main__':
	running = True
	while running:
		num = raw_input("Input question to test (type q for quit): ")
		if str(num) == 'q':
			running = False
			break
		if int(num) == 1:
			q1_test()
		elif int(num) == 2:
			q2_test()
		elif int(num) == 3:
			q3_test()
		elif int(num) == 4:
			q4_test()
		elif int(num) == 5:
			q5_test()
		elif int(num) == 6:
			q6_test()
		elif int(num) == 7:
			q7_test()
		elif int(num) == 8:
			q8_test()
		elif int(num) == 9:
			q9_test()	
		else:
			print "Invalid input"