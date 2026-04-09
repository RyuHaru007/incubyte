from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, services 
from app.database import get_db

router = APIRouter(prefix="/employees", tags=["Employees"])

# --- NEW HELPER FUNCTION ---
def get_employee_or_404(emp_id: int, db: Session) -> schemas.EmployeeResponse:
    db_employee = crud.get_employee(db, employee_id=emp_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.post("/", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@router.get("/metrics/country", response_model=schemas.CountryMetricsResponse)
def get_country_metrics(country: str, db: Session = Depends(get_db)):
    metrics = crud.get_country_metrics(db, country=country)
    
    return {
        "country": country,
        "min_salary": metrics.min_salary or 0.0,
        "max_salary": metrics.max_salary or 0.0,
        "avg_salary": metrics.avg_salary or 0.0
    }

@router.get("/metrics/title", response_model=schemas.JobTitleMetricsResponse)
def get_job_title_metrics(job_title: str, db: Session = Depends(get_db)):
    metrics = crud.get_job_title_metrics(db, job_title=job_title)
    
    return {
        "job_title": job_title,
        "avg_salary": metrics.avg_salary or 0.0
    }

@router.get("/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    # --- REFACTORED TO USE HELPER ---
    return get_employee_or_404(emp_id, db)

@router.put("/{emp_id}", response_model=schemas.EmployeeResponse)
def update_employee(emp_id: int, employee_update: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = get_employee_or_404(emp_id, db)
    return crud.update_employee(db=db, db_employee=db_employee, employee_update=employee_update)

@router.delete("/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee_or_404(emp_id, db)
    crud.delete_employee(db=db, db_employee=db_employee)

@router.get("/{emp_id}/salary", response_model=schemas.SalaryResponse)
def get_employee_salary(emp_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee_or_404(emp_id, db)
    deductions, net_salary = services.calculate_deductions(
        country=db_employee.country, 
        gross_salary=db_employee.salary
    )
    return {
        "employee_id": db_employee.id,
        "gross_salary": db_employee.salary,
        "deductions": deductions,
        "net_salary": net_salary
    }