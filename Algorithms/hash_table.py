cache = {} 
import requests

def get_page(url):
	'''This function take in parameter url and return it hash content.
	If not it search for it and store it.'''

	if cache.get(url):
		return cache[url] # This return the data in the hash table if present.
	else:
		data = requests.get(url)  # This search for the url data that is not in the hash table.
		cache[url] = data
		return data

if __name__ == '__main__':
	url = 'http://facebook.com/page'
	get_page(url)