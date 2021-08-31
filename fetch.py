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
    classes = soup.find_all("td", class_="infobox-data")
    lang = classes[1].find("a").text.strip()
    return lang

def get_president(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    president = classes[1].find("a").text.strip()
    return president
