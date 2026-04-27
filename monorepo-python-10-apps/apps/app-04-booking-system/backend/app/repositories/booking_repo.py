from sqlalchemy.orm import Session
from app.models.booking import Booking

def list_items(db: Session) -> list[Booking]:
    return db.query(Booking).all()

def create_item(db: Session, name: str, status: str) -> Booking:
    item = Booking(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
