from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

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
GET = Returning
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth

"""

@app.get("/")
def Welcome():
    return "Welcome! Use https://stoonks-api.herokuapp.com/docs to learn how to use the API!"

