from sqlalchemy.orm import Session
from app.models.order import Order

def list_items(db: Session) -> list[Order]:
    return db.query(Order).all()

def create_item(db: Session, name: str, status: str) -> Order:
    item = Order(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
