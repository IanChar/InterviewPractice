import random

def select(l):
	for i, curr in enumerate(l):
		m = curr
		m_index = i
		for j in range(i, len(l)):
			if l[j] < m:
				m = l[j]
				m_index = j
		l[i], l[m_index] = m, curr

def bubble(l):
	done = False
	while not done:
		done = True
		for i in range(len(l) - 1):
			if l[i] > l[i + 1]:
				l[i], l[i + 1] = l[i + 1], l[i]
				done = False

# Run time O(nlogn) at worst
#Probably not ideal way since had to use temp buffs
def merge(l, start = None, end = None):
	if start is None:
		start = 0
		end = len(l)
	if start >= end - 1:
		return
	if start + 2 == end:
		end -= 1
		if l[start] > l[end]:
			l[start], l[end] = l[end], l[start]
		return
	mid = (end + start) // 2
	merge(l, start, mid)
	merge(l, mid, end)
	temp1 = l[start:mid]
	temp2 = l[mid:end]
	for k in range(start, end):
		if len(temp1) == 0:
			l[k] = temp2.pop(0)
		elif len(temp2) == 0:
			l[k] = temp1.pop(0)
		elif temp1[0] >= temp2[0]:
			l[k] = temp2.pop(0)
		else:
			l[k] = temp1.pop(0)

def quick(l, start = None, end = None):
	if start is None:
		start = 0
		end = len(l)
	if start >= end - 1:
		return
	if start == end - 2:
		end = end - 1
		if l[start] > l[end]:
			l[start], l[end] = l[end], l[start]
		return
	pivot = l[end - 1]
	fwd = start
	bckwd = end - 2
	over = False
	under = False
	while fwd <= bckwd:
		if not over:
			if l[fwd] > pivot:
				over = True
			else:
				fwd += 1
		if not under:
			if l[bckwd] <= pivot:
				under = True
			else:
				bckwd -= 1
		if over and under:
			l[fwd], l[bckwd] = l[bckwd], l[fwd]
			over, under = False, False
			fwd += 1
			bckwd -= 1
	if fwd == bckwd:
		fwd += 1
	l[end - 1], l[fwd] = l[fwd], pivot
	quick(l, start, fwd)
	quick(l, fwd, end)

def radix(l):
	buckets = [[] for _ in range(10)]
	done = False
	n = 1
	while not done:
		done = True
		for num in l:
			key = (num % (n * 10)) // n
			if key != 0:
				done = False
			buckets[key].append(num)
		i = 0
		for bucket in buckets:
			for num in bucket:
				l[i] = num
				i += 1
		buckets = [[] for _ in range(10)]
		n *= 10

class MinHeap:
	def __init__(self, arr = None):
		if arr is None:
			self.arr = []
		else:
			self.arr = arr
		self.size = 0

	def get_parent(self, index):
		if index == 0:
			return 
		if index % 2 == 1:
			index += 1
		return index // 2 - 1

	def get_left(self, index):
		return index * 2 + 1

	def add(self, key):
		self.arr.append(key)
		index = len(self.arr) - 1
		parent = self.get_parent(index)
		while not parent is None:
			if self.arr[index] < self.arr[parent]:
				self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
				index = parent
				parent = self.get_parent(parent)
			else:
				break

	def get_min(self):
		return self.arr[0]

	def remove_min(self):
		if len(self.arr) == 0:
			return
		if len(self.arr) == 1:
			return self.arr.pop()
		rtn = self.arr.pop(0)
		self.arr.insert(0, self.arr.pop())
		self.heapify()
		return rtn

	def heapify(self):
		curr = 0
		left = self.get_left(curr)
		right = self.get_left(curr) + 1
		while left < len(self.arr):
			if not right < len(self.arr):
				if self.arr[left] < self.arr[curr]:
					self.arr[left], self.arr[curr] = self.arr[curr], self.arr[left]
					curr = left
				else:
					break
			elif self.arr[left] < self.arr[right]:
				if self.arr[left] < self.arr[curr]:
					self.arr[left], self.arr[curr] = self.arr[curr], self.arr[left]
					curr = left
				else:
					break
			else:
				if self.arr[right] < self.arr[curr]:
					self.arr[right], self.arr[curr] = self.arr[curr], self.arr[right]
					curr = right
				else:
					break
			left = self.get_left(curr)
			right = self.get_left(curr) + 1

def heap(l):
	h = MinHeap()
	for item in l:
		h.add(item)
	for i in range(len(l)):
		l[i] = h.remove_min()

def create_list(size, lower, upper):
	return [random.randint(lower, upper) for _ in range(size)]

if __name__ == '__main__':
	running = True
	while running:
		print "\n1:Selection\n2:Bubble\n3:Merge\n4:Quick\n5:Radix\n6:Heap\nAnything else to quit"
		selection = int(raw_input("Input:"))
		if selection == 1:
			to_sort = create_list(10, 0, 9)
			print to_sort
			select(to_sort)
			print to_sort
		elif selection == 2:
			to_sort = create_list(10, 0, 9)
			print to_sort
			bubble(to_sort)
			print to_sort
		elif selection == 3:
			c = 0
			to_sort = create_list(10, 0, 9)
			print to_sort
			merge(to_sort)
			print to_sort
		elif selection == 4:
			to_sort = create_list(10, 0, 9)
			print to_sort
			quick(to_sort)
			print to_sort
		elif selection == 5:
			to_sort = create_list(10, 0, 1000)
			print to_sort
			radix(to_sort)
			print to_sort
		elif selection == 6:
			to_sort = create_list(10, 0, 9)
			print to_sort
			heap(to_sort)
			print to_sort
		else:
			running = False


