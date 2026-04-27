from pydantic import BaseModel

class EnrollmentBase(BaseModel):
    name: str
    status: str = "active"

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentRead(EnrollmentBase):
    id: int
    class Config:
        from_attributes = True
