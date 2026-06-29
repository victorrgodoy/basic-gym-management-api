import uuid
from typing import Optional
from app.domain.aluno import Aluno
from app.repository.aluno_repository import AlunoRepository
from app.service.usuario_service import UsuarioService

class AlunoService:
    def __init__(
        self, 
        aluno_repository: AlunoRepository,
        usuario_service: UsuarioService
    ):
        self.__aluno_repository = aluno_repository
        self.__usuario_service = usuario_service

    def find_by_cpf(self, cpf: str) -> Optional[Aluno]:
        if not cpf:
            raise ValueError("CPF não pode ser nulo ou vazio.")
        return self.__aluno_repository.find_by_cpf(cpf)

    def create(self, aluno: Aluno) -> Aluno:
        if aluno is None:
            raise ValueError("Aluno não pode ser nulo.")
        if self.__usuario_service.find_by_email(aluno.email):
            raise ValueError("Aluno com esse email já existe.")
        if self.find_by_cpf(aluno.cpf):
            raise ValueError("Aluno com esse CPF já existe.")
        return self.__aluno_repository.create(aluno)

    def read(self) -> list[Aluno]:
        return self.__aluno_repository.read()

    def update(self, aluno_id: uuid.UUID, dados) -> Aluno:
        usuario = self.__usuario_service.find_by_id(aluno_id)
        if not usuario:
            raise ValueError("Aluno não encontrado.")
        usuario.alterar_telefone(dados.telefone)
        usuario.alterar_nome(dados.nome)
        usuario.alterar_email(dados.email)
        usuario.alterar_senha(dados.senha)
        return self.__usuario_service.update(usuario)
    
    def delete(self, aluno_id: uuid.UUID) -> None:
        usuario = self.__usuario_service.find_by_id(aluno_id)
        self.__usuario_service.delete(aluno_id)
