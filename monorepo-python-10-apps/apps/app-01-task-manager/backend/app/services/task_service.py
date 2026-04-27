from sqlalchemy.orm import Session
from app.repositories.task_repo import list_items, create_item
from app.schemas.task import TaskCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: TaskCreate):
    return create_item(db, payload.name, payload.status)
