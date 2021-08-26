from fastapi import FastAPI

app = FastAPI()

"""
GET = Returning
POST = Sending to endpoint
PUT = update existing smth
DELETE = delete smth

"""

@app.get("/")
def Welcome():
    return "Welcome! Use https://stoonks-api.herokuapp.com/docs to learn how to use the API!"

