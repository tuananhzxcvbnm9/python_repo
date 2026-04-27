from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.expense import ExpenseCreate, ExpenseRead
from app.services.expense_service import get_items, add_item

router = APIRouter(prefix='/expenses', tags=['expenses'])

@router.get('', response_model=list[ExpenseRead])
def list_expenses(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=ExpenseRead)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
