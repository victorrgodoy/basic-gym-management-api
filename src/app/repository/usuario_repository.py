import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.usuario import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Usuario]: 
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Usuario]:
        pass
    
    @abstractmethod
    def create(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod 
    def read(self, tipo: Optional[str] = None) -> list[Usuario]:
        pass

    @abstractmethod 
    def update(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod 
    def delete(self, id: uuid.UUID) -> None: 
        pass