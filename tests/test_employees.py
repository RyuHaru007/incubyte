def test_create_employee(client):
    response = client.post(
        "/employees/",
        json={"full_name": "Bruce Wayne", "job_title": "CEO", "country": "United States", "salary": 500000.0}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Bruce Wayne"
    assert "id" in data

def test_get_employee(client):
    # Setup: Create an employee first
    create_resp = client.post(
        "/employees/",
        json={"full_name": "Clark Kent", "job_title": "Reporter", "country": "United States", "salary": 80000.0}
    )
    emp_id = create_resp.json()["id"]

    # Test GET
    response = client.get(f"/employees/{emp_id}")
    assert response.status_code == 200
    assert response.json()["full_name"] == "Clark Kent"

def test_get_employee_not_found(client):
    response = client.get("/employees/999")
    assert response.status_code == 404