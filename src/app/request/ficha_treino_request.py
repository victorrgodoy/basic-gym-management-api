import uuid

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from typing import Optional

class FichaTreinoCreateRequest(BaseModel):
    objetivo: str
    aluno_id: uuid.UUID
    instrutor_id: uuid.UUID

    @field_validator("objetivo")
    @classmethod
    def validar_objetivo(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("O objetivo da ficha não pode ser vazio.")

        if len(value.strip()) > 200:
            raise ValueError(
                "O objetivo da ficha não pode ter mais de 200 caracteres."
            )

        return value.strip()


class FichaTreinoUpdateRequest(BaseModel):
    objetivo: Optional[str] = None
    aluno_id: Optional[uuid.UUID] = None
    instrutor_id: Optional[uuid.UUID] = None

    @field_validator("objetivo")
    @classmethod
    def validar_objetivo(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value

        if not value.strip():
            raise ValueError("O objetivo da ficha não pode ser vazio.")

        if len(value.strip()) > 200:
            raise ValueError(
                "O objetivo da ficha não pode ter mais de 200 caracteres."
            )

        return value.strip()

    @model_validator(mode="after")
    def validar_alteracao(self):
        if (
            self.objetivo is None
            and self.aluno_id is None
            and self.instrutor_id is None
        ):
            raise ValueError(
                "Informe pelo menos um campo para atualizar a ficha."
            )

        return self


class FichaTreinoResponse(BaseModel):
    id: uuid.UUID
    objetivo: str
    aluno_id: uuid.UUID
    instrutor_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)