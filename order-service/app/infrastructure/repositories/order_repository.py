from sqlalchemy.orm import Session
from app.core.models.order import Order
from app.core.schemas.order import OrderCreate, OrderUpdate

class OrderRepository:

    @staticmethod
    def create_order(db: Session, order: OrderCreate) -> Order:
        db_order = Order(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def list_orders(db: Session, skip: int, limit: int) -> list[Order]:
        return db.query(Order).offset(skip).limit(limit).all()

    @staticmethod
    def update_order_status(db: Session, order_id: int, status: OrderUpdate) -> Order:
        order = db.query(Order).filter(Order.id == order_id).first()
        if order is None:
            return None
        order.status = status.status
        db.commit()
        db.refresh(order)
        return order
