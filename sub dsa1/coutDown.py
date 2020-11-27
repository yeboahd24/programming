#!usr/bin/env/python3

#This program Count for max to min

#simple iteration
def countDown(num):
	while num >=0:
		print(num)
		num = num - 1

# print(countDown(10))


#Recursive
def countDown1(nums):
	if nums >= 0: # base
		print(nums)
		countDown1(nums - 1)

# countDown1(10)

