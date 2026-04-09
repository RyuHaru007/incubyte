import pytest
from app.schemas import EmployeeCreate

def test_employee_create_schema_valid():
    data = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 150000.0
    }
    employee = EmployeeCreate(**data)
    assert employee.full_name == "John Doe"