import timeit

def plainlist(n=1000000):
	my_list = []
	for i in range(n):
		if i % 5 == 0:
			my_list.append(i)
	return my_list

def listcomp(n=1000000):
	my_list = [i for i in range(n) if i % 5 == 0]
	return my_list

def generator_yield(n=1000000):
	for i in range(n):
		if i % 5 == 0:
			yield i
def generator(n=1000000):
	my_gen = (i for i in range(n) if i % 5 == 0)
	return my_gen


def test_plainlist(plain_list):
	for i in plainlist():
		pass

def test_listcomp(listcompr):
	for i in listcompr():
		pass

def test_generator_yield(generator_yield):
	for i in generator_yield():
		pass

print('plain_list:  ', end='')
%timeit test_plainlist(plainlist)
print('\nlistcompr:  ', end='')
%timeit test_listcomp(listcomp)
print('\ngenerator:  ', end='')
%timeit test_generator_yield(generator)
print('\ntest_generator_yield:  ', end='')
%timeit test_generator_yield(generator_yield)

