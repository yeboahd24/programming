graph = {'Amin':{'Wasim', 'Nick', 'Mike'},
		'Wasim': {'Imran', 'Amin'},
		'Imran': {'Wasim', 'Faras'},
		'Faras': {'Imran'},
		'Mike': {'Amin'},
		'Nick': {'Amin'}}

def DFS(graph, start, visited=None):
	'''In DFS we will go in depth also we used stack'''
	if visited is None:
		visited = set() # to get unique vertices
	visited.add(start)
	print(start)

	for next in graph[start] - visited:
		DFS(graph, next, visited)
	return visited

print(DFS(graph, 'Amin'))