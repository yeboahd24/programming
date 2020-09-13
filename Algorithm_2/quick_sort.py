def quickSort(array):
	'''This function takes array and sort them
	in a recursive manner
	time complexity O(nlogn).
	This sort in ascending order.'''
	if len(array) < 2:
		return array # This is the base case.

	else:
		pivot = array[0] # This item we use the compare, which if the first index.
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]

	return quickSort(less) + [pivot] + quickSort(greater)  # The recursive function.


my_list = [5,9,1,6,8]
print(quickSort(my_list))

