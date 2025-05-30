from ..databases import Session
from fastapi import status,HTTPException
from ..models import User_detail
from ..hash import Hash

def login_user(request,db:Session):
    user=db.query(User_detail).filter(User_detail.Username==request.Username).first()

    if not user or not Hash.verify_hash(request.Password,user.Password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    else:
        return "Logged_in"