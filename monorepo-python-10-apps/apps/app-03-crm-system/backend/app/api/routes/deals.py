from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.deal import DealCreate, DealRead
from app.services.deal_service import get_items, add_item

router = APIRouter(prefix='/deals', tags=['deals'])

@router.get('', response_model=list[DealRead])
def list_deals(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=DealRead)
def create_deal(payload: DealCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
