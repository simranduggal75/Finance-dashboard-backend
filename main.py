from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Finance Dashboard Backend is running!"}