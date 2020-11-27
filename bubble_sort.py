#!usr/bin/env/python3
# Bubble Sort Algorithm
# It involve two steps, swaping and comparing
# By Dominic(Python Developer)
# Complexity: O(N^2) -> quadratic time
# O(N*N)-N

def bubble_sort(sequence):
	unsorted_list_index = len(sequence) - 1 # last index of the sequence
	sorted_ = False # default
	while not sorted_: # here becomes True now
		sorted_ = True
		for value in range(unsorted_list_index): # iterating through the last index
			if sequence[value] > sequence[value + 1]: # if first value is greater than the next value
				sorted_ = False
				sequence[value], sequence[value + 1] = sequence[value + 1], sequence[value]# value swaping
		unsorted_list_index = unsorted_list_index - 1 # decrementing

# Test Case
data =  [65, 55, 45, 35, 25, 15, 10]
bubble_sort(data)
print(data)
