from pydantic import BaseModel
class User(BaseModel):
    Firstname:str
    Email:str
    Username:str
    Password:str

class UserOut(BaseException):
    Firstname:str
    Email:str
    username:str

    class config():
        orm_mode=True