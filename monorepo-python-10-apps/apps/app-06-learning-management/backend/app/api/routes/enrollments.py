from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead
from app.services.enrollment_service import get_items, add_item

router = APIRouter(prefix='/enrollments', tags=['enrollments'])

@router.get('', response_model=list[EnrollmentRead])
def list_enrollments(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=EnrollmentRead)
def create_enrollment(payload: EnrollmentCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
