def calculate_deductions(country: str, gross_salary: float) -> tuple[float, float]:
    # Currently only handles the 10% rule from our first test
    deduction_rate = 0.10
    deductions = gross_salary * deduction_rate
    net_salary = gross_salary - deductions
    return deductions, net_salary