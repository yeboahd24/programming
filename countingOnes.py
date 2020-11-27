#!usr/bin/env/python3

#complexity: O(N)
def count_ones(array):
	count = 0
	#iterating
	for value in array:
		if value == 1:
			count += 1
	return count


# Test Case:
data = [1, 0, 1, 0, 1]
print(count_ones(data))