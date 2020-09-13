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

	n = len(s)  # length of s.

	# comparing the first half of s to reverse the second half of.
	# omitting the middle character of odd-length string.

	return s[:n//2] == reverse_str(s[n - n // 2:])




def reverse_str(s):
	"""str(s)-->str
		return a reverse of str(s)

	 """
	rev = ''
	for char in s:
		rev = char + rev  # do not make make it rev = rev + char if you do all will return true.
	return rev

print(is_palindrome('noon'))
print(is_palindrome('racecar'))
print(is_palindrome('dented'))
