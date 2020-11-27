#!usr/bin/env/python3

# Code by Dominic(Python Developer)
# Binary search is only done if the array is odered
# Complexity: O(logN)


def binary_search(array_, value):
	lower_bound = 0  # first index of the array
	upper_bound = (len(array_) - 1) # last index of the array

	while lower_bound <= upper_bound:
		midpoint = (upper_bound + lower_bound)//2  # middle number of the array
		value_at_midpoint = array_[midpoint]

		if value == value_at_midpoint:
			return value

		elif value > value_at_midpoint:
			lower_bound = midpoint + 1

		elif value < value_at_midpoint:
			upper_bound = midpoint - 1

	return None


# Test Case
data = [1, 2, 3, 4, 5]
print(binary_search(data, 5))

		
		

