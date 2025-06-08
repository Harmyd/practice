from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from .databases import Base

class User_detail(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    Email = Column(String,unique=True,index=True)
    Username = Column(String,unique=True,index=True)
    Password = Column(String)

    task  = Relationship("Task",back_populates="user")

class Task(Base):
    __tablename__= "tasks"
    id = Column(Integer,primary_key=True,index=True)
    Content=Column(String)
    User_id = Column(ForeignKey=("User_detail.id"))

    user = Relationship("User_detail",back_populates="task")
