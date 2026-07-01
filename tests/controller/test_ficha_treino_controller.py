import pytest
from unittest.mock import MagicMock
import uuid
from main import app
from app.controller.ficha_treino_controller import get_ficha_treino_service

@pytest.fixture
def mock_service():
    return MagicMock()

@pytest.fixture(autouse=True)
def setup_dependencies(mock_service):
    app.dependency_overrides[get_ficha_treino_service] = lambda: mock_service
    yield
    app.dependency_overrides.clear()

def test_should_create_ficha_treino_successfully(client, mock_service):
    aluno_id = str(uuid.uuid4())
    instrutor_id = str(uuid.uuid4())
    
    payload = {
        "objetivo": "Ganho de Massa Muscular",
        "aluno_id": aluno_id,
        "instrutor_id": instrutor_id
    }
    
    mock_service.create.return_value = {
        "id": str(uuid.uuid4()),
        "objetivo": "Ganho de Massa Muscular",
        "aluno_id": aluno_id,
        "instrutor_id": instrutor_id
    }

    response = client.post("/fichas-treino/", json=payload)

    assert response.status_code == 201
    assert response.json()["objetivo"] == "Ganho de Massa Muscular"

def test_should_return_404_when_create_raises_lookup_error(client, mock_service):
    body_data = {
        "objetivo": "Treino de Força",
        "aluno_id": str(uuid.uuid4()),
        "instrutor_id": str(uuid.uuid4())
    }
    mock_service.create.side_effect = LookupError("Aluno não encontrado.")

    resp = client.post("/fichas-treino/", json=body_data)

    assert resp.status_code == 404
    assert resp.json()["detail"] == "Aluno não encontrado."

def test_should_return_ficha_treino_by_id(client, mock_service):
    ficha_id = uuid.uuid4()
    mock_service.find_by_id.return_value = {
        "id": str(ficha_id),
        "objetivo": "Condicionamento Físico",
        "aluno_id": str(uuid.uuid4()),
        "instrutor_id": str(uuid.uuid4())
    }

    res = client.get(f"/fichas-treino/{ficha_id}")

    assert res.status_code == 200
    assert res.json()["objetivo"] == "Condicionamento Físico"

def test_should_return_404_when_ficha_not_found_by_id(client, mock_service):
    fake_id = uuid.uuid4()
    mock_service.find_by_id.return_value = None

    response = client.get(f"/fichas-treino/{fake_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Ficha de treino não encontrada."

def test_should_update_ficha_treino_successfully(client, mock_service):
    ficha_id = uuid.uuid4()
    req_payload = {
        "objetivo": "Resistência Muscular",
        "aluno_id": str(uuid.uuid4()),
        "instrutor_id": str(uuid.uuid4())
    }
    mock_service.update.return_value = {
        "id": str(ficha_id),
        "objetivo": "Resistência Muscular",
        "aluno_id": req_payload["aluno_id"],
        "instrutor_id": req_payload["instrutor_id"]
    }

    response = client.put(f"/fichas-treino/{ficha_id}", json=req_payload)

    assert response.status_code == 200
    assert response.json()["objetivo"] == "Resistência Muscular"

def test_should_delete_ficha_treino_successfully(client, mock_service):
    target_id = uuid.uuid4()
    mock_service.delete.return_value = None

    resp = client.delete(f"/fichas-treino/{target_id}")

    assert resp.status_code == 204
    mock_service.delete.assert_called_once_with(target_id)