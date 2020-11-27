#!usr/bin/env/python3

def twoSumProduct(array):
	products = []
	for i in range(len(array)-1):
		j = i+1
		for j in range(len(array)):
			products.append(array[i] * array[j])
			
		

	return products

# Test Case:
data = [1, 2, 3, 4, 5]
print(twoSumProduct(data))
