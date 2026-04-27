from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment

def list_items(db: Session) -> list[Enrollment]:
    return db.query(Enrollment).all()

def create_item(db: Session, name: str, status: str) -> Enrollment:
    item = Enrollment(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
