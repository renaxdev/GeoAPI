def get_btc():
    URL = 'https://www.coindesk.com/price/bitcoin'
    website = requests.get(URL)
    results = BeautifulSoup(website.content, 'html.parser')

    price_tag = results.find_all('div', class_='price-large')
    for i in price_tag:
        price = i.text.strip()

    return price