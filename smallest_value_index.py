#!usr/bin/env/python3
# By Dominic(Python Developer)
# Complexity: O(N^2)
def smallest_index(array):
	smallest_value = array[0] # Default smallest value
	smallest_index = 0 # Default index
	array_length = len(array) # length of the array
	for value in range(1, array_length):
		if array[value] < smallest_value:
			smallest_index = value
	return smallest_index # return index of the smallest



data = [10, 60, 43, 20, 7]
# print(selection_sort(data))


