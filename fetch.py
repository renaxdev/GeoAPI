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
    president = classes[4].text.strip()
    return president


def get_longitude(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("span", class_="longitude")
    longitude = classes[0].text.strip()
    return longitude


def get_latitude(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("span", class_="latitude")
    latitude = classes[0].text.strip()
    return latitude
