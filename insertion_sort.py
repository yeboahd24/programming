#!usr/bin/env/python3
# Complexity: O(N^2)
"""
High Level Description:
For every element in the given list, find its correct index by iterating
backwards and finding a slot. This forms a sorted array.
Time Complexity:
Every element is visited, which contributes O(n). Swapping backwards takes
O(n/2) time on average, meaning that the total complexity is O(n^2)
"""

def insertion_sort(array):
	array_length = len(array)
	for index in range(1, array_length):
		temp_value = array[index] # temporary value
		position = index - 1 # left side
		while position >= 0:
			if array[position] > temp_value:
				array[position + 1] = array[position]
				position = position - 1
			else:
				break
			array[position + 1] = temp_value
	return array


# Test Case
data = [9, 7, 6, 4, 2]
# print(insertion_sort(data))
			


def insertion_sort1(lst):
    for i in range(1,len(lst)):
        while(i > 0 and lst[i] < lst[i - 1]):
            lst[i], lst[i - 1] = lst[i -  1], lst[i]
            i -= 1
    return lst

test_data  = [5,9,4,27,3,6]
print(insertion_sort1(test_data))