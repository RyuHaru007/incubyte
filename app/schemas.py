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

class SalaryResponse(BaseModel):
    employee_id: int
    gross_salary: float
    deductions: float
    net_salary: float
    model_config = ConfigDict(from_attributes=True)

class CountryMetricsResponse(BaseModel):
    country: str
    min_salary: float
    max_salary: float
    avg_salary: float