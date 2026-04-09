def test_calculate_salary_india(client):
    # Setup: Create an employee in India
    create_resp = client.post(
        "/employees/",
        json={"full_name": "Rahul", "job_title": "Dev", "country": "India", "salary": 100000.0}
    )
    emp_id = create_resp.json()["id"]

    # Action: Get salary calculation
    response = client.get(f"/employees/{emp_id}/salary")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["gross_salary"] == 100000.0
    assert data["deductions"] == 10000.0   # 10%
    assert data["net_salary"] == 90000.0

def test_calculate_salary_us(client):
    create_resp = client.post(
        "/employees/",
        json={"full_name": "John", "job_title": "Manager", "country": "United States", "salary": 100000.0}
    )
    emp_id = create_resp.json()["id"]

    response = client.get(f"/employees/{emp_id}/salary")
    
    data = response.json()
    assert data["deductions"] == 12000.0   # 12%
    assert data["net_salary"] == 88000.0