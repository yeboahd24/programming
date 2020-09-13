def binarySearch(lyst, target):
	'''Binary search algorithm used in sorted order.
	params:
	lyst: containing the list items.
	target: the value you are looking for.
	time complexity O(log)'''
	low = 0 # the first index of the lyst.
	high = len(lyst) - 1 # the highest index of the lyst.

	while low <= high:
		mid = (low + high)//2  # finding the middle number of the lyst.
		guess = lyst[mid]

		if guess == target:
			return mid
		if guess > target:
			high = mid - 1  # note if you make high = mid + 1 this will not work
		else:
			low = mid + 1  # do not change it to low = mid -1
	return None


# Testing field.

my_list = [1, 3, 5, 7, 9]

# print(binarySearch(my_list, 7))


# this is the worst case (linear time)

# target = 7
# for i,k in enumerate(my_list):
# 	if k == target:
# 		print(i)
# 		break



