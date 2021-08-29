import requests
from bs4 import BeautifulSoup

def get_capital(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    capital_class = soup.find("td", class_="infobox-data")
    capital = capital_class.find("a").text.strip()
    return capital