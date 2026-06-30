import uuid

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator
)


class ItemTreinoCreateRequest(BaseModel):
    exercicio_id: uuid.UUID
    series: int = Field(gt=0)
    repeticoes: int = Field(gt=0)
    observacao: str | None = None

    @field_validator("observacao")
    @classmethod
    def validar_observacao(cls, value: str | None) -> str | None:
        if value is None:
            return None

        observacao = value.strip()

        if not observacao:
            return None

        if len(observacao) > 500:
            raise ValueError(
                "A observação não pode ter mais de 500 caracteres."
            )

        return observacao


class ItemTreinoUpdateRequest(BaseModel):
    exercicio_id: uuid.UUID | None = None
    series: int | None = Field(default=None, gt=0)
    repeticoes: int | None = Field(default=None, gt=0)
    observacao: str | None = None

    @field_validator("observacao")
    @classmethod
    def validar_observacao(cls, value: str | None) -> str | None:
        if value is None:
            return None

        observacao = value.strip()

        if not observacao:
            return None

        if len(observacao) > 500:
            raise ValueError(
                "A observação não pode ter mais de 500 caracteres."
            )

        return observacao

    @model_validator(mode="after")
    def validar_campos_para_atualizacao(self):
        if not self.model_fields_set:
            raise ValueError(
                "Informe pelo menos um campo para atualizar o item de treino."
            )

        return self


class ItemTreinoResponse(BaseModel):
    id: uuid.UUID
    ficha_treino_id: uuid.UUID
    exercicio_id: uuid.UUID
    series: int
    repeticoes: int
    observacao: str | None

    model_config = ConfigDict(from_attributes=True)