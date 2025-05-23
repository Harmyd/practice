from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from databases import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Age = Column(Integer)
    Department = Column(String)
    MatricNo = Column(String, unique=True, index=True)  
