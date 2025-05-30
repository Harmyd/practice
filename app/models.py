from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .databases import Base

class User_detail(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    Email = Column(String,unique=True,index=True)
    Username = Column(String,unique=True,index=True)
    Password = Column(String)  
