from app.request.usuario_request import UsuarioBaseRequest
from pydantic import BaseModel, EmailStr
from typing import Optional

class AdministradorRequest(UsuarioBaseRequest):

    pass

class AdministradorUpdate(BaseModel):
    nome: str
    email: EmailStr
    senha: Optional[str] = None
    pass