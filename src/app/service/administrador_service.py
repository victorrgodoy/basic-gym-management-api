import uuid
from typing import Optional
from app.domain.administrador import Administrador
from app.repository.administrador_repository import AdministradorRepository
from app.service.usuario_service import UsuarioService

class AdministradorService:
    def __init__(
        self, 
        administrador_repository: AdministradorRepository,
        usuario_service: UsuarioService
    ):
        self.__administrador_repository = administrador_repository
        self.__usuario_service = usuario_service

    def create(self, administrador: Administrador) -> Administrador:
        if administrador is None:
            raise ValueError("Administrador não pode ser nulo.")
        if self.__usuario_service.find_by_email(administrador.email):
            raise ValueError("Administrador com esse email já existe.")
        if self.__administrador_repository.find_by_cpf(administrador.cpf):
            raise ValueError("Administrador com esse CPF já existe.")
        return self.__administrador_repository.create(administrador)

    def read(self) -> list[Administrador]:
        return self.__administrador_repository.read()

    def update(self, administrador_id: uuid.UUID, dados) -> Administrador:
        administrador = self.__administrador_repository.find_by_id(administrador_id)
        if not administrador:
            raise ValueError("Administrador não encontrado.")
        if dados.nome is not None:
            administrador.alterar_nome(dados.nome)
        if dados.email is not None:
            administrador.alterar_email(dados.email)
        if dados.senha is not None:
            administrador.alterar_senha(dados.senha)
        return self.__usuario_service.update(administrador)

    def delete(self, administrador_id: uuid.UUID) -> None:
        self.__usuario_service.delete(administrador_id)
