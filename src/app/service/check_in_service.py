import uuid
from typing import List
from app.domain.check_in import CheckIn
from app.repository.sqlalchemy.sqlalchemy_check_in_repository import SqlAlchemyCheckInRepository
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository

class CheckInService:
    def __init__(self, check_in_repository: SqlAlchemyCheckInRepository, usuario_repository: SqlAlchemyUsuarioRepository):
        self.__check_in_repository = check_in_repository
        self.__usuario_repository = usuario_repository

    def create(self, aluno_id: uuid.UUID) -> CheckIn:
        aluno = self.__usuario_repository.find_by_id(aluno_id)
        if not aluno or aluno.tipo != "aluno":
            raise ValueError("Apenas usuários do tipo aluno podem fazer check-in.")
        
        novo_check_in = CheckIn(aluno_id=aluno_id)
        return self.__check_in_repository.create(novo_check_in)

    def read_by_aluno(self, aluno_id: uuid.UUID) -> List[CheckIn]:
        return self.__check_in_repository.find_by_aluno_id(aluno_id)

    def read_all(self) -> List[CheckIn]:
        return self.__check_in_repository.read()