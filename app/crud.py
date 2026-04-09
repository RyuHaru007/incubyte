from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, db_employee: models.Employee, employee_update: schemas.EmployeeCreate):
    for key, value in employee_update.model_dump().items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, db_employee: models.Employee):
    db.delete(db_employee)
    db.commit()

def get_country_metrics(db: Session, country: str):
    return db.query(
        func.min(models.Employee.salary).label("min_salary"),
        func.max(models.Employee.salary).label("max_salary"),
        func.avg(models.Employee.salary).label("avg_salary")
    ).filter(models.Employee.country == country).first()