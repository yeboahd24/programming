#!usr/bin/env/python3

# code by Dominic(Python Developer)
# liner search
# time complexity: O(N) that is worst case.

def linear_search(array_, value):
	for index, item in enumerate(array_, start=0):
		if item == value:
			return f'{value} is found at index: {index}'
	return f'{value}: not in array'  # if value does not exist
		

	

# Test Case
data = [1, 5, 8, 9, 4]
print(linear_search(data, 0))




		

