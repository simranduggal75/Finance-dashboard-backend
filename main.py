from fastapi import FastAPI
from database import engine, Base


from models import user, transaction

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Finance Dashboard Backend is running!"}