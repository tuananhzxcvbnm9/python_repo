from sqlalchemy.orm import Session
from app.models.product import Product

def list_items(db: Session) -> list[Product]:
    return db.query(Product).all()

def create_item(db: Session, name: str, status: str) -> Product:
    item = Product(name=name, status=status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
