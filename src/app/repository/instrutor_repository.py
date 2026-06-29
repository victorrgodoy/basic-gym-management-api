import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.instrutor import Instrutor

class InstrutorRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Instrutor]:
        pass

    @abstractmethod
    def find_by_cref(self, cref: str) -> Optional[Instrutor]:
        pass

    @abstractmethod
    def create(self, instrutor: Instrutor) -> Instrutor:
        pass

    @abstractmethod
    def read(self) -> list[Instrutor]:
        pass