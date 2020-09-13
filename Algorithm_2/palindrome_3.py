def is_palindrome(s):
	"""  Return True if and only is a palindrome
		--> str(s) --> bool
		is_palindrome('noon')
		>>> True
		is_palindrome('racecar')
		>>> True
		is_palindrome('dented')
		>>> False
	"""

	# first index of s
	i = 0 

	j = len(s) - 1  # the last index of s

	while i < j and s[i] == s[j]:
		i = i + 1
		j = j - 1

	return j <= i

print(is_palindrome('noon'))
print(is_palindrome('racecar'))
print(is_palindrome('dented'))
