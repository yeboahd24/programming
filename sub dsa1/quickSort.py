#!usr/bin/env/python3

def quickSort(array):
	#base case
	if len(array) < 2:
		return array

	pivot = array[0] # pivot to be compare
	less = [i for i in array[1:] if i <= pivot]  # less  values
	great = [i for i in array[1:] if i > pivot]

	return quickSort(less) + [pivot] + quickSort(great)


#Test Case
data = [5, 4, 3, 2, 1]
print(quickSort(data))
