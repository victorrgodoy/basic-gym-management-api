import uuid
from pydantic import BaseModel, EmailStr, field_validator

def checar_nome(value: str) -> str:
    if not value or not value.strip():
        raise ValueError("O nome não pode ser vazio.")
    if len(value) > 100:
        raise ValueError("O nome não pode ter mais de 100 caracteres.")
    if not all(c.isalpha() or c.isspace() for c in value):
        raise ValueError("O nome deve conter apenas letras e espaços.")
    return value

def checar_senha(value: str) -> str:
    if len(value) < 6:
        raise ValueError("A senha deve ter pelo menos 6 caracteres.")
    if not any(c.isupper() for c in value):
        raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(c.islower() for c in value):
        raise ValueError("A senha deve conter pelo menos uma letra minúscula.")
    if not any(c.isdigit() for c in value):
        raise ValueError("A senha deve conter pelo menos um número.")
    if not any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in value):
        raise ValueError("A senha deve conter pelo menos um caractere especial.")
    return value

class UsuarioBaseRequest(BaseModel):
    nome: str
    email: EmailStr  
    senha: str

    @field_validator("nome")
    def validar_nome(cls, value: str) -> str:
        return checar_nome(value)

    @field_validator("senha")
    def validar_senha(cls, value: str) -> str:
        return checar_senha(value)