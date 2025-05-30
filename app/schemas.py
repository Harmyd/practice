from pydantic import BaseModel
class User(BaseModel):
    Firstname:str
    Email:str
    Username:str
    Password:str

class UserOut(BaseException):
    FirstName:str
    Email:str
    Username:str

    class Config:
        orm_mode=True