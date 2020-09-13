# Restuarants names rating
name_to_rating = {
	'Gorgie Porgie': 87,
	'Queen St. Cafe': 82,
	'Dumplings R Us': 72,
	'Mexican Grill': 85,
	'Deep Fried Everything': 52
}

# Prices to foods
price_to_names = {
	'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
	'$$': ['Mexican Grill'],
	'$$$': ['Gorgie Porgie'],
	'$$$$': []
}

# foods serves by the restaurants
cuisine_to_names = {
	'Canadian': ['Gorgie Porgie'],
	'Pub Food': ['Gorgie Porgie', 'Deep Fried Everything'],
	'Mexican': ['Mexican Grill'],
	'Malaysia': ['Queen St. Cafe'],
	'Chinese': ['Dumplings R Us']
}


from operator import itemgetter
restaurants_data = {
	'name_to_rating': name_to_rating,
	'price_to_names': price_to_names,
	'cuisine_to_names': cuisine_to_names
	}

# x = sorted(restaurants_data['price_to_names'].items())
# print(restaurants_data['cuisine_to_names'])
# print(x)
# x=sorted(restaurants_data, key=itemgetter('name_to_rating'))
# print(x)

# def cuisines():
# 	return restaurants_data['cuisine_to_names']
# print(cuisines())
# def prices():
# 	return restaurants_data['price_to_names']

# def rating():
# 	return restaurants_data['name_to_rating']


