import pytest
from unittest.mock import MagicMock
import uuid
from app.service.ficha_treino_service import FichaTreinoService

@pytest.fixture
def ficha_repo(): return MagicMock()

@pytest.fixture
def aluno_repo(): return MagicMock()

@pytest.fixture
def instrutor_repo(): return MagicMock()

@pytest.fixture
def service(ficha_repo, aluno_repo, instrutor_repo):
    return FichaTreinoService(
        ficha_treino_repository=ficha_repo,
        aluno_repository=aluno_repo,
        instrutor_repository=instrutor_repo
    )

def test_should_create_ficha_treino_successfully(service, ficha_repo, aluno_repo, instrutor_repo):
    ficha_mock = MagicMock()
    aluno_repo.find_by_id.return_value = MagicMock()
    instrutor_repo.find_by_id.return_value = MagicMock()
    ficha_repo.create.return_value = ficha_mock

    res = service.create(ficha_mock)

    assert res == ficha_mock
    ficha_repo.create.assert_called_once_with(ficha_mock)

def test_should_raise_lookup_error_when_aluno_not_found(service, aluno_repo):
    target_ficha = MagicMock()
    aluno_repo.find_by_id.return_value = None

    with pytest.raises(LookupError) as exc:
        service.create(target_ficha)
    assert str(exc.value) == "Aluno não encontrado."

def test_should_raise_lookup_error_when_instrutor_not_found(service, aluno_repo, instrutor_repo):
    target_ficha = MagicMock()
    aluno_repo.find_by_id.return_value = MagicMock()
    instrutor_repo.find_by_id.return_value = None

    with pytest.raises(LookupError) as exc:
        service.create(target_ficha)
    assert str(exc.value) == "Instrutor não encontrado."

def test_should_raise_lookup_error_on_update_when_ficha_not_found(service, ficha_repo):
    invalid_id = uuid.uuid4()
    ficha_repo.find_by_id.return_value = None

    with pytest.raises(LookupError) as exc:
        service.update(invalid_id, objetivo="Hipertrofia")
    assert str(exc.value) == "Ficha de treino não encontrada."

def test_should_update_ficha_treino_properties_successfully(service, ficha_repo, aluno_repo, instrutor_repo):
    id_ficha = uuid.uuid4()
    id_aluno = uuid.uuid4()
    id_inst = uuid.uuid4()
    
    mock_obj = MagicMock()
    ficha_repo.find_by_id.return_value = mock_obj
    aluno_repo.find_by_id.return_value = MagicMock()
    instrutor_repo.find_by_id.return_value = MagicMock()
    ficha_repo.update.return_value = mock_obj

    res = service.update(id_ficha, objetivo="Emagrecimento e Cardio", aluno_id=id_aluno, instrutor_id=id_inst)

    assert res == mock_obj
    mock_obj.alterar_objetivo.assert_called_once_with("Emagrecimento e Cardio")
    ficha_repo.update.assert_called_once_with(mock_obj)

def test_should_raise_lookup_error_on_delete_when_ficha_not_found(service, ficha_repo):
    ficha_id = uuid.uuid4()
    ficha_repo.find_by_id.return_value = None

    with pytest.raises(LookupError) as exc:
        service.delete(ficha_id)
    assert str(exc.value) == "Ficha de treino não encontrada."

def test_should_delete_ficha_treino_successfully(service, ficha_repo):
    target_id = uuid.uuid4()
    mock_ficha = MagicMock()
    ficha_repo.find_by_id.return_value = mock_ficha

    service.delete(target_id)
    ficha_repo.delete.assert_called_once_with(mock_ficha)