#!usr/bin/env/python3

"""
    Queue is an abstract data structure, somewhat similar to Stacks.
    Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue)
    and the other is used to remove data (dequeue).
    Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first.

    """

# Simple One
class Queue(object):

	def __init__(self):
		self.data = [] # default

	def enqueue(self, element): # pushing
		self.data.append(element)

	def dequeue(self): # removing
		get = self.data[0]
		self.data = self.data[1:]
		return get



#Test Case:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue()) #1







class Queue(object):



    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def put(self, item):
        self.entries.append(item)
        self.length += 1

    def get(self):
        if self.length <= 0:
            return
        self.length -= 1
        de_queued = self.entries[self.front]
        self.entries = self.entries[1:]
        return de_queued

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def size(self):
        return self.length