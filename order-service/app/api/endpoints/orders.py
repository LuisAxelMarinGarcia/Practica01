from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.schemas.order import OrderCreate, OrderUpdate, Order
from app.core.services.order_service import OrderService
from app.infrastructure.database import get_db

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return OrderService.create_order(db=db, order=order)

@router.get("/", response_model=list[Order])
def list_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return OrderService.list_orders(db=db, skip=skip, limit=limit)

@router.patch("/{order_id}/status", response_model=Order)
def update_order_status(order_id: int, status: OrderUpdate, db: Session = Depends(get_db)):
    order = OrderService.update_order_status(db=db, order_id=order_id, status=status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
