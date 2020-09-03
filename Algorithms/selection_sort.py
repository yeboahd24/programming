def findSmallest(arr):
	'''This fucntion find the samllest arrays in order.
	params: arr = array'''
	smallest = arr[0] # The value of the first element.
	smallest_index = 0 # The index of the smallest value.

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index



def selectionSort(arr):
	'''Passing the findSmallest function here
	complexity: O(n^2)
	average: O(n log n)'''
	newArr = []

	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

my_list = [5,3,7,9,11,]
print(selectionSort(my_list))