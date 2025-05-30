from pydantic import BaseModel
class User(BaseModel):
    Firstname:str
    Email:str
    Username:str
    Password:str