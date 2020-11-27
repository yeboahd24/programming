#!usr/bin/env/python3

def twoSum(array):
	array_length = len(array)
	for i in range(array_length):
		for j in range(array_length):
			if(i!=j and array[i] + array[j]):
				return True
	return False


# Test Case
data = [3, 5, 6, 4]
print(twoSum(data))