class Stack:
	'''Stack implentation using array'''
	def __init__(self):
		self.stack = []

	def stackEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)


s = Stack()
s.push(1)
s.push(2)

print(s.size())