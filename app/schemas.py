from pydantic import BaseModel, Field, ConfigDict

class EmployeeBase(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float = Field(..., gt=0)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)