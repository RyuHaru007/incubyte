import pytest
from pydantic import ValidationError
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

def test_employee_create_schema_invalid_salary():
    data = {
        "full_name": "Jane Doe",
        "job_title": "Manager",
        "country": "United States",
        "salary": -5000.0
    }
    with pytest.raises(ValidationError):
        EmployeeCreate(**data)