from sqlalchemy.orm import Session
from app.repositories.post_repo import list_items, create_item
from app.schemas.post import PostCreate

def get_items(db: Session):
    return list_items(db)

def add_item(db: Session, payload: PostCreate):
    return create_item(db, payload.name, payload.status)
