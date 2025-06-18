from ..databases import get_db,Session
from ..schemas import TaskList,TaskOut,TaskEdit
from ..Repository import Tasks
from fastapi import HTTPException,status,Depends,APIRouter
from fastapi.responses import JSONResponse
from ..oauth import verify_token


TaskRoute = APIRouter(
    prefix="/Task"
    )


@TaskRoute.post("/add_task",status_code=status.HTTP_201_CREATED,response_model=TaskOut)
def taskcreate(request:TaskList,db:Session=Depends(get_db),current_user=Depends(verify_token)):
    return Tasks.create_task(request,current_user,db)

@TaskRoute.get("/{id}",status_code=status.HTTP_200_OK,response_model=TaskOut)
def get_task(id:int,db:Session=Depends(get_db),current_user=Depends(verify_token)):
    return Tasks.get_task_for_user(id,current_user,db)

@TaskRoute.put("/update_task/{task_id}",status_code=status.HTTP_200_OK,response_model=TaskOut)
def update_task(task_id:int,request:TaskEdit,current_user=Depends(verify_token), db:Session=Depends(get_db)):
    return Tasks.edit_task(task_id,current_user,request,db)

@TaskRoute.delete("/delete_task/{task_id}",status_code=status.HTTP_200_OK)
def delete_task(task_id:int,user_id:int,current_user=Depends(verify_token), db:Session=Depends(get_db)):
    return Tasks.delete_task(user_id,task_id,db)

