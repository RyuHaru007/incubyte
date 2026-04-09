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

def test_job_title_salary_metrics(client):
    # Setup: 2 Devs, 1 Manager
    client.post("/employees/", json={"full_name": "D", "job_title": "Dev", "country": "India", "salary": 100000.0})
    client.post("/employees/", json={"full_name": "E", "job_title": "Dev", "country": "US", "salary": 300000.0})
    client.post("/employees/", json={"full_name": "F", "job_title": "Manager", "country": "India", "salary": 200000.0})

    # Action: Get metrics for Dev
    response = client.get("/employees/metrics/title?job_title=Dev")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["job_title"] == "Dev"
    assert data["avg_salary"] == 200000.0  # (100k + 300k) / 2

def test_metrics_no_data_found(client):
    response_country = client.get("/employees/metrics/country?country=Mars")
    assert response_country.status_code == 404

    response_title = client.get("/employees/metrics/title?job_title=Astronaut")
    assert response_title.status_code == 404