from ..databases import get_db,Session
from ..schemas import Task,TaskOut
from ..Repository import Tasks
from fastapi import HTTPException,status,Depends,APIRouter
from fastapi.responses import JSONResponse


TaskRoute = APIRouter(
    prefix="/Task"
    )


@TaskRoute.post("/add_task",status_code=status.HTTP_201_CREATED,response_model=TaskOut)
def taskcreate(request:Task,db:Session=Depends(get_db)):
    return Tasks.create_task(request,db)

@TaskRoute.get("/{id}",status_code=status.HTTP_200_OK,response_model=TaskOut)
def get_task(id:int,db:Session=Depends(get_db)):
    return Tasks.get_task_for_user(id,db)

@TaskRoute.put("/update_task/{task_id}",status_code=status.HTTP_200_OK,response_model=TaskOut)
def update_task(task_id:int,request:Task,db:Session=Depends(get_db)):
    return Tasks.edit_task(task_id,request,db)

@TaskRoute.delete("/delete_task/{task_id}",status_code=status.HTTP_200_OK)
def delete_task(task_id:int,user_id:int,db:Session=Depends(get_db)):
    return Tasks.delete_task(user_id,task_id,db)