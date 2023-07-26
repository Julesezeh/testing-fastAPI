from fastapi import FastAPI
import json
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"name": "Jules", "mentality": "Slime"}


@app.get("/number/")
async def rando():
    randint: int = random.randint(0, 100)
    # symbols = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
    return randint


@app.get("/number/{num}/")
async def spec_range_rando(num: int):
    randint = random.randint(0, num)
    list_of_rando = [x for x in range(0, randint)]
    return {"number range generated": list_of_rando, "limit set by you": num}
