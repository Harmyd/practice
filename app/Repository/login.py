from ..databases import Session
from fastapi import status,HTTPException
from .. import Token
from ..models import User_detail
from ..hash import Hash
from sqlalchemy import func
from fastapi.responses import JSONResponse


def login_user(request,db:Session):
    username=request.Username.strip().lower()
    user=db.query(User_detail).filter(func.lower(User_detail.Username)==username).first()
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"user not found"}
        ) 
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    elif not Hash.verify_hash(request.Password,user.Password):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"wrong password"}
        )
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Wrong Password")
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content= {"message":"Login Successful",
                    "user_id":user.id,
                    "user_name":user.Username
                    }
        )
        

      