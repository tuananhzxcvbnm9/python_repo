from pydantic import BaseModel

class ExpenseBase(BaseModel):
    name: str
    status: str = "active"

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseRead(ExpenseBase):
    id: int
    class Config:
        from_attributes = True
