"""
Starte den Lokalen Server mit: uvicorn main:app --reload

Erreichbar unter: http://127.0.0.1:8000/

Requests List:
GET = Get lol
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth


WICHTIG:

WENN ETWAS BEI HEROKU NICHT GEHT, SCHREIB MIR DIREKT AN
!!!

DONT TOUCH:
- Procfile
- requirements.txt --> wenn du neue libs hinzugefügt hast, schreib mir 

"""

# --------Libs------#
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import wikipedia

import fetch

import requests
import json


import fetch_data

# -------other--------#

app = FastAPI()

# ---------openapi docs--------#
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Geo API",
        version="0.0.0 beta",
        description="An API for geographical data",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn.discordapp.com/attachments/883257235193614357/883257298259165204/image0.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


# ---------ENDPOINTS--------#
@app.get("/", tags=["welcome"])
def Welcome():
    return "Welcome! Use https://geography-api.herokuapp.com/docs to learn how to use the API!"


@app.get("/country/{country}", tags=["country"])
def country(country: str):
    try:
        filter_api = requests.get(f"https://coronavirus-19-api.herokuapp.com/countries/{country}")
        f = filter_api.json()

        try:
            ct_wiki = wikipedia.page(country)
            infos = fetch_data.FetchData(country)
        except wikipedia.exceptions.DisambiguationError:
            return {"error 500": f"{country} may refer to something else"}

        inv = {
            "country": {
                "title": ct_wiki.title,
                "url": ct_wiki.url,
                "official_language": fetch.get_lang(ct_wiki.url),
                "capital": fetch.get_capital(ct_wiki.url),
                "president": fetch.get_president(ct_wiki.url),
                "population": infos.population(),
                "area": f"{infos.area()}km2",
                "longitude": fetch.get_longitude(ct_wiki.url),
                "latitude": fetch.get_latitude(ct_wiki.url),
                "currency": infos.currencies()[0],
                "timezone": infos.timezones(),
                "iso3166": infos.iso()
            }
        }
        return inv

    except json.decoder.JSONDecodeError:
        return "Enter a real country"
