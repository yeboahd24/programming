class Node:
	'''Creating Node for the Stack.'''
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.size = 0

	def pushData(self, data):
		'''Pushing data to the Stack.'''
		node = Node(data)
		if self.top:
			node.next = self.top
			self.top = node
		else:
			self.top = node
			self.size+=1

	def popData(self):
		'''Removing data from the Stack.'''
		if self.top:
			data = self.top.data
			self.size-=1
			if self.top.next:
				self.top = self.top.next
			else:
				self.top = None
		else:
			return data

	def peek(self):
		'''This return the last item in the stack.'''
		if self.top:
			return self.top.data
		else:
			return None


s = Stack()
s.pushData(1)
s.pushData(2)
s.pushData(3)
print(s.peek())