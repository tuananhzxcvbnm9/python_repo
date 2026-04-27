from sqlalchemy.orm import Session
from app.models.post import Post

def list_items(db: Session) -> list[Post]:
    return db.query(Post).all()

def create_item(db: Session, name: str, status: str) -> Post:
    item = Post(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
