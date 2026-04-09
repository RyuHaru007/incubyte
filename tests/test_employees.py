def test_create_employee(client):
    response = client.post(
        "/employees/",
        json={"full_name": "Bruce Wayne", "job_title": "CEO", "country": "United States", "salary": 500000.0}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Bruce Wayne"
    assert "id" in data