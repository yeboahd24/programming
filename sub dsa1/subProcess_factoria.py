#!usr/bin/env/python3


"""In this implementation, we have three parameters. n, as before, is the number
whose factorial we’re computing. i is a simple variable that starts at 1 and
increments by one in each successive call until it reaches n. Finally, product is
the variable in which we store the calculation as we keep multiplying each
successive number. We keep passing the product to the successive call so we
can keep track of it as we go.
"""
def factorial(n, i=1, product=1):
	# i = index, n = number
	if i > n:
		return product
	return factorial(n, i+1, product * i)

# print(factorial(6))


# subproblem
def fact(num):
	if num <= 1:
		return num

	return num * fact(num - 1) 

print(fact(5)*6) # This also gives factorial of 6 which is 720