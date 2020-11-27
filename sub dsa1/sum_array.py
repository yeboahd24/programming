#!usr/bin/env/python3

"""A “100-Sum Array” meets the following criteria:
• Its first and last numbers add up to 100.
• Its second and second-to-last numbers add up to 100.
• Its third and third-to-last numbers add up to 100, and so on."""

def one_hundred_sum(array):
	first_index = 0
	last_index = len(array) - 1
	while first_index < last_index//2:
		if(array[first_index] + array[last_index] !=100):
			return False
		first_index+=1
		last_index-=1
	return True


#Test Case:
data = [10, 50, 80, 90] # True
# print(one_hundred_sum(data))

def two_consecutive_sum(array, n): # find the two consecutive sum that at up to n
	b = len(array) - 1

	for i in range(b):
		if(array[i]+array[i+1] == n):
			return array[i], array[i+1]
	return None
			

data = [1, 2, 3, 4, 5]
# print(two_consecutive_sum(data, 9))


def two_consecutive_sum_1(array, n): 
	# any num plus last index that sum up to n
	index = len(array) - 1
	for i in range(index):
		if(array[i] + array[index] == n):
			return array[i], array[index]
	return None

#Test Case
data = [1, 2, 3, 4, 5]
n = 9
print(two_consecutive_sum_1(data, n))