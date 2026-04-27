from pydantic import BaseModel

class PostBase(BaseModel):
    name: str
    status: str = "active"

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    class Config:
        from_attributes = True
