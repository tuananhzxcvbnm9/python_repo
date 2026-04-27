from sqlalchemy.orm import Session
from app.repositories.expense_repo import list_items, create_item
from app.schemas.expense import ExpenseCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: ExpenseCreate):
    return create_item(db, payload.name, payload.status)
