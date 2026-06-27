from pydantic import field_validator
from app.request.usuario_request import UsuarioBaseRequest

class InstrutorRequest(UsuarioBaseRequest):
    cref: str

    @field_validator("cref")
    def validar_cref(cls, value: str) -> str:
        if not value:
            raise ValueError("O CREF não pode ficar vazio.")
        
        cref_limpo = value.strip().upper()
        
        if len(cref_limpo) > 20:
            raise ValueError("O CREF não pode ter mais de 20 caracteres.")
            
        if "-" not in cref_limpo:
            raise ValueError("CREF inválido. (Ex: 123456-G/SP).")
            
        return cref_limpo