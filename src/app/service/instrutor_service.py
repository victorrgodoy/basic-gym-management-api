import uuid
from typing import Optional
from app.domain.instrutor import Instrutor
from app.repository.instrutor_repository import InstrutorRepository
from app.service.usuario_service import UsuarioService

class InstrutorService:
    def __init__(
        self, 
        instrutor_repository: InstrutorRepository,
        usuario_service: UsuarioService
    ):
        self.__instrutor_repository = instrutor_repository
        self.__usuario_service = usuario_service

    def find_by_cref(self, cref: str) -> Optional[Instrutor]:
        if not cref:
            raise ValueError("CREF não pode ser nulo ou vazio.")
        return self.__instrutor_repository.find_by_cref(cref)

    def create(self, instrutor: Instrutor) -> Instrutor:
        if instrutor is None:
            raise ValueError("Instrutor não pode ser nulo.")
        if self.__usuario_service.find_by_email(instrutor.email):
            raise ValueError("Instrutor com esse email já existe.")
        if self.find_by_cref(instrutor.cref):
            raise ValueError("Instrutor com esse CREF já existe.")
        return self.__instrutor_repository.create(instrutor)

    def read(self):
        return self.__instrutor_repository.read()