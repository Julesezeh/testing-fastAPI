from pydantic import BaseModel
from enum import Enum
from uuid import UUID, uuid4
from typing import List


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    student = "student"
    user = "user"
    janitor = "janitor"


class Users(BaseModel):
    id: UUID = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    role: List[Role]
