from fastapi import FastAPI,status,HTTPException, Depends
from .models import Base
from .databases import engine
from fastapi.middleware.cors import CORSMiddleware
from .Routes import Sign_up_route,login_route
import os
app=FastAPI()



# CORS
origin=[
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
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
app.include_router(login_route.Login_route)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)