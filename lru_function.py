import time
import functools

def func(x):
	'''This code runs without
	the lru_funcion'''
	time.sleep(1)
	print(f'Heavey operation for {x}')
	return x *10

# print('Func returned:', func(1))
# print('Func returned:', func(1))


@functools.lru_cache

def func(x):
	'''code with lru'''
	time.sleep(1)
	print(f'Heavey operation for {x}')
	return x *10

print('Func returned:', func(1))
print('Func returned:', func(1))
print('Func returned:', func(2))

