#!usr/bin/env/python3


def consecutive_sum(N):
	ans = 0
	i = 1
	while N > 0:
		N-=1
		ans+=(N % i == 0)
		i+=1
	return ans 

# print(consecutive_sum(2)) #4


#


def counsecutive(N):
	res = 0
	n = 0
	while True:
		top = N - (n *n + n)/2
		if(top <= 0):
			break
		if(top % (n + 1) == 0):
			res += 1
		n += 1
	return res

print(counsecutive(2))