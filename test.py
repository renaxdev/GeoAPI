import requests 
from bs4 import BeautifulSoup
def get():
    URL = 'https://www.coindesk.com/price/bitcoin'
    website = requests.get(URL)
    results = BeautifulSoup(website.content, 'html.parser')

    price = results.find_all('div', class_='price-large')
    for i in price:
        price = i.text.strip()
    
    return price

print(get())
