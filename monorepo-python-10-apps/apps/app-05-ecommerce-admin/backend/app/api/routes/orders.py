from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.order import OrderCreate, OrderRead
from app.services.order_service import get_items, add_item

router = APIRouter(prefix='/orders', tags=['orders'])

@router.get('', response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=OrderRead)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
