from fastapi import FastAPI,status,HTTPException, Depends
import models,databases,schemas
from databases import get_db,engine,Session
import os
app=FastAPI()

models.Base.metadata.create_all(engine)

port=int(os.environ.get("PORT", "8000"))

@app.get("/")
def show():
    return {"data": "Hello World"}

@app.post("/students",status_code=status.HTTP_201_CREATED)
def create_student(request:schemas.Student,db:Session=Depends(get_db)):
    try:
        new_student=models.Student(
            Name=request.name,
            Age=request.age,
            Department=request.department,
            MatricNo=request.matricNo
        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    