from sqlalchemy.orm import Session
from app.repositories.report_repo import list_items, create_item
from app.schemas.report import ReportCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: ReportCreate):
    return create_item(db, payload.name, payload.status)
