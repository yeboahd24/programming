import math, random

# function to generate OTP

def generateOTP():
	# Declare a digit variable to store digits
	digit = '0123456789'
	OTP = ''

	# length of OTP can be changed
	for i in range(4):
		OTP+=digit[math.floor(random.random() *10)]
	return OTP

	# Derive code

if __name__=='__main__':
	print('Your 4 digit OTP is: ', generateOTP())