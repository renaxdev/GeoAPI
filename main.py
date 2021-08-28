"""
Starte den Lokalen Server mit: uvicorn main:app --reload

Erreichbar unter: http://127.0.0.1:8000/

Requests List:
GET = Get lol
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth

"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import requests 
from bs4 import BeautifulSoup

app = FastAPI()

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
        "url": "https://i.imgflip.com/4qp9rs.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/")
def Welcome():
    return "Welcome! Use https://geography-api.herokuapp.com/docs to learn how to use the API!"


