from LinkedList import LinkedList
from LinkedList import Node
from StackAndQueue import Stack
from StackAndQueue import Queue
import random
import copy
#Write code to remove deplicates from an unsorted linked list.
#Also do it with no temporary buffer allowed. Assume singly linked
def q1(link):
	#With temporary buffer
	link_copy = copy.deepcopy(link)
	curr = link_copy.get_head()
	if curr is None or curr.get_next() is None:
		return
	nxt = curr.get_next()
	temp_buf = []
	curr_data = curr.get_data()
	temp_buf.append(curr_data)
	while nxt:
		nxt_data = nxt.get_data()
		if nxt_data in temp_buf:
			nxt = nxt.get_next()
			curr.set_next(nxt)
		else:
			curr = curr.get_next()
			nxt = nxt.get_next()
			curr_data = curr.get_data()
			temp_buf.append(curr_data)
	print link_copy

	#Without temporary buffer
	curr = link.get_head()
	if curr is None or curr.get_next() is None:
		return
	while curr:
		data = curr.get_data()
		nxt = curr.get_next()
		if nxt is None:
			break
		if nxt.get_data() == data:
			curr.set_next(nxt.get_next())
		else:
			while nxt:
				nxtnxt = nxt.get_next()
				if nxtnxt and nxtnxt.get_data() == data:
					nxt.set_next(nxtnxt.get_next())
				else:
					nxt = nxt.get_next()
			curr = curr.get_next()
	print link


def q1_test():
	link1 = LinkedList()
	for i in range(10):
		link1.addNode(i // 3)
	print "Testing... ", link1
	q1(link1)
	
	link2 = LinkedList()
	for i in range(10):
		link2.addNode(1)
	print "\nTesting... ", link2
	q1(link2)
	
	link3 = LinkedList()
	link3.addNode(2)
	link3.addNode(1)
	link3.addNode(3)
	link3.addNode(5)
	link3.addNode(2)
	link3.addNode(0)
	link3.addNode(6)
	print "\nTesting... ", link3
	q1(link3)

	link4 = LinkedList()
	print "\nTesting... ", link4
	q1(link4)
	
#Implement algorithm to find kth to last element of singly linked list
def q2(link, k):
	curr = link.get_head()
	if curr is None:
		print "Out of Bounds"
		return 
	k_away = curr
	for i in range(k - 1):
		tmp = k_away.get_next()
		if tmp:
			k_away = tmp
		else:
			print "Out of Bounds"
			return
	while k_away.get_next():
		k_away = k_away.get_next()
		curr = curr.get_next()
	
	print curr
	return curr

def q2_test():
	link = LinkedList()
	for i in range(1, 10):
		link.addNode(i)
	print link
	print "Find 1st to last..."
	q2(link, 1)
	print "Find 4th to last..."
	q2(link, 4)
	print "Find 10th to last..."
	q2(link, 10)
	print "Find 11th to last..."
	q2(link, 11)

#Implement an algorithm to delete a node in the middle of a singly 
#linked list given only access to that node
def q3(node):
	nxt = node.get_next()
	node.set_data(nxt.get_data())
	node.set_next(nxt.get_next())
	return

def q3_test():
	link = LinkedList('a')
	link.addNode('b')
	node = Node('c')
	link.get_tail().set_next(node)
	link.set_tail(node)
	link.addNode('d')
	link.addNode('e')
	print "Testing... ", link
	q3(node)
	print link

#Write code to partition a linked list around a value x,
#such that all nodes less than x come before all nodes 
#greater than or equal to x
def q4(link, x):
	curr = link.get_head()
	less_list = None #Keep track of tail
	greater_list = None #Keep track of head
	head_node = None
	while curr:
		if curr.get_data() < x:
			if less_list is None:
				less_list = curr
				curr = curr.get_next()
				less_list.set_next(None)
				head_node = less_list
			else:
				temp = curr.get_next()
				less_list.set_next(curr)
				curr.set_next(None)
				less_list = curr
				curr = temp
		else:
			if greater_list is None:
				greater_list = curr
				curr = curr.get_next()
				greater_list.set_next(None)
			else:
				temp = curr.get_next()
				curr.set_next(greater_list)
				greater_list = curr
				curr = temp
	if head_node is None:
		head_node = greater_list
	else:
		less_list.set_next(greater_list)
	link = head_node
	#Done! Now to read off values
	curr = head_node
	while curr:
		print curr,
		curr = curr.get_next()
	print '\n'

def q4_test():
	link1 = LinkedList(5)
	for i in range(9):
		link1.addNode(random.randint(0,9))
	x1 = random.randint(0,9)
	print "Testing... x =", x1, " list: ", link1
	q4(link1, x1)
	link2 = LinkedList(5)
	for i in range(9):
		link2.addNode(random.randint(0,9))
	x2 = random.randint(0,9)
	print "Testing... x =", x2, " list: ", link2
	q4(link2, x2)
	link3 = LinkedList(5)
	for i in range(9):
		link3.addNode(random.randint(0,9))
	x3 = random.randint(0,9)
	print "Testing... x =", x3, " list: ", link3
	q4(link3, x3)

#You have two numbers represented by a linked list
#The number is stored in reverse order where each node is a digit
#PART 2 do it where they are stored in forwards order
def q5(num1, num2):
	node1 = num1.get_head()
	node2 = num2.get_head()
	carry = False
	s = node1.get_data() + node2.get_data()
	carry = s > 9
	s = s % 10
	final = LinkedList(s)
	node1 = node1.get_next()
	node2 = node2.get_next()
	while node1 and node2:
		s = node1.get_data() + node2.get_data() + carry
		carry = s > 9
		s = s % 10
		final.addNode(s)
		node1 = node1.get_next()
		node2 = node2.get_next()
	if carry and node1 is None and node2 is None:
		final.addNode(1)
	while node1:
		s = node1.get_data() + carry
		carry = s > 9
		s = s % 10
		final.addNode(s)
		node1 = node1.get_next()
	while node2:
		s = node2.get_data() + carry
		carry = s > 9
		s = s % 10
		final.addNode(s)
		node2 = node2.get_next()

	print final

def q5_2(num1, num2):
	length1 = 0
	length2 = 0
	node1 = num1.get_head()
	node2 = num2.get_head()
	#These should probably be in helper functions
	#Really almost all of this should be in respective funcs
	while node1 or node2:
		if node1: 
			node1 = node1.get_next()
			length1 += 1
		if node2:
			node2 = node2.get_next()
			length2 += 1
	
	node1 = num1.get_head()
	node2 = num2.get_head()
	if length1 == length2:
		head, carry = q5_helper(node1, node2)
		if carry:
			temp = Node(1)
			temp.set_next(head)
			head = temp
	
	elif length1 > length2:
		head, carry = q5_helper2(node1, node2, length1 - length2)
		if carry:
			tmp = Node(1)
			tmp.set_next(head)
			head = tmp
	else:
		head, carry = q5_helper2(node2, node1, length2 - length1)
		if carry:
			tmp = Node(1)
			tmp.set_next(head)
			head = tmp

	curr = head
	while curr:
		print curr,
		curr = curr.get_next()
	print '\n'
#Helper functions should have more helpful names
def q5_helper(node1, node2):
	if node1.get_next() is None:
		s = node1.get_data() + node2.get_data()
		carry = s > 9
		s = s % 10
		return Node(s), carry
	else:
		last_node, carry = q5_helper(node1.get_next(), node2.get_next())
		s = node1.get_data() + node2.get_data() + carry
		carry = s > 9 
		s = s % 10
		nxt_node = Node(s)
		nxt_node.set_next(last_node)
		return nxt_node, carry

def q5_helper2(long_node, short_node, excess):
	if excess == 1:
		tmp_node, carry = q5_helper(long_node.get_next(), short_node)
	else:
		tmp_node, carry = q5_helper2(long_node.get_next(), short_node, excess - 1)
	s = long_node.get_data() + carry
	carry = s > 9
	s = s % 10
	node = Node(s)
	node.set_next(tmp_node)
	return node, carry


def gen_test5(length1, length2):
	num1 = LinkedList(random.randint(1,9))
	num2 = LinkedList(random.randint(1,9))
	for i in range(length1):
		num1.addNode(random.randint(0,9))
	for i in range(length2):
		num2.addNode(random.randint(0,9))
	print "(Reverse)", num1, "+", num2, "="
	q5(num1, num2)
	print "(Forward)", num1, "+", num2, "="
	q5_2(num1, num2)

def q5_test():
	num1 = LinkedList(7)
	num1.addNode(1)
	num1.addNode(6)
	num2 = LinkedList(5)
	num2.addNode(9)
	num2.addNode(2)
	print "(Reverse)", num1, "+", num2, "="
	q5(num1, num2)
	print "(Forward)", num1, "+", num2, "="
	q5_2(num1, num2)

	gen_test5(3, 5)
	gen_test5(4, 5)
	gen_test5(5, 3)
	gen_test5(5, 4)

#Given a circular linked list, implement an algorithm which returns
#the node at the beginning of the loop
def q6(link):
	#Naive Way
	dic  = {}
	curr = link.get_head()
	found_loop = False
	while not found_loop:
		if curr in dic:
			found_loop = True
		else:
			dic[curr] = True
			curr = curr.get_next()
	print curr
	
	#Tricky way
	fast = link.get_head()
	fast = fast.get_next().get_next()
	slow = link.get_head()
	slow = slow.get_next()
	while not slow is fast:
		slow = slow.get_next()
		fast = fast.get_next().get_next()
	slow = link.get_head()
	while not slow is fast:
		slow = slow.get_next()
		fast = fast.get_next()
	print slow

def q6_test():
	link1 = LinkedList('A')
	curr = link1.get_head()
	curr.set_next(Node('B'))
	curr = curr.get_next()
	strt = Node('C')
	curr.set_next(strt)
	curr = curr.get_next()
	curr.set_next(Node('D'))
	curr = curr.get_next()
	curr.set_next(Node('E'))
	curr = curr.get_next()
	curr.set_next(strt)

	print "Testing..."
	curr = link1.get_head()
	for i in range(6):
		print curr,
		curr = curr.get_next()
	print '\n'
	q6(link1)

#Implement a way to see if a linked list is a palindrome
def q7(link):
	#With stack
	#Find middle of the list
	slow = link.get_head()
	fast = link.get_head()
	stack = Stack()
	while fast:
		fast = fast.get_next()
		if fast is None:
			break
		fast = fast.get_next()
		slow = slow.get_next()
	while slow:
		stack.push(slow.get_data())
		slow = slow.get_next()
	slow = link.get_head()
	pal = True
	while stack.get_size() != 0:
		if slow.get_data() != stack.pop():
			pal = False
			break
		slow = slow.get_next()
	print "Stack says", pal

	#By reversing
	fwd = link.get_head()
	bckwd = reverse(fwd)[0]
	pal = True
	while fwd and bckwd:
		if fwd.get_data() != bckwd.get_data():
			pal = False
			break
		fwd = fwd.get_next()
		bckwd = bckwd.get_next()
	print "Reverse says", pal

def reverse(head):
	nxt = head.get_next()
	if nxt is None:
		head = Node(head.get_data())
		return head, head
	else:
		data = head.get_data()
		head, last = reverse(nxt)
		nxt = Node(data)
		last.set_next(nxt)
		return head, nxt


def q7_test():
	link1 = LinkedList('C')
	link1.addNode('A')
	link1.addNode('T')
	print "Testing", link1
	q7(link1)

	link2 = LinkedList('R')
	link2.addNode('A')
	link2.addNode('C')
	link2.addNode('E')
	link2.addNode('C')
	link2.addNode('A')
	link2.addNode('R')
	print "\nTesting", link2
	q7(link2)

	link3 = LinkedList('A')
	link3.addNode('B')
	link3.addNode('B')
	link3.addNode('A')
	print "\nTesting", link3
	q7(link3)

	link4 = LinkedList('E')
	link4.addNode('V')
	link4.addNode('E')
	link4.addNode('N')
	print "\nTesting", link4
	q7(link4)

	link5 = LinkedList('R')
	link5.addNode('A')
	link5.addNode('C')
	link5.addNode('E')
	link5.addNode('C')
	link5.addNode('R')
	link5.addNode('A')
	link5.addNode('R')
	link5.addNode('C')
	link5.addNode('E')
	link5.addNode('C')
	link5.addNode('A')
	link5.addNode('R')
	print "\nTesting", link5
	q7(link5)


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
		else:
			print "Invalid input"