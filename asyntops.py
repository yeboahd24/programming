def sequentialSearch(target, lyst):
	"""Returns the position of the target item if found,
	or -1 otherwise"""
	position = 0

	while position < len(lyst):
		if target == lyst[position]:
			return f'{target} is found in the position: {position}'
		position+=1

	return -1

data = [1,2,5,7,8]
test = sequentialSearch(4, data)
# print(test)


def binarySearch(target, sortedlyst):
	left = 0
	right = len(sortedlyst)-1

	while left <= right:
		midpoint = (left + right)//2
		if target == sortedlyst[midpoint]:
			return midpoint
		elif target < sortedlyst[midpoint]:
			right = midpoint - 1
		else:
			left = midpoint + 1
	return -1

x = [1,2,3,4,5,6]
print(binarySearch(5, x))


