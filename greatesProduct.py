#!usr/bin/env/python3
# By Dominic(Python Developer)
# Complexity: O(N^2)

def greatestProduct(array):
	_DEFAULT = array[0] * array[1] # Assume for now that i is the greatest:
	for i, iVal in enumerate(array, start=0):
		for j, jVal in enumerate(array, start=0): 
		# If we find another value that is greater than i, i is not the greatest:
			if(i != j and iVal * jVal > _DEFAULT):
				_DEFAULT = iVal * jVal
	return _DEFAULT


data = [1, 2, 3, 4, 5] # 20
print(greatestProduct(data))



def greatestNum(array):
	#iterating
	for i in array:
		is_greatest = True # assumption
		for j in array:
			if j > i:
				is_greatest = False

		if is_greatest:
			return i

data = [1, 2, 3, 4, 5]
print(greatestNum(data)) # 5