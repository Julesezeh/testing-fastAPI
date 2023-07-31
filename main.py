from fastapi import FastAPI, HTTPException
import json
import random
from enum import Enum
from models import Users, Gender, Role, User_update
from uuid import uuid4, UUID
from typing import List

app = FastAPI()


# predefined values for a path operation
class ModelName(str, Enum):
    alex = "alex"
    bodega = "bodega"
    leia = "leia"


# Fake db
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# second bd from tutorial
db: List[Users] = [
    Users(
        id=uuid4(),
        first_name="James",
        last_name="St. Patrick",
        gender=Gender.male,
        role=[Role.admin],
    ),
    Users(
        id=uuid4(),
        first_name="Phoenix",
        last_name="Okoye-ezeh",
        gender=Gender.female,
        role=[Role.student, Role.admin],
    ),
]


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


# Multiple query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Required query parameters (simply don't set a default value)
# If you don't want to add a specific value but just make it optional, set the default as None. (|None = None)
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


# Defining required, optional and default valued query parameters
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# USING THE MAKESHIFT DB


# GETTING USERS
@app.get("/api/users/")
async def get_users():
    return db


# CREATING A USER
@app.post("/api/users/")
async def register_user(user: Users):
    db.append(user)
    return {"id": user.id}


# DELETING A USER
@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    return HTTPException(
        status_code=400, detail=f"User with id: {user_id} does not exist."
    )


@app.put("/api/users/{user_id}")
async def update_user(user_id: UUID, user_details: User_update):
    for user in db:
        if user.id == user_id:
            if user_details.first_name:
                user.first_name = user_details.first_name
            if user_details.last_name:
                user.last_name = user_details.last_name
            if user_details.middle_name:
                user.middle_name = user_details.middle_name
            if user_details.gender:
                user.gender = user_details.gender
            if user_details.role:
                user.role = user_details.role

    raise HTTPException(
        status_code=400, detail=f"user with id: {user_id} does not exist."
    )
