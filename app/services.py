def calculate_deductions(country: str, gross_salary: float) -> tuple[float, float]:
    country_normalized = country.strip().lower()
    if country_normalized == "india":
        deduction_rate = 0.10
    elif country_normalized == "united states":
        deduction_rate = 0.12
    else:
        deduction_rate = 0.0

    deductions = gross_salary * deduction_rate
    net_salary = gross_salary - deductions
    return deductions, net_salary