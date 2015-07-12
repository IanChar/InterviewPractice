from StackAndQueue import Stack
from StackAndQueue import Queue
from LinkedList import Node
from LinkedList import LinkedList
import random

#Use a single array to implement 3 stacks
class Q1:
	def __init__(self):
		self.stacks= [1, 2, 3]
		self.sub_list = [0,1,2]

	def push(self, stack, data):
		self.stacks.insert(self.sub_list[stack] + 1, data)
		for i in range(stack + 1, 3):
			self.sub_list[i] += 1
		return True

	def pop(self, stack):
		if  stack == 2:
			if self.sub_list[stack] + 1 != len(self.stacks):
				self.stacks.pop(self.sub_list[stack] + 1)
				for i in range(stack + 1, 3):
					self.sub_list[i] -= 1
				return True
		else:
			if self.sub_list[stack] + 1 != self.sub_list[stack + 1]:
				self.stacks.pop(self.sub_list[stack] + 1)
				for i in range(stack + 1, 3):
					self.sub_list[i] -= 1
				return True
		return False

	def __str__(self):
		fin_string = "Stack 1: "
		for i in range(self.sub_list[0] + 1, self.sub_list[1]):
			fin_string += " " + str(self.stacks[i])
		fin_string += "\nStack 2: "
		for i in range(self.sub_list[1] + 1, self.sub_list[2]):
			fin_string += " " + str(self.stacks[i])
		fin_string += "\nStack 3: "
		for i in range(self.sub_list[2] + 1, len(self.stacks)):
			fin_string += " " + str(self.stacks[i])
		return fin_string

def q1_test():
	test = Q1()
	print test
	for i in range(9):
		test.push(i % 3, i)
	print test
	for i in range(4):
		test.pop(0)
	for i in range(2):
		test.pop(1)
	for i in range(1):
		test.pop(2)
	print test

#Design a stack that also has min func that is O(1)
class Q2:
	def __init__(self):
		self.stack = []

	def peek(self):
		if len(self.stack) > 0:
			return self.stack[0][0]

	def min(self):
		if len(self.stack) > 0:
			return self.stack[0][1]	
	
	def push(self, data):
		old_min = self.min()
		if old_min is None or old_min > data:
			self.stack.insert(0, (data, data))
		else:
			self.stack.insert(0, (data, old_min))
		return True

	def pop(self):
		if len(self.stack) > 0:
			return self.stack.pop(0)[0]

	def __str__(self):
		fin_string = ""
		for item in self.stack:
			fin_string += str(item[0]) + " "
		fin_string += "min:" + str(self.min())
		return fin_string 

def q2_test():
	test = Q2()
	for i in range(10):
		test.push(random.randint(0, 9))
	print test
	for i in range(11):
		test.pop()
		print test

#Make a datastructure that adds stacks if one gets too big
class Q3:
	def __init__(self, max_capacity = 5):
		self.stack_of_stacks = [Stack()]

	def push(self, data):
		if self.stack_of_stacks[0].get_size() >= 5:
			self.stack_of_stacks.insert(0, Stack())
		self.stack_of_stacks[0].push(data)
		return True

	def pop(self, index = 0):
		stack = self.stack_of_stacks[index]
		data = stack.pop()
		if stack.get_size() == 0:
			if len(self.stack_of_stacks) != 1:
				self.stack_of_stacks.pop(index)
		return data

	def __str__(self):
		fin_string = ""
		for i in range(len(self.stack_of_stacks)):
			fin_string += "Stack " + str(i) + ": " + str(self.stack_of_stacks[i]) + "\n"
		return fin_string

def q3_test():
	test = Q3()
	for i in range(15):
		test.push(i)
	print test
	for i in range(5):
		test.pop()
	print test
	for i in range(4):
		test.pop(random.randint(0,1))
		print test
			
#Solve the tower of Hanoi Problem
def q4(disks):
	if disks < 3:
		disks = 3
	stacks = [Stack(), Stack(), Stack()]
	start_stack = stacks[0]
	for i in range(disks):
		start_stack.push(disks - i)

	print "Start"
	for i in range(1, 4):
		print "Stack", i, ":", stacks[i - 1]
	solve_hanoi(stacks, disks, 0, 2)
	print "\nDone!"
	for i in range(1, 4):
		print "Stack", i, ":", stacks[i - 1]

def solve_hanoi(stacks, disks, start, dest):
	mid = start ^ dest ^ 0 ^ 1 ^ 2
	s_stack = stacks[start]
	m_stack = stacks[mid]
	d_stack = stacks[dest]
	if disks == 3:
		d_stack.push(s_stack.pop())
		m_stack.push(s_stack.pop())
		m_stack.push(d_stack.pop())
		d_stack.push(s_stack.pop())
		s_stack.push(m_stack.pop())
		d_stack.push(m_stack.pop())
		d_stack.push(s_stack.pop())
		print "\nIterate"
		for i in range(1, 4):
			print "Stack", i, ":", stacks[i - 1]
	else:
		solve_hanoi(stacks, disks - 1, start, mid)
		d_stack.push(s_stack.pop())
		solve_hanoi(stacks, disks - 1, mid, dest)

def q4_test():
	for i in range(3, 8):
		print "\nSolving for", i, "disks..."
		q4(i)

#Implement a Queue using two stacks
class Q5:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def push(self, data):
		self.stack1.push(data)

	def pop(self):
		size = self.stack1.get_size()
		if size != 0:
			for i in range(size):
				self.stack2.push(self.stack1.pop())
			rtrn = self.stack2.pop()
			for i in range(size - 1):
				self.stack1.push(self.stack2.pop())
			return rtrn

def q5_test():
	test = Q5()
	for i in range(10):
		test.push(i)

	for i in range(11):
		print test.pop(),
	print ""

#Write a program to sort stack in ascending order
#You can use one other stack 
def q6(stack):
	help_stack = Stack()
	while not stack.is_empty():
		to_place = stack.pop()
		if help_stack.is_empty():
			help_stack.push(to_place)
		else:
			removed = 0
			placed = False
			while not help_stack.is_empty() and not placed:
				if to_place <= help_stack.peek():
					help_stack.push(to_place)
					placed = True
				stack.push(help_stack.pop())
				removed += 1
			if not placed:
				help_stack.push(to_place)
			for i in range(removed):
				help_stack.push(stack.pop())
	while not help_stack.is_empty():
		stack.push(help_stack.pop())
	print stack

def q6_test():
	test = Stack()
	for i in range(10):
		test.push(random.randint(0,9))
	print "Pre sort:", test
	print "Post sort:",
	q6(test)

#Create a data structure that will give oldest dog, cat,
#or either in the animal shelter
class AnimalNode(Node):
	def __init__(self, data, species, nxt = None):
		self.data = data
		self.prev = None
		self.nxt = nxt
		self.species = species

	def get_species(self):
		return self.species

	def set_species(self, species):
		self.species = species


class Q7:
	def __init__(self):
		self.cat_queue = Queue()
		self.dog_queue = Queue()
		self.any_list = None
		self.total_animals = 0

	def push_dog(self, name):
		list_node = AnimalNode(name, "dog")
		queue_node = AnimalNode(name, "dog")
		queue_node.set_next(list_node)
		self.dog_queue.push(queue_node)
		if not self.any_list is None:
			list_node.set_next(self.any_list)
		self.any_list = list_node
		self.total_animals += 1

	def push_cat(self, name):
		list_node = AnimalNode(name, "cat")
		queue_node = AnimalNode(name, "cat")
		queue_node.set_next(list_node)
		self.cat_queue.push(queue_node)
		if not self.any_list is None:
			list_node.set_next(self.any_list)
		self.any_list = list_node
		self.total_animals += 1

	def pop_dog(self):
		popped = self.dog_queue.pop()
		if popped is None:
			return 
		popped_name = popped.get_data()
		popped = popped.get_next()
		replace = popped.get_next()
		if self.total_animals == 1:
			self.any_list = None
		elif replace is None:
			curr = self.any_list
			if curr.get_next():
				while curr.get_next().get_next():
					curr = curr.get_next()
			curr.set_next(None)
		else:
			popped.set_next(replace.get_next())
			popped.set_species(replace.get_species())
			popped.set_data(replace.get_data())
		self.total_animals -= 1
		return popped_name

	def pop_cat(self):
		popped = self.cat_queue.pop()
		if popped is None:
			return 
		popped_name = popped.get_data()
		popped = popped.get_next()
		replace = popped.get_next()
		if self.total_animals == 1:
			self.any_list = None
		elif replace is None:
			curr = self.any_list
			if curr.get_next():
				while curr.get_next().get_next():
					curr = curr.get_next()
			curr.set_next(None)
		else:
			popped.set_next(replace.get_next())
			popped.set_species(replace.get_species())
			popped.set_data(replace.get_data())
		self.total_animals -= 1
		return popped_name

	def pop_any(self):
		curr = self.any_list
		if curr is None:
			return 
		self.total_animals -= 1

		if curr.get_next() is None:
			self.any_list = None
			if curr.get_species() == "dog":
				self.dog_queue.pop()
			else:
				self.cat_queue.pop()
			return curr.get_data()
		
		while not curr.get_next().get_next() is None:
			curr = curr.get_next()
		popped = curr.get_next()
		if popped.get_species() == "dog":
			self.dog_queue.pop()
		else:
			self.cat_queue.pop()
		curr.set_next(None)

		return popped.get_data()

	def __str__(self):
		fin_string = "Dog Queue: " + str(self.dog_queue)
		fin_string += "\nCat Queue: " + str(self.cat_queue)
		fin_string += "\nCombined Queue: "
		curr = self.any_list
		while curr:
			fin_string += str(curr) + " "
			curr = curr.get_next()
		return fin_string

def q7_test():
	test = Q7()
	for i in range(10):
		rand = random.randint(0,9)
		if rand % 2 == 0:
			test.push_dog(rand)
		else:
			test.push_cat(rand)
	print test, '\n'
	for i in range(3):
		test.pop_dog()
		print test, '\n'
	for i in range(3):
		test.pop_cat()
		print test, '\n'
	for i in range(4):
		test.pop_any()
		print test, '\n'


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