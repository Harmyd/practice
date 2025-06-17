from ..databases import Session
from ..  import models
from fastapi import HTTPException,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def create_task(request,current_user:dict,db:Session):
    if current_user is None :
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Authentication is required"}
        )
    
    task_list=[]
    for task in request.Tasks:
        new_task=models.Task(Content=task.todo,User_id=current_user[user_id])
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        task_dict = {
            "todo":new_task.Content,
            "task_id":new_task.id
        }
        task_list.append(task_dict)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message":"Task Added",
                 "tasks":task_list
                 }
    )

def get_task_for_user(id,current_user,db:Session):
    if current_user is None :
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Authentication is required"}
        )
    if current_user[id] != id :
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"message":"You can only view your task"}
        )
    
    check_user=db.query(models.User_detail).filter(models.User_detail.id==id).first()
    if not check_user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"User does not exist"}
        )
  
    tasks=db.query(models.Task).filter(models.Task.User_id==id).order_by(models.Task.id.asc()).all()
    if not tasks:
        return JSONResponse(
            content={"message":"No Task found for this user"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"successfull",
                "tasks": jsonable_encoder(tasks)}
    )


def edit_task(task_id,request,current_user:dict,db:Session):
    if not current_user:
         return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Authentication is required"}
        )

    current_task=db.query(models.Task).filter(models.Task.id==task_id).first()
    
    if not current_task:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"task does not exist"}
        )
    
    if current_user.user_id != current_task.User_id:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"This user is not authorized to make changes"}
        )
    current_task.Content=request.todo
    db.commit()
    db.refresh(current_task)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"updated"}
    )


def delete_task(user_id,task_id,current_user,db:Session):
    if not current_user:
         return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Authentication is required"}
        )
    task=db.query(models.Task).filter(models.Task.id==task_id).first()

    if not task:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"task does not exist"}
        )
    
    if user_id != task.User_id:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"This user is not authorized to make changes"}
        )
    
    db.delete(task)
    db.commit()
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message":"Task deleted"}
    )