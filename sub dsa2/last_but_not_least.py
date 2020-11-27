#!usr/bin/env/python3
"""This algorithm returns the value before the last value
	Eg: [1, 2, 3, 4, 5] = 4
"""

def last_but_not_least(array):
	size = len(array) - 1

	for i in range(len(array)-1):
		return array[size - 1]

data = [1, 2, 3, 4, 5]
print(last_but_not_least(data)) # 4