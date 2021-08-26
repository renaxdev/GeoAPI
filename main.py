from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

import requests 
from bs4 import BeautifulSoup

import req_func

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Stonks API",
        version="0.0.0 beta",
        description="An API for different Stock data",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn.discordapp.com/attachments/879671944637722625/880421415789162516/Neues_Projekt1.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

"""
Requests List:
GET = Returning
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth

"""

@app.get("/")
def Welcome():
    return "Welcome"

@app.get("/bitcoin")
def BTC():
    #try:
    price = get_btc()
    return f"{price:{price}}"
    
    #except:
       # return {"Internal Server Error": "ERROR 500"}


