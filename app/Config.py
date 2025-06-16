import os 
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv("Secret_key")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_TIME=30