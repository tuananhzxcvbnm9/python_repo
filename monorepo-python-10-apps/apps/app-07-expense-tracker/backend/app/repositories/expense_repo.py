from sqlalchemy.orm import Session
from app.models.expense import Expense

def list_items(db: Session) -> list[Expense]:
    return db.query(Expense).all()

def create_item(db: Session, name: str, status: str) -> Expense:
    item = Expense(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
