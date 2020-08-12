# nums = [2, 7, 11, 15]
# target = 9
# nums = [2,7,9,4]
# target = 9

# lookup = {}
# for index, item in enumerate(nums):
#     if(target - item) in lookup:
#         print([lookup[target-item],index])
#     else:
#         lookup[item] = index



# sum of consecutive numbers
# n =[0,1,1,0,1,0]
# x =[]
# for i in n:
# 	n[3],n[4] = 1,0
# 	if i >=1:
# 		x.append(i)
# print(sum(x))

#maximum number

numbers = [10,2,65,90]
maxs = numbers[0]

for nums in numbers:
	if nums > maxs:
		maxs = nums
print(nums)

