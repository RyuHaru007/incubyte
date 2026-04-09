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

def test_update_employee(client):
    # Setup
    create_resp = client.post(
        "/employees/",
        json={"full_name": "Diana Prince", "job_title": "Curator", "country": "France", "salary": 90000.0}
    )
    emp_id = create_resp.json()["id"]

    # Action
    response = client.put(
        f"/employees/{emp_id}",
        json={"full_name": "Diana Prince", "job_title": "Director", "country": "France", "salary": 120000.0}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["salary"] == 120000.0
    assert response.json()["job_title"] == "Director"

def test_delete_employee(client):
    # Setup
    create_resp = client.post(
        "/employees/",
        json={"full_name": "Barry Allen", "job_title": "CSI", "country": "United States", "salary": 70000.0}
    )
    emp_id = create_resp.json()["id"]

    # Action
    response = client.delete(f"/employees/{emp_id}")
    assert response.status_code == 204

    # Verify it was actually deleted
    get_resp = client.get(f"/employees/{emp_id}")
    assert get_resp.status_code == 404