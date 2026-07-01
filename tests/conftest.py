import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """cliente de testes HTTP para o FastAPI."""
    return TestClient(app)