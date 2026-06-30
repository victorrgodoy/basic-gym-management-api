from app.repository.usuario_repository import UsuarioRepository
import uuid
from app.domain.usuario import Usuario
from typing import Optional
from app.request.administrador_request import AdministradorUpdate
from app.request.instrutor_request import InstrutorUpdate

class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.__usuario_repository = usuario_repository
    
    def find_by_id(self, id: uuid.UUID) -> Optional[Usuario]:
        if not id:
            raise ValueError("ID não pode ser nulo ou vazio.")
        return self.__usuario_repository.find_by_id(id)
    
    def find_by_email(self, email: str) -> Optional[Usuario]:
        if not email:
            raise ValueError("Email não pode ser nulo ou vazio.")
        return self.__usuario_repository.find_by_email(email)
    
    def create(self, usuario: Usuario) -> Usuario:
        if usuario is None:
            raise ValueError("Usuário não pode ser nulo.")
        if self.find_by_email(usuario.email):
            raise ValueError("Usuário com esse email já existe.")
        return self.__usuario_repository.create(usuario)
    
    def read(self, tipo: Optional[str] = None):
        return self.__usuario_repository.read(tipo=tipo)
    
    def update(self, usuario: Usuario) -> Usuario:
        if not self.find_by_id(usuario.id):
            raise ValueError("Usuário não encontrado.")
        return self.__usuario_repository.update(usuario)
    
    def delete(self, id: uuid.UUID) -> None:
        if not id:
            raise ValueError("ID não pode ser nulo ou vazio.")
        usuario = self.find_by_id(id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        self.__usuario_repository.delete(id)

    def update_administrador(self, id: uuid.UUID, dados: AdministradorUpdate) -> Optional[Usuario]:
        admin = self.find_by_id(id)
        if not admin or admin.tipo != "administrador":
            raise ValueError("Administrador não encontrado.")
        
        admin.nome = dados.nome
        admin.email = dados.email
        if dados.senha:
            admin.senha = dados.senha

        return self.__usuario_repository.update(admin)