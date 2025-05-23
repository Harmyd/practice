from pydantic import BaseModel
class Student(BaseModel):
    name:str
    age:int
    matricNo:str
    department:str