from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.booking import BookingCreate, BookingRead
from app.services.booking_service import get_items, add_item

router = APIRouter(prefix='/bookings', tags=['bookings'])

@router.get('', response_model=list[BookingRead])
def list_bookings(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=BookingRead)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
