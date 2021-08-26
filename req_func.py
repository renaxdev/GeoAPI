def get_btc():
    URL = 'https://www.coindesk.com/price/bitcoin'
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',}) #Sonst werden die Requests abgelehnt
    req = requests.get(URL)

    results = BeautifulSoup(req.content, 'html.parser')

    price = results.find_all('div', class_='price-large')
    for i in price:
        price = i.text.strip()
    
    return price