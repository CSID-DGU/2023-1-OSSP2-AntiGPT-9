from fastapi import FastAPI
import uvicorn
from route.trans import trans_router

app = FastAPI()

# access all
origins = ["*"]

# route
app.include_router(trans_router)

# run: app api, port 8001, http://localhost:8001
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)