from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,status
from fastapi.responses import JSONResponse
from jose import jwt,JWTError
from .Config import ALGORITHM


oauth2_scheme= OAuth2PasswordBearer("https://practice-vdup.onrender.com/login")
SECRET_KEY="WL2YXpgjYyFue6AL06H7fqxcoQylEk-96UTnb0KpWd0"

def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        user_id = payload.get("user_id")
        username=payload.get("username")
        if not user_id or not username:
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={"message":"Invalid token payload"}
            )
        return JSONResponse(
            content={"user_id":user_id,"username":username}
        )
    except JWTError as e :
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Token expired or invalid"},
            headers={"WWW-Authenticate": "Bearer"}
        )

#def get_current_user(current_user= Depends(verify_token)):
    
