from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.ticket import TicketCreate, TicketRead
from app.services.ticket_service import get_items, add_item

router = APIRouter(prefix='/tickets', tags=['tickets'])

@router.get('', response_model=list[TicketRead])
def list_tickets(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=TicketRead)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
