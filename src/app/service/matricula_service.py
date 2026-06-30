import uuid
from typing import Optional
from app.domain.matricula import Matricula
from app.repository.matricula_repository import MatriculaRepository

class MatriculaService:
    def __init__(
        self, 
        matricula_repository: MatriculaRepository
    ):
        self.__matricula_repository = matricula_repository

    def find_by_id(self, id: uuid.UUID) -> Optional[Matricula]:
        return self.__matricula_repository.find_by_id(id)

    def create(self, matricula: Matricula) -> Matricula:
        if matricula is None:
            raise ValueError("Matricula não pode ser nula.")
        return self.__matricula_repository.create(matricula)

    def read(self) -> list[Matricula]:
        return self.__matricula_repository.read()

    def ativar(self, matricula_id: uuid.UUID) -> Matricula:
        matricula = self.__matricula_repository.find_by_id(matricula_id)
        if not matricula:
            raise ValueError("Matrícula não encontrada.")
        matricula.ativar_matricula() 
        return self.__matricula_repository.update(matricula) 

    def desativar(self, matricula_id: uuid.UUID) -> Matricula:
        matricula = self.__matricula_repository.find_by_id(matricula_id)
        if not matricula:
            raise ValueError("Matrícula não encontrada.")
        
        matricula.desativar_matricula() 
        return self.__matricula_repository.update(matricula) 