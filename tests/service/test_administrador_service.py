import pytest
from unittest.mock import MagicMock
from app.service.administrador_service import AdministradorService

@pytest.fixture
def repo_mock():
    return MagicMock()

@pytest.fixture
def user_service_mock():
    return MagicMock()

@pytest.fixture
def service(repo_mock, user_service_mock):
    return AdministradorService(
        administrador_repository=repo_mock,
        usuario_service=user_service_mock
    )

def test_should_create_administrator_successfully(service, repo_mock, user_service_mock):
    admin_mock = MagicMock()
    user_service_mock.find_by_email.return_value = None
    repo_mock.find_by_cpf.return_value = None
    repo_mock.create.return_value = admin_mock
    
    res = service.create(admin_mock)
    
    assert res == admin_mock
    repo_mock.create.assert_called_once_with(admin_mock)

def test_should_raise_value_error_when_email_already_exists(service, user_service_mock):
    admin_mock = MagicMock()
    admin_mock.email = "coordenacao@academia.com"
    user_service_mock.find_by_email.return_value = admin_mock
    
    with pytest.raises(ValueError) as exc:
        service.create(admin_mock)
        
    assert str(exc.value) == "Administrador com esse email já existe."