from fastapi import FastAPI
from app.api.endpoints import orders
from app.infrastructure.database import engine, Base
from app.core.models.order import Order

# Crear las tablas en la base de datos (opcional, por si no se ha ejecutado initialize_db.py)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Order Service is running"}
