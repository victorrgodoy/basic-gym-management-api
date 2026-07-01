import pytest
from unittest.mock import MagicMock
import uuid
from main import app
from app.controller.matricula_controller import get_matricula_service

@pytest.fixture
def mock_service():
    return MagicMock()

@pytest.fixture(autouse=True)
def setup_routes(mock_service):
    app.dependency_overrides[get_matricula_service] = lambda: mock_service
    yield
    app.dependency_overrides.clear()

def test_should_create_matricula_successfully(client, mock_service):
    student_id = uuid.uuid4()
    mock_service.create.return_value = {
        "id": str(uuid.uuid4()),
        "aluno_id": str(student_id),
        "ativo": True
    }

    response = client.post(f"/matriculas/{student_id}")

    assert response.status_code == 201
    assert response.json()["ativo"] is True

def test_should_return_400_when_create_raises_value_error(client, mock_service):
    student_id = uuid.uuid4()
    mock_service.create.side_effect = ValueError("Aluno já possui matrícula ativa.")

    res = client.post(f"/matriculas/{student_id}")

    assert res.status_code == 400
    assert res.json()["detail"] == "Aluno já possui matrícula ativa."

def test_should_return_all_matriculas(client, mock_service):
    mock_service.read.return_value = [
        {"id": str(uuid.uuid4()), "ativo": True},
        {"id": str(uuid.uuid4()), "ativo": False}
    ]

    response = client.get("/matriculas/")

    assert response.status_code == 200
    assert len(response.json()) == 2

def test_should_activate_matricula_successfully(client, mock_service):
    sub_id = uuid.uuid4()
    mock_service.ativar.return_value = {"id": str(sub_id), "ativo": True}

    resp = client.patch(f"/matriculas/{sub_id}/ativar")

    assert resp.status_code == 200
    assert resp.json()["ativo"] is True

def test_should_return_400_on_activation_when_not_found(client, mock_service):
    missing_id = uuid.uuid4()
    mock_service.ativar.side_effect = ValueError("Matrícula não encontrada.")

    response = client.patch(f"/matriculas/{missing_id}/ativar")

    assert response.status_code == 400
    assert response.json()["detail"] == "Matrícula não encontrada."

def test_should_deactivate_matricula_successfully(client, mock_service):
    sub_id = uuid.uuid4()
    mock_service.desativar.return_value = {"id": str(sub_id), "ativo": False}

    resp = client.patch(f"/matriculas/{sub_id}/desativar")

    assert resp.status_code == 200
    assert resp.json()["ativo"] is False