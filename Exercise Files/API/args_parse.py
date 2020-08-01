# def foo(name):
# 	print(f'Your name is {name}')
	

# if __name__=='__main__':
# 	'''This store your argument in a list.'''
# 	import sys
# 	foo(sys.argv[0])



# def mult(x,y):
# 	return x*y

# def div(x,y):
# 	return x/y

# def math(func,x,y):
# 	'''Using function as an argument.'''
# 	result = func(x,y)
# 	return result

# print(math(mult, 2,4))

from functools import wraps
def deco(func):
	wraps(func)
	def wrap(a,b):
		if a<b:
			a,b=b,a
			return func(a,b)
		return func(a,b)
	return wrap


@deco
def add(x,y):
	return x/y

print(add(4,2))


