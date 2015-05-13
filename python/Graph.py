import StackAndQueue as sq

class Vertex:
	def __init__(self, data):
		self.data = data
		self.edges = {}

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_edge(self, vertex, weight = 1):
		self.edges[vertex] = weight

	def get_edges(self):
		return self.edges

	def __str__(self):
		return str(self.data)

class Graph:
	def __init__(self):
		self.vertices = []

	def get_vertex(self, data):
		for vertex in self.vertices:
			if vertex.get_data() == data:
				return vertex

	def add_vertex(self, data):
		self.vertices.append(Vertex(data))

	def sample_graph(self):
		self.vertices = []
		a = Vertex('A')
		b = Vertex('B')
		c = Vertex('C')
		d = Vertex('D')
		e = Vertex('E')
		f = Vertex('F')
		a.set_edge(b, 7)
		a.set_edge(c, 1)
		b.set_edge(d, 4)
		b.set_edge(f, 1)
		c.set_edge(b, 5)
		c.set_edge(e, 2)
		c.set_edge(f, 7)
		e.set_edge(b, 2)
		e.set_edge(d, 5)
		f.set_edge(e, 3)
		self.vertices.append(a)
		self.vertices.append(b)
		self.vertices.append(c)
		self.vertices.append(d)
		self.vertices.append(e)
		self.vertices.append(f)

	def dft(self, start = 0):
		if len(self.vertices) == 0:
			print "Empty"
			return
		stack = sq.Stack()
		visited = []
		curr_vertex = self.vertices[0]
		visited.append(curr_vertex.get_data())
		for key in curr_vertex.get_edges().keys():
			if not key in visited:
				stack.push(key)
		while stack.get_size() > 0:
			curr_vertex = self.get_vertex(stack.pop())
			while curr_vertex != None and curr_vertex.get_data() in visited:
				curr_vertex = self.get_vertex(stack.pop())
			if curr_vertex == None:
				break
			visited.append(curr_vertex.get_data())
			for key in curr_vertex.get_edges().keys():
				if not key in visited:
					stack.push(key)

		return visited

	def bft(self, start = 0):
		if len(self.vertices) == 0:
			print "Empty"
			return
		queue = sq.Queue()
		visited = []
		curr_vertex = self.vertices[0]
		visited.append(curr_vertex.get_data())
		for key in curr_vertex.get_edges().keys():
			if not key in visited:
				queue.push(key)
		while queue.get_size() > 0:
			curr_vertex = self.get_vertex(queue.pop())
			while curr_vertex != None and curr_vertex.get_data() in visited:
				curr_vertex = self.get_vertex(queue.pop())
			if curr_vertex == None:
				break
			visited.append(curr_vertex.get_data())
			for key in curr_vertex.get_edges().keys():
				if not key in visited:
					queue.push(key)

		return visited

	def __str__(self):
		return str(self.bft())

if __name__ == '__main__':
	graph = Graph()
	graph.sample_graph()
	print graph
