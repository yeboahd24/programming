def binary_search(data, elem):
	'''The data is the ordered sequece
	and elem is the element we want to search,
	low is the initial index, high is the last
	index'''

	low = 0
	high = len(data)-1

	while low < high:
		middle = (low + high)//2

		if data[middle]==elem:
			return middle

		elif data[middle] > elem:
			high = middle-1

		else:
			low = middle+1
	return -1

b = [1,2,5,7,9]
print(binary_search(b, 5))


