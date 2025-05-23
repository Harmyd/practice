from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os


# Postgre database URL
DATABASE_URL = os.environ.get("Database_url")
# Create the SQLAlchemy engine
# Create a db engine
engine = create_engine(DATABASE_URL,"postgresql://postgres:#Hamid2345#*@db.mjjftecmbhuncnfgbddn.supabase.co:6543/postgres")
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