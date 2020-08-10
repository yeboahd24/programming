class Node:
	'''The Node for the Doubly Linked List'''
	def __init__(self, data=None,prev=None,nex=None):
		self.data = data
		self.prev = prev
		self.nex = nex 
		


class DLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, data):
		node = Node(data, None, None)
		if self.head is None:
			self.head = node
			self.tail = self.head
		else:
			node.prev = self.tail
			self.tail.prev = self.tail
			self.tail = node
			self.size+=1

	def delete(self, data):
		current = self.tail
		node_deleted = False

		if current is None:
			node_deleted = False
		elif current.data == data:
			self.head = current.nex
			self.head.prev = None
			node_deleted = True
		elif self.tail.data == data:
			self.tail = tail.prev
			tail.prev = None
			node_deleted = True

		else:
			while current:
				if current.data == data:
					current.prev.nex = current.nex
					current.nex.prev = current.prev
				node_deleted = True
				if node_deleted:
					self.size-=1





		

	

