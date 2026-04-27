from sqlalchemy.orm import Session
from app.models.report import Report

def list_items(db: Session) -> list[Report]:
    return db.query(Report).all()

def create_item(db: Session, name: str, status: str) -> Report:
    item = Report(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
