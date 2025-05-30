from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from ..databases import Session,get_db
from ..schemas import loginInSch
from ..Repository import login


Login_route=APIRouter(
    prefix="/login"
)
@Login_route.post("/",status_code=status.HTTP_200_OK)
def loginIn(request:loginInSch,db:Session=Depends(get_db)):
    return login.login_user(request,db)