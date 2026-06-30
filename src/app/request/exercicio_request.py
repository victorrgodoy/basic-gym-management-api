import uuid

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from typing import Optional


class ExercicioCreateRequest(BaseModel):
    nome: str
    descricao: str

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("O nome do exercício não pode ser vazio.")

        if len(value.strip()) > 100:
            raise ValueError(
                "O nome do exercício não pode ter mais de 100 caracteres."
            )

        return value.strip()

    @field_validator("descricao")
    @classmethod
    def validar_descricao(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("A descrição do exercício não pode ser vazia.")

        if len(value.strip()) > 500:
            raise ValueError(
                "A descrição não pode ter mais de 500 caracteres."
            )

        return value.strip()


class ExercicioUpdateRequest(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value

        if not value.strip():
            raise ValueError("O nome do exercício não pode ser vazio.")

        if len(value.strip()) > 100:
            raise ValueError(
                "O nome do exercício não pode ter mais de 100 caracteres."
            )

        return value.strip()

    @field_validator("descricao")
    @classmethod
    def validar_descricao(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value

        if not value.strip():
            raise ValueError("A descrição do exercício não pode ser vazia.")

        if len(value.strip()) > 500:
            raise ValueError(
                "A descrição não pode ter mais de 500 caracteres."
            )

        return value.strip()

    @model_validator(mode="after")
    def validar_alteracao(self):
        if self.nome is None and self.descricao is None:
            raise ValueError(
                "Informe pelo menos nome ou descrição para atualizar."
            )

        return self


class ExercicioResponse(BaseModel):
    id: uuid.UUID
    nome: str
    descricao: str

    model_config = ConfigDict(from_attributes=True)