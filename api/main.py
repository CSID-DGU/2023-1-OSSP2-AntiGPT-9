from fastapi import FastAPI
import uvicorn

app = FastAPI

#access all
origins = ["*"]

#run: app api, port 8001, http://localhost:8001
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)