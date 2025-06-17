import os 
from dotenv import load_dotenv

#dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
#load_dotenv(dotenv_path=dotenv_path)
#SECRET_KEY = os.getenv("Secret_key")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_TIME=30