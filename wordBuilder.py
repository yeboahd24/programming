#!usr/bin/env/python3

# word builder is when for example ['a', 'b', 'c', 'd']
# generate something like,
# ]
# 'ab', 'ac', 'ad', 'ba', 'bc', 'bd',
# 'ca', 'cb', 'cd', 'da', 'db', 'dc'
# ]


def word_builder(strings): # O(N^2)
	collection = []
	strings_size = len(strings)
	for i in range(strings_size):
		for j in range(strings_size):
			if(i != j):
				collection.append(strings[i] + strings[j]) # combination of strings
	return collection

#Test Case
data = ['a', 'b', 'c', 'd']
# print(word_builder(data))


def word_builders(strings): # O(N^3) Cubic
	# this returns triple combinations
	collections = []
	strings_length = len(strings)
	for i in range(strings_length):
		for j in range(strings_length):
			for k in range(strings_length):
				if(i != j and j != k and i != k):
					collections.append(strings[i] + strings[j] + strings[k])
	return collections


#Test Case
data = ['a', 'b', 'c', 'd']
print(word_builders(data))