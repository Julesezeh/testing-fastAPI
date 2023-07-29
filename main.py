from fastapi import FastAPI
import json
import random
from enum import Enum

app = FastAPI()


# predefined values for a path operation
class ModelName(str, Enum):
    alex = "alex"
    bodega = "bodega"
    leia = "leia"


# Fake db
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    name = "Jules"
    mentality = "Slime"
    return {"name": name, "mentality": mentality}


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


@app.get("/name/{name}/")
async def myname(name: str):
    name = name
    welcome = f"Hello {name}"
    return {welcome}


# Using the predefined values (defined in ModelName above)
@app.get("/users/{username}/")
async def users(username: ModelName):
    if username is ModelName.alex:
        name = "alex"
    if username is ModelName.bodega:
        name = "bodega"
    if username is ModelName.leia:
        name = "leia"
    if name:
        return {"model_name": name}
    else:
        return {"model_name": "fraud"}


# Query parameters (Using fake db defined above)
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
