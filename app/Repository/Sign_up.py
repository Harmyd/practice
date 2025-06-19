from fastapi import HTTPException,status
from fastapi.responses import JSONResponse
from ..models import User_detail
from ..databases import Session
from ..schemas import User
from ..hash import Hash
from fastapi.responses import PlainTextResponse
from ..Token import create_access_token

def signUp(request,db:Session):
    Username=request.Username.strip()
    Email=request.Email.strip().lower()
    username_check=db.query(User_detail).filter(User_detail.Username==Username).first()
    Email_check=db.query(User_detail).filter(User_detail.Email==Email).first()
    if username_check:
        return {"message":"username already exist"}
        #raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username already exist")
    elif Email_check:
        return {"message":"email already exist"}
        #raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already exist")
    else:
        try:
            new_user=User_detail(FirstName=request.Firstname,Email=request.Email,Username=request.Username,Password=Hash.hash_password(request.Password))
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={
                            "message":"Signed up successfully",
                            "Token":create_access_token(data={"user_id":new_user.id,"username":new_user.Username}),
                            "Token_type":"Bearer"
                         }
            )
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))