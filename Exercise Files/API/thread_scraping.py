import requests
from bs4 import BeautifulSoup as BS
from threading import Thread
from time import sleep

class Pages(Thread):
    def run(self):
        
        url = 'https://www.melcomonline.com/catalogsearch/result/?cat=1276&q=mobile%20phones'
        page = requests.get(url)
        soup = BS(page.content, 'lxml')
        titles = soup.find('ol', class_='products list items product-items')
        title = titles.find_all('a', class_='product-item-link', limit=24)
​
        for item in title:
            print(item.get_text())
            sleep(2)
class Page_price(Thread):
​
        def run(self):
            
            url = 'https://www.melcomonline.com/catalogsearch/result/?cat=1276&q=mobile%20phones'
            page = requests.get(url)
            soup = BS(page.content, 'lxml')
            titles = soup.find('ol', class_='products list items product-items')
            prices = titles.find_all('span', class_='price', limit=24)
            for item in prices:
            	print(item.get_text())
            	sleep(2)


    
    
c1 = Pages()
c2 = Page_price()
c1.start()
sleep(2)
c2.start()
c1.join()
sleep(2)
c2.join()
