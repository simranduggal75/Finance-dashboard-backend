from fastapi import FastAPI
from database import engine, Base


from models import user, transaction
from routes import user_routes
from routes import transaction_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)

app.include_router(transaction_routes.router)

@app.get("/")
def home():
    return {"message": "Finance Dashboard Backend is running!"}




