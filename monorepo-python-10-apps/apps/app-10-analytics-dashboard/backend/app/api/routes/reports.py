from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.report import ReportCreate, ReportRead
from app.services.report_service import get_items, add_item

router = APIRouter(prefix='/reports', tags=['reports'])

@router.get('', response_model=list[ReportRead])
def list_reports(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=ReportRead)
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
