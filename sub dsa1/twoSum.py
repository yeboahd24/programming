#!usr/bin/env/python3
#Complexity: O(N)
def twoNumberProduct(array1, array2):
	all_products = []
	for i in range(len(array1)):
		for j in range(len(array2)):
			all_products.append(array1[i] * array2[j])
	return all_products


#Test Case:
data = [10, 20, 30, 40]
data1 = [50, 60, 70, 80]
print(twoNumberProduct(data, data1))