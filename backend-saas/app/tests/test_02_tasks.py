import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_create_task(client):
    # Fazer login para obter token
    login_response = client.post("/login", json={"email": "teste@email.com", "password": "123456"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Criar uma nova tarefa
    response = client.post("/tasks?user_id=1", json={"description": "Fazer exercício"}, headers=headers)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["description"] == "Fazer exercício"
    

def test_get_tasks(client):
    login_response = client.post("/login", json={"email": "teste@email.com", "password": "123456"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/tasks?user_id=1", headers=headers)
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    