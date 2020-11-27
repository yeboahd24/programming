#!usr/bin/env/python3
#complexity: O(N)
def mark_iventory(clothing_item):
	collections = []
	for cloth in clothing_item:
		# For sizes 1 through 5 (Python ranges go UP TO second
		# number, but do not include it):
		for item in range(1, 6):
			collections.append(cloth +' Size: ' + str(item))
	return collections

#Test Case
data = ["Purple Shirt", "Green Shirt"]
print(mark_iventory(data))
