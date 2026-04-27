from pydantic import BaseModel

class OrderBase(BaseModel):
    name: str
    status: str = "active"

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    class Config:
        from_attributes = True
