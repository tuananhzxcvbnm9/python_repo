from pydantic import BaseModel

class TicketBase(BaseModel):
    name: str
    status: str = "active"

class TicketCreate(TicketBase):
    pass

class TicketRead(TicketBase):
    id: int
    class Config:
        from_attributes = True
