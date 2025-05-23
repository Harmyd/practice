from fastapi import FastAPI,status,HTTPException, Depends
import models,databases,schemas
from databases import get_db,engine,Session
from fastapi.middleware.cors import CORSMiddleware
import os
app=FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

port=int(os.environ.get("PORT", "8000"))

@app.get("/")
def show():
    return {"data": "Hi there"}

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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)