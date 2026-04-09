def calculate_deductions(country: str, gross_salary: float) -> tuple[float, float]:
    if country == "United States":
        deduction_rate = 0.12
    else:
        deduction_rate = 0.10
    
    deductions = gross_salary * deduction_rate
    net_salary = gross_salary - deductions
    return deductions, net_salary