from sqlalchemy.orm import Session
from app.repositories.booking_repo import list_items, create_item
from app.schemas.booking import BookingCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: BookingCreate):
    return create_item(db, payload.name, payload.status)
