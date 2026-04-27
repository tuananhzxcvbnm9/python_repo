from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    status: str = "active"

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    class Config:
        from_attributes = True
