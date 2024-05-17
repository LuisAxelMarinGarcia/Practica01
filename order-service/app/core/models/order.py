from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Creado")
