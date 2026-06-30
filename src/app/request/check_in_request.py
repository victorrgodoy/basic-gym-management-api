from pydantic import BaseModel
from uuid import UUID

class CheckInRequest(BaseModel):
    aluno_id: UUID