from fastapi import FastAPI
import json
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"name": "Jules", "mentality": "Slime"}


@app.get("/number")
async def rando():
    # symbols = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
    return random.randint(0, 100)
