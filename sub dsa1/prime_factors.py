#!usr/bin/env/python3

def get_prime_factors(N):
	factors = list()
	divisor = 2
	while (divisor <= N):
		if(N % divisor) == 0:
			factors.append(divisor)
			N = N/divisor
		else:
			divisor+=1
	return factors

#Test Case
data = 24
print(get_prime_factors(data))
		
