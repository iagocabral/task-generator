import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db, SessionLocal

# Substituir a conexão do banco no FastAPI para usar o banco de testes
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # Forçar FastAPI a usar o banco de testes

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_create_user(client):
    response = client.post("/users", json={"name": "Teste", "email": "teste@email.com", "password": "123456"})

    print(response.json())  # Debug

    assert response.status_code == 200
    assert response.json()["name"] == "Teste"
    assert response.json()["email"] == "teste@email.com"

def test_login_user(client):
    response = client.post("/login", json={"email": "teste@email.com", "password": "123456"})
    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()