#!/usr/bin/env python3
""" Check how many students are in the class. """

from time import sleep
from concurrent.futures import ThreadPoolExecutor

def how_many_student():
	print('Linux is counting the number of students.\n')
	sleep(5)
	num_student = 40
	return f'The number of students in the class is: {num_student}'

if __name__ == '__main__':
	print('Parrot asks Linux how many students are in the class.')
	with ThreadPoolExecutor() as pool:
		future = pool.submit(how_many_student)
		print('Parrot is doing other things while Linux is counting.')
		print('Linux response with', future.result())
