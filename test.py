import requests 
from bs4 import BeautifulSoup

URL = 'https://www.coindesk.com/price/bitcoin'
website = requests.get(URL)
results = BeautifulSoup(website.content, 'html.parser')

price = results.find_all('div', class_='price-large')
for i in price:
    print(i.text.strip())
