import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.administrador import Administrador

class AdministradorRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Administrador]:
        pass
    
    @abstractmethod
    def create(self, administrador: Administrador) -> Administrador:
        pass
    
    @abstractmethod
    def read(self) -> list[Administrador]:
        pass