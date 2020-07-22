import requests
from bs4 import BeautifulSoup



url = 'https://scrapingclub.com/exercise/list_basic/?page=2'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for item in items:
    cloth = item.find('h4', class_='card-title').get_text().strip()
    price = item.find('h5').get_text()
    all_items = f'item name: {cloth} item price: {price}'
    #print(all_items, end = '\n')
    count = count+1
    
urls =[]
pages = soup.find('ul', class_='pagination')
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.get_text()) if link.get_text().isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
#print(urls)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for item in items:
        cloth = item.find('h4', class_='card-title').get_text().strip()
        price = item.find('h5').get_text()
        all_items = f'item name: {cloth} items price {price}'
        print(all_items, end ='\n')
        count = count + 1

    
​
​





















