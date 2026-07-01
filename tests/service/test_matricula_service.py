import pytest
from unittest.mock import MagicMock
import uuid
from app.service.matricula_service import MatriculaService

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return MatriculaService(matricula_repository=mock_repo)

def test_should_create_matricula_successfully(service, mock_repo):
    data_mock = MagicMock()
    mock_repo.create.return_value = data_mock

    result = service.create(data_mock)

    assert result == data_mock
    mock_repo.create.assert_called_once_with(data_mock)

def test_should_raise_value_error_when_matricula_is_none(service):
    with pytest.raises(ValueError) as err:
        service.create(None)
    assert str(err.value) == "Matricula não pode ser nula."

def test_should_activate_matricula_successfully(service, mock_repo):
    id_val = uuid.uuid4()
    mock_obj = MagicMock()
    mock_repo.find_by_id.return_value = mock_obj
    mock_repo.update.return_value = mock_obj

    res = service.ativar(id_val)

    assert res == mock_obj
    mock_obj.ativar_matricula.assert_called_once()
    mock_repo.update.assert_called_once_with(mock_obj)

def test_should_raise_value_error_on_activation_when_not_found(service, mock_repo):
    bad_id = uuid.uuid4()
    mock_repo.find_by_id.return_value = None

    with pytest.raises(ValueError) as err:
        service.ativar(bad_id)
    assert str(err.value) == "Matrícula não encontrada."

def test_should_deactivate_matricula_successfully(service, mock_repo):
    target_id = uuid.uuid4()
    mock_item = MagicMock()
    mock_repo.find_by_id.return_value = mock_item
    mock_repo.update.return_value = mock_item

    res = service.desativar(target_id)

    assert res == mock_item
    mock_item.desativar_matricula.assert_called_once()
    mock_repo.update.assert_called_once_with(mock_item)

def test_should_raise_value_error_on_deactivation_when_not_found(service, mock_repo):
    missing_id = uuid.uuid4()
    mock_repo.find_by_id.return_value = None

    with pytest.raises(ValueError) as err:
        service.desativar(missing_id)
    assert str(err.value) == "Matrícula não encontrada."