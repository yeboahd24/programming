#!usr/bin/env/python3

"""Let’s say we’re writing a function that accepts an array of strings
and returns an array of those strings in ALL CAPS. For example, the function
would accept an array like ["tuvi", "leah", "shaya", "rami"] and return ["TUVI", "LEAH",
"SHAYA", "RAMI"]."""


# time complexity: O(N)
# space complexity: O(N)
def upperCase(array):
	new_array = []
	for i in range(len(array)):
		new_array.append(array[i].upper())
	return(new_array)
	

#time O(1)
#space O(1)
def upperCase2(array):
	for i in range(len(array)):
		array[i] = array[i].upper()
	return array

data = ['tuvi', 'leah', 'shaya', 'rami']
print(upperCase2(data))