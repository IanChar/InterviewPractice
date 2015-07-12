import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from python.data_structures.Tree import Node, BinaryTree, BinarySearchTree
# Construct a tree using pre-order and inorder traversal
# This takes O(n) time since every node should be touched once
# Mem is something like 2(n/2 + n/4 + n/8) etc
def rebuild_tree(inorder, preorder, node = None, left = None):
	if len(preorder) == 1:
		root = Node(preorder.pop())
		if node is not None:
			if left:
				node.set_left(root)
			else:
				node.set_right(root)
		return root
	if len(preorder) == 0:
		return
	root = preorder[0]
	pivot = inorder.index(root)
	left_in = inorder[:pivot]
	right_in = inorder[pivot:]
	for index, item in enumerate(preorder):
		if index != 0 and item not in left_in:
			pivot = index
			break
	left_pre = preorder[1:pivot]
	right_pre = preorder[pivot:]
	root = Node(root)
	if node is not None:
		if left:
			node.set_left(root)
		else:
			node.set_right(root)
	rebuild_tree(left_in, left_pre, root, True)
	rebuild_tree(right_in, right_pre, root, False)
	return root

# This can also be done without inorder. Easy if O(nlogn) is
# good enough just go through list and use add_node func.
# But how do you do it in O(n) time?
def reubild_tree2(preorder, tree = None):
	pass

def print_preorder(node):
	if node is None:
		return
	print node,
	print_preorder(node.get_left())
	print_preorder(node.get_right())


def q1_test():
	tree = BinarySearchTree()
	tree.add_node(4)
	tree.add_node(1)
	tree.add_node(7)
	tree.add_node(0)
	tree.add_node(2)
	tree.add_node(5)
	tree.add_node(8)
	tree.add_node(3)
	tree.add_node(6)
	tree.add_node(9)
	print tree
	inorder = tree.inorder()
	preorder = tree.preorder()
	print "Inorder:", inorder
	print "Preorder:", preorder
	node = rebuild_tree(inorder, preorder)
	print node
	print_preorder(node)
	print ""

# Check if a number is prime
# I just copied and pasted this. Not really any clever way
# Although seems some loop unrolling was performed
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Given a string, check if it is made of a repeated substring
# This is O(n) time since it only has to iterate through the
# string once. However takes around O(n) mem. Brute force
# has constant mem but is O(n^2)
def is_repeated(s):
	s_length = len(s)
	curr = []
	tmp = []
	curr_index = 0
	for char in s:
		if len(curr) == 0:
			curr.append(char)
		else:
			tmp.append(char)
			if char == curr[curr_index]:
				if curr_index + 1 >= len(curr):
					curr_index = 0
				else:
					curr_index += 1
			else:
				curr.extend(tmp)
				tmp = []
				curr_index = 0
	print "Substring:", "".join(curr)
	if len(curr) > len(s) // 2:
		return False
	else:
		return True

def q2_test():
	test1 = "abcabcabc"
	print test1
	print is_repeated(test1)

	test2 = "aacaacaac"
	print "\n", test2
	print is_repeated(test2)

	test3 = "abcabcabd"
	print "\n", test3
	print is_repeated(test3)

	test4 = "a"
	print "\n", test4
	print is_repeated(test4)

if __name__ == '__main__':
	running = True
	while running:
		print "1:rebuild_tree\n2:is_repeated"
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
