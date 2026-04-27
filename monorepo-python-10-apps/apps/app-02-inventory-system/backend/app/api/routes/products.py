from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import get_items, add_item

router = APIRouter(prefix='/products', tags=['products'])

@router.get('', response_model=list[ProductRead])
def list_products(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=ProductRead)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
