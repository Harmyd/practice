from fastapi import APIRouter,status,Depends
from ..databases import Session,get_db
from ..schemas import User,UserOut
from ..Repository import Sign_up

Sign_up_Router=APIRouter(
    prefix="/signup"
)
@Sign_up_Router.post("/",status_code=status.HTTP_201_CREATED,response_model=UserOut)
def sign_up(request:User,db:Session=Depends(get_db)):
    return Sign_up.signUp(request,db)
