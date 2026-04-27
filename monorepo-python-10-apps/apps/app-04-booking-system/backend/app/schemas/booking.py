from pydantic import BaseModel

class BookingBase(BaseModel):
    name: str
    status: str = "active"

class BookingCreate(BookingBase):
    pass

class BookingRead(BookingBase):
    id: int
    class Config:
        from_attributes = True
