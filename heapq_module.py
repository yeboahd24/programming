# largest and smallest items in a collection

import heapq

nums = [1,2,4,89,56,34,6,24,80]

largest = heapq.nlargest(2, nums) # finding 2 largest numbers
# print(largest)

smallest = heapq.nsmallest(2, nums) # finding 2 smallest numbers
# print(smallest)

peoples = [
	{'firstname': 'Johna', 'lastname': 'Doe', 'age': 30},
	{'firstname': 'Jane', 'lastname': 'Doe', 'age': 37},
	{'firstname': 'Janie', 'lastname':'Doe', 'age': 36},
	{'firstname': 'Jackelyn', 'lastname': 'Roe', 'age': 24},
	{'firstname': 'Joyce', 'lastname': 'Doe', 'age': 30},
	{'firstname': 'Linux', 'lastname': 'Doe', 'age': 68},
	{'firstname': 'Parrot', 'lastname': 'Pygmalion', 'age': 39}



]

oldest = heapq.nlargest(2, peoples, key=lambda x: x['age'])
youngest = heapq.nsmallest(2, peoples, key=lambda  x: x['age'])  # Note the heapq takes an optional parameter key.

numbers = [8,90,5,1,9,2]

heapq.heapify(numbers) # The heapify push the smaellest element to the first position.
# print(numbers)

