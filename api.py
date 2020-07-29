
import json
​
baseurl = 'https://api.upcitemdb.com/prod/trial/lookup?'
parameters = {'upc':'0012993441012'}
response = requests.get(baseurl, params = parameters)
#print(response.url)
contents = response.content
info = json.loads(contents)
#print(type(info))
#print(info)
item = info['items']
iteminfo = item[0]
title = iteminfo['title']
brand = iteminfo['brand']
#print(title)
#print(brand)
