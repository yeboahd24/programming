class Node:
	def __init__(self, data):
		self.data = data
		self.link = None


class SLL:
	def __init__(self):
		self.head = None
		


	def insert_empty(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node

	def insert_beginning(self, data):
		node = Node(data)
		node.link = self.head
		self.head = node

	def insert_end(self, data):
		node = Node(data)
		current = self.head
		if current is None:
			self.head = node
			return
		while current.link is not None:
			current = current.link
		current.link = node

	def get_last_node_ref(self):
		current = self.head
		while current.link is not None:
			current = current.link


	def size(self):
		current = self.head
		size = 0
		while current is not None:
			size+=1
			current = current.link
		return size

	def search(self, value):
		current = self.head
		while current.data != value:
			current = current.link
			return True
		return False

	def get_last_item(self):
		current = self.head
		while current.link.data is not None:
			current = current.data
			return current

	def delete_first_node(self):
		self.head = self.head.link


s = SLL()
s.insert_beginning(1)
s.insert_beginning(2)
s.insert_beginning(3)


























