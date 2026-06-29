import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.aluno import Aluno

class AlunoRepository(ABC):

    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Optional[Aluno]: 
        pass
    
    @abstractmethod
    def create(self, aluno: Aluno) -> Aluno:
        pass
    
    @abstractmethod
    def read(self) -> list[Aluno]:
        pass