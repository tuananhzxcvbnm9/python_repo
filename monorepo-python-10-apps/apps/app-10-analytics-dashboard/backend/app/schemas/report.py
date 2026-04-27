from pydantic import BaseModel

class ReportBase(BaseModel):
    name: str
    status: str = "active"

class ReportCreate(ReportBase):
    pass

class ReportRead(ReportBase):
    id: int
    class Config:
        from_attributes = True
