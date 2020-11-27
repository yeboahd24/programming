#!usr/bin/env/python

# This program double any value inside an array

def double_array(array, index=0):
	if index >=len(array):
		return
	array[index] *= 2

	double_array(array, index + 1)


#Test Case:
data = [1, 2, 3, 4, 5]
double_array(data)
print(data)