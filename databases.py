from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os


# Postgre database URL
DATABASE_URL = "postgresql://hamid:VFPlRcEMnYa0pveS6IIsIWFWsGJcOfK9@dpg-d0ocf1be5dus73auola0-a.oregon-postgres.render.com/studentdb_m113"
# Create the SQLAlchemy engine
# Create a db engine
engine = create_engine(DATABASE_URL)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for declarative models
Base=declarative_base()
# Dependency to get the database session 
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()