from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderCreate(BaseModel):
    total: float
    status: str = "Creado"

class OrderUpdate(BaseModel):
    status: str

class Order(BaseModel):
    id: int
    total: float
    fecha: datetime
    status: str

    class Config:
        orm_mode = True
