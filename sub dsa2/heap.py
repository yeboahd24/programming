#!usr/bin/env/python3

class Heap(object):

	def __init__(self, data):
		self.data = []

	def root_node(self):
		# this the first inde of the array
		return self.data[0]

	def last_node(self):
		# last node
		return self.data[-1]


	def left_child_index(self, index):
		return (index * 2) + 1

	def right_child_index(self, index):
		return (index * 2) + 2


	def parent_index(self, index):
		return (index - 1)//2


	def insert(self, value):
		# Turn value into last node by inserting it at the end of the array:
		self.data.append(value)
		# Keep track of the index of the newly inserted node:
		new_node_index = len(self.data) - 1
		# The following loop executes the "trickle up" algorithm.
		# If the new node is not in the root position,
		# and it's greater than its parent node:
		while new_node_index > 0 and self.data[new_node_index] > self.data[parent_index(new_node_index)]:
			# Swap the new node with the parent node:
			self.data[parent_index(new_node_index)], self.data[new_node_index] = \
			self.data[new_node_index], self.data[parent_index(new_node_index)]

			# Update the index of the new node:
			new_node_index = parent_index(new_node_index)


	def delete(self):
		# We only ever delete the root node from a heap, so we
		# pop the last node from the array and make it the root node:
		self.data[0] = self.data.pop()
		trickle_node_index = 0
		# The following loop executes the "trickle down" algorithm:
		# We run the loop as long as the trickle node has a child
		# that is greater than it:
		while has_greater_child(trickle_node_index):
			# Save larger child index in variable:
			larger_child_index = calculate_larger_child_index(trickle_node_index)
			# Swap the trickle node with its larger child:
			self.data[trickle_node_index], self.data[larger_child_index] = \
			self.data[larger_child_index], self.data[trickle_node_index]


	def has_greater_child(index):
		# We check whether the node at index has left and right
		# children and if either of those children are greater
		# than the node at index:
		(self.data[left_child_index(index)] and \
		self.data[left_child_index(index)] > self.data[index]) or \
		(self.data[right_child_index(index)] and \
		self.data[right_child_index(index)] > self.data[index])


	def calculate_larger_child_index(index):
		# If there is no right child:
		if not self.data[right_child_index(index)]:
			# Return left child index:
			return left_child_index(index)

		# If right child value is greater than left child value:
		if self.data[right_child_index(index)] > self.data[left_child_index(index)]:
			# Return right child index:
			return right_child_index(index)
		# If the left child value is greater or equal to right child:
		# Return the left child index:
		else:
			return left_child_index(index)



		









