from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    # 1. Simulate a user visiting "/"
    response = client.get("/")

    # 2. Check if the server responded with "200 OK" (Success)
    assert response.status_code == 200

    # 3. Check if the JSON is exactly what we expect
    assert response.json() == {"message": "Hello from CI/CD Pipeline!"}