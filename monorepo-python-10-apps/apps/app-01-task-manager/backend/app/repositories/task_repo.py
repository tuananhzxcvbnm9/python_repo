from sqlalchemy.orm import Session
from app.models.task import Task

def list_items(db: Session) -> list[Task]:
    return db.query(Task).all()

def create_item(db: Session, name: str, status: str) -> Task:
    item = Task(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
