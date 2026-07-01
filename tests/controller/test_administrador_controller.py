import pytest
from unittest.mock import MagicMock
from main import app
from app.controller.administrador_controller import get_administrador_service

@pytest.fixture
def mock_service():
    return MagicMock()

@pytest.fixture(autouse=True)
def setup_dependencies(mock_service):
    app.dependency_overrides[get_administrador_service] = lambda: mock_service
    yield
    app.dependency_overrides.clear()

def test_should_return_201_when_creating_administrator_successfully(client, mock_service):
    payload = {
        "nome": "Ronaldo Nazario",
        "email": "coordenacao.unidade1@academia.com",
        "senha": "SecurePass@123"
    }
    mock_service.create.return_value = {
        "id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "nome": "Ronaldo Nazario",
        "email": "coordenacao.unidade1@academia.com"
    }

    response = client.post("/administradores/", json=payload)

    assert response.status_code == 201
    assert response.json()["email"] == "coordenacao.unidade1@academia.com"

def test_should_return_400_when_administrator_email_already_exists(client, mock_service):
    body = {
        "nome": "Ronaldo Nazario",
        "email": "coordenacao.unidade1@academia.com",
        "senha": "SecurePass@123"
    }
    mock_service.create.side_effect = ValueError("Administrador com esse email já existe.")

    resp = client.post("/administradores/", json=body)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Administrador com esse email já existe."

def test_should_return_200_when_reading_all_administrators(client, mock_service):
    mock_service.read.return_value = [
        {"nome": "Admin Central", "email": "central@academia.com"},
        {"nome": "Supervisor Geral", "email": "supervisor@academia.com"}
    ]

    response = client.get("/administradores/")

    assert response.status_code == 200
    assert len(response.json()) == 2