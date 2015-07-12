# HashTable for words
class HashTable:
	def __init__(self):
		self.table = [[] for _ in range(27)]
		self.size = 0

	def add(self, key, value):
		if self.get(key) is not None:
			return False
		entry = (key, value)
		bucket = ord(key[:1])
		if bucket > 96:
			bucket -= 97
		else:
			bucket -= 65
		if bucket < 0 or bucket > 26:
			bucket = 26
		self.table[bucket].append(entry)
		return True

	def get(self, key):
		bucket = ord(key[:1])
		if bucket > 96:
			bucket -= 97
		else:
			bucket -= 65
		if bucket < 0 or bucket > 26:
			bucket = 26
		for entry in self.table[bucket]:
			if entry[0] == key:
				return entry[1]
		return None

if __name__ == '__main__':
	table = HashTable()
	table.add("Apples", 1)
	table.add("Bannanas", 2)
	table.add("Cherries", 3)
	table.add(" ", 0)
	print table.get("Apples")
	print table.get("Bannanas")
	print table.get("Cherries")
	print table.get(" ")