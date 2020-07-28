class Node:
	'''Node structure for the list.'''
	def __init__(self, data):
		self.data = data
		self.next = None



class Linked:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0


	def append(self, data):
		node = Node(data)
		if self.head:
			self.head.next = node
			self.head = node
		else:
			self.head = node
			self.tail = node
			self.size+=1

	def listSize(self):
		count = 0
		current = self.tail
		while current:
			count+=1
			current = current.next
		return f'The size of the LinkedList is: {count}'

			

	def empty(self):
		return self.head is None

		
		# O(1)
	def iter(self):
		current = self.tail
		while current:
			val = current.data
			current = current.next
			yield val

	def __str__(self):
		return f'current Linked: {self.head}'


	def search(self, data):
		for node in self.iter():
			if data == node:
				return True
		return False

	def clear(self):
		'''clearing the entire list.'''
		self.head = None
		self.tail = None

	def delete(self, data):
		current = self.head
		prev = self.tail

		while current:
			if current.data == data:
				if current == self.tail:
					self.tail = current.next
				else:	
					prev.next = current.next
				self.size-=1
				return

			prev = current
			current = current.next




l = Linked()
l.append(1)
l.append(2)
l.append(3)

# print(l.empty())


# O(N)
# current = l.tail
# while current:
# 	print(current.data)
# 	current = current.next




print(l.listSize())

for i in l.iter():
	print(i)

print(l.search(1))


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3

# Traversing through the list.
# current = n1
# while current:
# 	print(current.data)
# 	current = current.next

