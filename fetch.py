import requests
from bs4 import BeautifulSoup
import json

def get_capital(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    capital_class = soup.find("td", class_="infobox-data")
    capital = capital_class.find("a").text.strip()
    return capital

def get_lang(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    lang_class = soup.find_all("td", class_="infobox-data")
    lang = lang_class[1].find("a").text.strip()
    return lang

