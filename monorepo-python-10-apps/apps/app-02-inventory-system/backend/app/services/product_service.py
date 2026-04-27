from sqlalchemy.orm import Session
from app.repositories.product_repo import list_items, create_item
from app.schemas.product import ProductCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: ProductCreate):
    return create_item(db, payload.name, payload.status)
