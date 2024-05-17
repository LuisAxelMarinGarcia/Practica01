from sqlalchemy.orm import Session
from app.core.models.order import Order
from app.core.schemas.order import OrderUpdate, OrderCreate
from app.infrastructure.repositories.order_repository import OrderRepository

class OrderService:

    @staticmethod
    def create_order(db: Session, order: OrderCreate) -> Order:
        return OrderRepository.create_order(db, order)

    @staticmethod
    def list_orders(db: Session, skip: int, limit: int) -> list[Order]:
        return OrderRepository.list_orders(db, skip, limit)

    @staticmethod
    def update_order_status(db: Session, order_id: int, status: OrderUpdate) -> Order:
        return OrderRepository.update_order_status(db, order_id, status)
