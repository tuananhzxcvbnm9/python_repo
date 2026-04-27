from pydantic import BaseModel

class DealBase(BaseModel):
    name: str
    status: str = "active"

class DealCreate(DealBase):
    pass

class DealRead(DealBase):
    id: int
    class Config:
        from_attributes = True
