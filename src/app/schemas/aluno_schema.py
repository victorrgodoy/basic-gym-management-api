import uuid

from pydantic import BaseModel, EmailStr, field_validator


class AlunoRequest(BaseModel):
    nome: str
    email: str
    cpf: str

    @field_validator("nome")
    def validar_nome(cls, value: str) -> str:
        if not value:
            raise ValueError("O nome não pode ser vazio.")
        if len(value) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("O nome deve conter apenas letras e espaços.")
        return value

    @field_validator("email")
    def validar_email(cls, value: str) -> str:
        if not value:
            raise ValueError("O email não pode ser vazio.")
        if len(value) > 100:
            raise ValueError("O email não pode ter mais de 100 caracteres.")
        if "@" not in value or "." not in value:
            raise ValueError("O email deve conter '@' e '.'.")
        return value

    @field_validator("cpf")
    def validar_cpf(cls, value: str) -> str:
        if not value:
            raise ValueError("O CPF não pode ser vazio.")
        cpf = value.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. Use o formato 000.000.000-00.")
        return value


class AlunoResponse(BaseModel):
    id: uuid.UUID
    nome: str
    email: str
    cpf: str
    ativo: bool

    class Config:
        from_attributes = True