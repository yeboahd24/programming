#!usr/bin/env/python3

from itertools import combinations
def passwordCracker(string, num): # O(2^N)
	pos = list(combinations(string, num))
	for i in pos:
		print(''.join(i))
	
#TestCase:
data = 'linux'
num = 3
print(passwordCracker(data, num))




		

		

		
		