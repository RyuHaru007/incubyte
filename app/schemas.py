from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float