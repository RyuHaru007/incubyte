from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float = Field(..., gt=0)