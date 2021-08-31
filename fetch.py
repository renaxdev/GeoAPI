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


def get_citizen(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    citizen = classes[17].text.strip() #Unnötige Sachen weglöschen lassen
    return citizen


def get_area(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    area = classes[15].text.strip() #Unnötige Sachen weglöschen lassen
    return area


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

def get_currency(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    currency = classes[27].text.strip()
    return currency    

def get_timezn(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    timezone = classes[28].text.strip()
    return timezone

def get_iso(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    classes = soup.find_all("td", class_="infobox-data")
    iso = classes[31].text.strip()
    return iso