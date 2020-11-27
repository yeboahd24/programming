#!usr/bin/env/python3

"""A palindrome is a word or phrase that reads the same both forward and
	backward. Some examples include “racecar,” “kayak,” and “deified.”
# """

# def palindrome_checker(string): # O(N)
# 	#Start the leftIndex at index 0:
# 	leftIndex = 0
# 	#Start rightIndex at last index of array:
# 	rightIndex = len(string) - 1
# 	mid = len(string)//2
# 	#Iterate until leftIndex reaches the middle of the array:
# 	while (leftIndex < mid):
# 		if(string[leftIndex] != string[rightIndex]):
# 			return False

# 		leftIndex = leftIndex + 1
# 		rightIndex = rightIndex - 1
	# return True
		

#Test Case:
# data = ['racecar']
# print(palindrome_checker(data))


def reverse(x):
    num1=str(x)[::-1]
    if num1==str(x):
        return True
    return False
print(reverse('racecar'))