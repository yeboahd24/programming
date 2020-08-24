class Node(object):
	"""The Node for the circular linked list.
	params: data, link."""
	def __init__(self, data):
		self.data = data
		self.link = None

class Circular_Linked(object):
	def __init__(self):
		self.last = None

	def displaying_list_items(self):
		if self.last.link == None:
			print("List is empty\n")
			return
		p = last.link # pointing to the last referrence

		while True:
			print(p.data, ' ', end='')
			p = p.link
			if p == self.last.link:
				break
		print()

	def inserting_beginning(self, data):
		temp = Node(data):
		temp.link = self.last.link
		self.last.link = temp

	def inserting_empty_list(self, data):
		temp = Node(data):
		self.last = temp
		self.last.link = self.last

	def insert_end_list(self, data):
		temp = Node(data):
		temp.link = self.last.link
		self.last.link = temp
		self.last = temp


