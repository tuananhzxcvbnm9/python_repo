from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.post import PostCreate, PostRead
from app.services.post_service import get_items, add_item

router = APIRouter(prefix='/posts', tags=['posts'])

@router.get('', response_model=list[PostRead])
def list_posts(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=PostRead)
def create_post(payload: PostCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
