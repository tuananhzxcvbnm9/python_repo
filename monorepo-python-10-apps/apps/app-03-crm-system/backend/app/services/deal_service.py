from sqlalchemy.orm import Session
from app.repositories.deal_repo import list_items, create_item
from app.schemas.deal import DealCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: DealCreate):
    return create_item(db, payload.name, payload.status)
