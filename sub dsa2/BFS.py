#!usr/bin/env/python3

import queue

graph = {'Amin': {'Wasim', 'Nick', 'Mike'},
         'Wasim': {'Imran', 'Amin'},
         'Imran': {'Wasim', 'Faras'},
         'Faras': {'Imran'},
         'Mike': {'Amin'},
         'Nick': {'Amin'}}


def BFS(graph, start):
    visited = []  # this contains all visited vertices
    queue = [start]  # what we want to search for

    while queue:
        node = queue.pop(0)  # initial starting point
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]  # finding the neigbours of the initial node
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


print(BFS(graph, 'Amin'))
