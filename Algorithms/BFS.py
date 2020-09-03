from  collections import deque

'''This script search for mango seller my hash tables,'''

graph = {}
graph['you'] = ['parrot', 'linux', 'java']
graph['parrot'] = ['python', 'monty']
graph['linux'] = ['ghat']
graph['java'] = ['parrot']
graph['python'] = ['jacenta']
graph['monty'] = []
graph['ghat'] = []
graph['parrot'] = []
graph['jacenta'] = []


def person_is_seller(name):
	'''This function search for name of the seller
	in the graph.'''
	return name[-1] == 'x'  # Search names that ends with x.


def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []  # This keep track of searched persons

	while  search_queue:
		person = search_queue.popleft()
		if not person in searched:  # If person is not searched
			if person_is_seller(person):
				print(person + ' is a mango seller!.')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)  # Marks this as searched
	return False

print(search('you'))