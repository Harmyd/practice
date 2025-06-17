from pydantic import BaseModel
from typing import List
class User(BaseModel):
    Firstname:str
    Email:str
    Username:str
    Password:str

class UserOut(BaseModel):
    FirstName:str
    Email:str
    Username:str

    class Config:
        orm_mode=True

class loginInSch(BaseModel):
    Username:str
    Password:str


#Task Schema

class task(BaseModel):
    todo:str

class TaskList(BaseModel):
    Tasks:List[task]

class TaskEdit(BaseModel):
    todo:str

class TaskOut(BaseModel):
    todo:str
    
    class Config:
        orm_mode=True


#Token_schema
