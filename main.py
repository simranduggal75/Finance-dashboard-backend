from fastapi import FastAPI
from database import engine, Base
from models import user, transaction
from routes import user_routes, transaction_routes, dashboard_routes

app = FastAPI(
    title="Finance Dashboard API",
    docs_url="/docs",
    openapi_url="/openapi.json",
    root_path_in_servers=False
)

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(dashboard_routes.router)

@app.get("/")
def home():
    return {"message": "Finance Dashboard Backend is running!"}