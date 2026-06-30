import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
from app.request.usuario_request import UsuarioBaseRequest, checar_nome, checar_senha

def checar_cref(value: str) -> str:
    if not value:
        raise ValueError("O CREF não pode ser vazio.") 
    cref_limpo = value.replace(".", "").replace("-", "").replace("/", "").strip()
    if len(cref_limpo) < 6 or not cref_limpo[:6].isdigit():
        raise ValueError("CREF inválido. Use o formato 000000-X ou 0000000-X.")
        
    return value

class InstrutorCreateRequest(UsuarioBaseRequest):
    cref: str

    @field_validator("cref")
    def validar_cref(cls, v): return checar_cref(v)

class InstrutorUpdateRequest(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None

    @field_validator("nome")
    def validar_nome(cls, v):
        return checar_nome(v) if v is not None else v

    @field_validator("senha")
    def validar_senha(cls, v):
        return checar_senha(v) if v is not None else v
