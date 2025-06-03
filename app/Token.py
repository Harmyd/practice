import secrets
from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError,jwt

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_TIME=30


def create_access_token(data:dict,expiry_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expiry_delta:
        expiry=datetime.utcnow + expiry_delta
    else:
        expiry = datetime.utcnow + timedelta(minutes=15)
    to_encode.update({"exp":expiry})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
