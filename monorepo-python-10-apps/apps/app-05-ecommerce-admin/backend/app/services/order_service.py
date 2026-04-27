from sqlalchemy.orm import Session
from app.repositories.order_repo import list_items, create_item
from app.schemas.order import OrderCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: OrderCreate):
    return create_item(db, payload.name, payload.status)
