#!usr/bin/env/python

# Prime numbers
# Complexity: O(N) because it depends on the input number
# By Dominic(Python Developer)

def is_prime(numbers):
	#Iterating 
	for number in range(2, numbers):
		if numbers % number == 0:
			return False
	return True

#Test case
print(is_prime(6))
