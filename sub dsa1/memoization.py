#!usr/bin/env/python3

#memoization: making an object hashable

def fibonacci(number, memoization={}):
	if number <= 1:
		return number

	# Check the hash table (called memo) to see whether fib(n)
	# was already computed or not:
	if not memoization.get(number):
		memoization[number] =   fibonacci(number - 1, memoization) + fibonacci(number - 2, memoization)

	return memoization[number]



#Test Case:
data = 5
print(fibonacci(data))