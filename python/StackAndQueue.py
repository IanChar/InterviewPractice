class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.insert(0, data)

	def pop(self):
		if self.get_size():
			return self.stack.pop(0)

	def peek(self):
		if self.get_size():
			return self.stack[0]

	def get_size(self):
		return len(self.stack)

	def is_empty(self):
		return self.get_size() == 0

	def __str__(self):
		fin_string = ""
		for item in self.stack:
			fin_string += " " + str(item)
		return fin_string

class Queue:
	def __init__(self):
		self.queue = []

	def push(self, data):
		self.queue.insert(0, data)

	def pop(self):
		size = self.get_size()
		if size > 0:
			return self.queue.pop(size - 1)

	def peek(self):
		size = self.get_size()
		if size > 0:
			return self.queue[size - 1]		

	def get_size(self):
		return len(self.queue)

	def is_empty(self):
		return self.get_size() == 0

	def __str__(self):
		fin_string = ""
		for item in self.queue:
			fin_string += " " + str(item)
		return fin_string

if __name__ == '__main__':
	print "Stack stuff..."
	new_stack = Stack()
	for i in range(5):
		new_stack.push(i)
	print new_stack, " with size ", new_stack.get_size() 
	print new_stack.pop()
	print new_stack.pop()
	print new_stack, " with size ", new_stack.get_size() 
	for i in range(5, 10):
		new_stack.push(i)
	print new_stack, " with size ", new_stack.get_size()
	for i in range (10):
		print new_stack.pop()
	print new_stack, " with size ", new_stack.get_size()

	print "\nQueue stuff..." 
	new_queue = Queue()
	for i in range(5):
		new_queue.push(i)
	print new_queue, " with size ", new_queue.get_size() 
	print new_queue.pop()
	print new_queue.pop()
	print new_queue, " with size ", new_queue.get_size() 
	for i in range(5, 10):
		new_queue.push(i)
	print new_queue, " with size ", new_queue.get_size()
	for i in range (10):
		print new_queue.pop()
	print new_queue, " with size ", new_queue.get_size()