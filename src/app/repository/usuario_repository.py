import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.usuario import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def find_by_id(self, usuario_id: uuid.UUID) -> Optional[Usuario]: 
        """Busca qualquer usuário pelo ID. Devolve Aluno, Instrutor ou Administrador."""
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Usuario]:
        """Busca por e-mail (usado principalmente no login)."""
        pass
    
    @abstractmethod
    def create(self, usuario: Usuario) -> Usuario:
        """Salva um Usuário, Aluno ou Instrutor no banco."""
        pass

    @abstractmethod 
    def update(self, usuario: Usuario) -> Usuario:
        """Atualiza os dados de qualquer tipo de usuário."""
        pass
    
    @abstractmethod 
    def delete(self, usuario_id: uuid.UUID) -> None: 
        """Deleta um usuário do banco de dados."""
        pass
