from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_service import get_items, add_item

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.get('', response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return get_items(db)

@router.post('', response_model=TaskRead)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    return add_item(db, payload)
