from sqlalchemy.orm import Session
from app.repositories.enrollment_repo import list_items, create_item
from app.schemas.enrollment import EnrollmentCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: EnrollmentCreate):
    return create_item(db, payload.name, payload.status)
