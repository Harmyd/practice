from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,status,HTTPException
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
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token payload"
                )
        return {"user_id":user_id,"username":username}
        
    except JWTError as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired or invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )

#def get_current_user(current_user= Depends(verify_token)):
    
