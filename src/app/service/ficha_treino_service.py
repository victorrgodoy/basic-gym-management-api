import uuid

from typing import Optional

from app.domain.ficha_treino import FichaTreino
from app.repository.aluno_repository import AlunoRepository
from app.repository.ficha_treino_repository import FichaTreinoRepository
from app.repository.instrutor_repository import InstrutorRepository


class FichaTreinoService:

    def __init__(
        self,
        ficha_treino_repository: FichaTreinoRepository,
        aluno_repository: AlunoRepository,
        instrutor_repository: InstrutorRepository
    ):
        self.__ficha_treino_repository = ficha_treino_repository
        self.__aluno_repository = aluno_repository
        self.__instrutor_repository = instrutor_repository

    def find_by_id(
        self,
        ficha_treino_id: uuid.UUID
    ) -> Optional[FichaTreino]:
        return self.__ficha_treino_repository.find_by_id(
            ficha_treino_id
        )

    def read(self) -> list[FichaTreino]:
        return self.__ficha_treino_repository.read()

    def create(self, ficha_treino: FichaTreino) -> FichaTreino:
        self.__validar_aluno(ficha_treino.aluno_id)
        self.__validar_instrutor(ficha_treino.instrutor_id)

        return self.__ficha_treino_repository.create(ficha_treino)

    def update(
        self,
        ficha_treino_id: uuid.UUID,
        objetivo: Optional[str] = None,
        aluno_id: Optional[uuid.UUID] = None,
        instrutor_id: Optional[uuid.UUID] = None
    ) -> FichaTreino:
        ficha_treino = self.find_by_id(ficha_treino_id)

        if not ficha_treino:
            raise LookupError("Ficha de treino não encontrada.")

        if objetivo is not None:
            ficha_treino.alterar_objetivo(objetivo)

        if aluno_id is not None:
            self.__validar_aluno(aluno_id)
            ficha_treino.aluno_id = aluno_id

        if instrutor_id is not None:
            self.__validar_instrutor(instrutor_id)
            ficha_treino.instrutor_id = instrutor_id

        return self.__ficha_treino_repository.update(ficha_treino)

    def delete(self, ficha_treino_id: uuid.UUID) -> None:
        ficha_treino = self.find_by_id(ficha_treino_id)

        if not ficha_treino:
            raise LookupError("Ficha de treino não encontrada.")

        self.__ficha_treino_repository.delete(ficha_treino)

    def __validar_aluno(self, aluno_id: uuid.UUID) -> None:
        aluno = self.__aluno_repository.find_by_id(aluno_id)

        if not aluno:
            raise LookupError("Aluno não encontrado.")

    def __validar_instrutor(self, instrutor_id: uuid.UUID) -> None:
        instrutor = self.__instrutor_repository.find_by_id(instrutor_id)

        if not instrutor:
            raise LookupError("Instrutor não encontrado.")