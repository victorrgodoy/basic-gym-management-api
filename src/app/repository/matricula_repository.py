import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.matricula import Matricula

class MatriculaRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Matricula]:
        pass
    
    @abstractmethod
    def create(self, matricula: Matricula) -> Matricula:
        pass
    
    @abstractmethod
    def read(self) -> list[Matricula]:
        pass
    
    @abstractmethod
    def update(self, matricula: Matricula) -> Matricula:
        pass
        