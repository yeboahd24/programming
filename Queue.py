class Queue:
	"""The Queue Structure"""
	def __init__(self):
		self.queue = []

	def isempty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		value = self.enqueue[0]
		del self.enqueue[0]
		return value

	def peek(self):
		return self.queue[0]

	def size(self):
		return len(self.queue)


		