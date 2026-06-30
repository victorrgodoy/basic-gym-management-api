import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
from app.request.usuario_request import UsuarioBaseRequest, checar_nome, checar_senha

def checar_telefone(value: str) -> str:
    if not value:
        raise ValueError("O telefone não pode ser vazio.")
    telefone = value.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) < 10 or len(telefone) > 11 or not telefone.isdigit():
        raise ValueError("Telefone inválido. Use o formato (00) 00000-0000 ou (00) 0000-0000.")
    return value

def checar_cpf(value: str) -> str:
    if not value:
        raise ValueError("O CPF não pode ser vazio.")
    cpf = value.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido. Use o formato 000.000.000-00.")
    return value


class AlunoCreateRequest(UsuarioBaseRequest):
    cpf: str
    telefone: str

    @field_validator("cpf")
    def validar_cpf(cls, v): return checar_cpf(v)

    @field_validator("telefone")
    def validar_telefone(cls, v): return checar_telefone(v)


class AlunoUpdateRequest(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None

    @field_validator("nome")
    def validar_nome(cls, v): 
        return checar_nome(v) if v is not None else v

    @field_validator("telefone")
    def validar_telefone(cls, v): 
        return checar_telefone(v) if v is not None else v

    @field_validator("senha")
    def validar_senha(cls, v): 
        return checar_senha(v) if v is not None else v