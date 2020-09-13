def bubbleSort(lyst):
	"""list(lyst)-->int
	>>> bubbleSort([9,8,3,6])
	[3,6,8,9]
	"""

	end = len(lyst) - 1

	while end != 0:
		for i in range(end):
			if lyst[i] > lyst[i + 1]:
				lyst[i], lyst[i + 1] = lyst[i + 1], lyst[i]
		end = end - 1
	return lyst



x = [9, 8, 3, 6]
print(bubbleSort(x))