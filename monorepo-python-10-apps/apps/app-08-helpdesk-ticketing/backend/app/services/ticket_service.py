from sqlalchemy.orm import Session
from app.repositories.ticket_repo import list_items, create_item
from app.schemas.ticket import TicketCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: TicketCreate):
    return create_item(db, payload.name, payload.status)
