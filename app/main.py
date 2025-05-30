from fastapi import FastAPI,status,HTTPException, Depends
from .models import Base
from .databases import engine
from fastapi.middleware.cors import CORSMiddleware
from .Routes import Sign_up_route
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

Base.metadata.create_all(engine)

port=int(os.environ.get("PORT", "8000"))

@app.get("/")
def show():
    return {"data": "Hi there"}


app.include_router(Sign_up_route.Sign_up_Router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)