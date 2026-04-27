from sqlalchemy.orm import Session
from app.models.ticket import Ticket

def list_items(db: Session) -> list[Ticket]:
    return db.query(Ticket).all()

def create_item(db: Session, name: str, status: str) -> Ticket:
    item = Ticket(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
