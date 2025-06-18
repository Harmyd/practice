from .Config import ALGORITHM,ACCESS_TOKEN_EXPIRY_TIME
from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError,jwt



def create_access_token(data:dict,expiry_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    SECRET_KEY="WL2YXpgjYyFue6AL06H7fqxcoQylEk-96UTnb0KpWd0"
    if expiry_delta:
        expiry=datetime.utcnow() + expiry_delta
    else:
        expiry = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp":expiry})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


