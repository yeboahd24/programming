#!usr/bin/env/python3

# finding the intersection of two arrays

def intersection(array_1, array_2):
	intersection_results = []
	# first iteration
	for i in range(len(array_1)):
		# second iteration
		for j in range(len(array_2)):
			if(array_1[i] == array_2[j]):
				intersection_results.append(array_1[i])
				break # meaning if there is no intersection

	return intersection_results


# Test Cass
arr1 = [3, 4, 5, 6]
arr2 = [7, 5, 4, 8]
print(intersection(arr1, arr2))
