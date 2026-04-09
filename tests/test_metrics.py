def test_country_salary_metrics(client):
    # Setup: Create 2 employees in India, 1 in the US
    client.post("/employees/", json={"full_name": "A", "job_title": "Dev", "country": "India", "salary": 100000.0})
    client.post("/employees/", json={"full_name": "B", "job_title": "QA", "country": "India", "salary": 200000.0})
    client.post("/employees/", json={"full_name": "C", "job_title": "Dev", "country": "United States", "salary": 500000.0})

    # Action: Get metrics for India
    response = client.get("/employees/metrics/country?country=India")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["country"] == "India"
    assert data["min_salary"] == 100000.0
    assert data["max_salary"] == 200000.0
    assert data["avg_salary"] == 150000.0  # (100k + 200k) / 2