from fastapi import FastAPI

app = FastAPI()

"""
GET = Returning
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth

"""

@app.get("/")
def home():
    return {"Data": "Test"}