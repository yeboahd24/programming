#!usr/bin/env/python3
# By Dominic(Python Developer)
# Complexity: O(N^2)
def has_duplicate(arrays):
	# first iterating
	array_size = len(arrays)
	for first in range(array_size):
		# secod iterating
		for second in range(array_size):
			"""Checking if first item is not equal to second item, then if first index is equal to second index"""
			if(first != second and arrays[first] == arrays[second]):
				return True
	return False

# Test Case
data = [1, 3, 1] # True
# print(has_duplicate(data))


def has_duplicate1(arrays):
	existing_value = {}
	for i in range(len(arrays)):
		if not arrays[i] in existing_value:
			existing_value[i] = True
		else:
			return True
		

	return False


#Test case
data = [1, 3, 1]
# print(has_duplicate1(data))




		