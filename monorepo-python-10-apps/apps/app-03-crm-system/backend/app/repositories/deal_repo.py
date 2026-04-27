from sqlalchemy.orm import Session
from app.models.deal import Deal

def list_items(db: Session) -> list[Deal]:
    return db.query(Deal).all()

def create_item(db: Session, name: str, status: str) -> Deal:
    item = Deal(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
