from ..databases import Session
from fastapi import status,HTTPException
from ..models import User_detail
from ..hash import Hash
from sqlalchemy import func

def login_user(request,db:Session):
    username=request.Username.strip().lower()
    user=db.query(User_detail).filter(func.lower(User_detail.Username)==username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    elif not Hash.verify_hash(request.Password,user.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Wrong Password")
    else:
        return {
            "message":"Login Successful",
            "user_id":user.id,
            "username":user.Username
        }