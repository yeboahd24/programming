#!usr/bin/env/python3

# Weighted graph is a graph with distance

class WeightedGraph(object):
	def __init__(self, value):
		self.value = value
		self.adjacent_vertices = {}

	def add_adjacent_vertex(self, vertex, weight):
		self.adjacent_vertices[vertex] = weight


class City(object):
	def __init__(self, name):
		self.name = name
		self.route = {}

	def add_route(self, city, price):
		self.route[city] = price


	def dijkstra_shortest_path(starting_city, final_destination):
		cheapest_prices_table = {}
		cheapest_previous_stopover_city_table = {}
		# To keep our code simple, we'll use a basic array to keep track of
		# the known cities we haven't yet visited:
		unvisited_cities = []
		# We keep track of the cities we've visited using a hash table.
		# We could have used an array, but since we'll be doing lookups,
		# a hash table is more efficient:
		visited_cities = {}
		# We add the starting city's name as the first key inside the
		# cheapest_prices_table. It has a value of 0, since it costs nothing
		# to get there:
		cheapest_prices_table[starting_city.name] = 0
		current_city = starting_city

		# This loop is the core of the algorithm. It runs as long as we can
		# visit a city that we haven't visited yet:
		while current_city:
		# We add the current_city's name to the visited_cities hash to record
		# that we've officially visited it. We also remove it from the list
		# of unvisited cities:
			visited_cities[current_city.name] = True
			unvisited_cities.delete(current_city)
		# We iterate over each of the current_city's adjacent cities:
		for adjacent_city, price in self.route:
			# If we've discovered a new city,
			# we add it to the list of unvisited_cities:
			unvisited_cities.append(adjacent_city)
		visited_cities[adjacent_city.name]


		# We calculate the price of getting from the STARTING city to the
		# ADJACENT city using the CURRENT city as the second-to-last stop:
		price_through_current_city = cheapest_prices_table[current_city.name] + price
		# If the price from the STARTING city to the ADJACENT city is
		# the cheapest one we've found so far...
		if not cheapest_prices_table[adjacent_city.name] and \
		price_through_current_city < cheapest_prices_table[adjacent_city.name]:

		# ... we update our two tables:
			cheapest_prices_table[adjacent_city.name] = price_through_current_city
			cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

		# We visit our next unvisited city. We choose the one that is cheapest
		# to get to from the STARTING city:
		current_city = min(unvisited_cities.city)
		cheapest_prices_table[city.name]

		# We have completed the core algorithm. At this point, the
		# cheapest_prices_table contains all the cheapest prices to get to each
		# city from the starting city. However, to calculate the precise path
		# to take from our starting city to our final destination,
		# we need to move on.
		# We'll build the shortest path using a simple array:
		shortest_path = []
		# To construct the shortest path, we need to work backwards from our
		# final destination. So, we begin with the final destination as our
		# current_city_name:
		current_city_name = final_destination.name
		# We loop until we reach our starting city:
		while current_city_name != starting_city.name:
		# We add each current_city_name we encounter to the shortest path array:
			shortest_path.append(current_city_name)
		# We use the cheapest_previous_stopover_city_table to follow each city
		# to its previous stopover city:
		current_city_name = cheapest_previous_stopover_city_table[current_city_name]
		# We cap things off by adding the starting city to the shortest path:
		shortest_path.append(starting_city.name)
		# We reverse the output so we can see the path from beginning to end:
		return shortest_path.reverse




dallas = WeightedGraph("Dallas")
toronto = WeightedGraph("Toronto")

dallas.add_adjacent_vertex(toronto, 138)
toronto.add_adjacent_vertex(dallas, 216)


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)