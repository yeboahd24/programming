#!usr/bin/env/python3
# Complexity: O(N)

def average_of_even_number(arrays):
	# The mean average of even numbers will be defined as the sum of
	# the even numbers divided by the count of even numbers, so we
	# keep track of both the sum and the count:
	sum_ = 0.0
	count_of_even_numbers = 0
	# We iterate through each number in the array, and if we encounter
	# an even number, we modify the sum and the count:
	for number in arrays:
		if number % 2 == 0:
			sum_+=number
			count_of_even_numbers +=1
	return sum_/count_of_even_numbers

# Test Case:
data = [1, 2, 3, 4, 5]
print(average_of_even_number(data))

