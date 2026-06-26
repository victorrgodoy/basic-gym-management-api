# from app.repositories.aluno_repository import AlunoRepository
# import uuid
# from app.domains.aluno import Aluno
# from typing import Optional

# class AlunoService:
#     def __init__(self, aluno_repository: AlunoRepository):
#         self.__aluno_repository = aluno_repository

#     def find_by_id(self, id: uuid.UUID) -> Optional[Aluno]:
#         if not id:
#             raise ValueError("ID não pode ser nulo ou vazio.")
#         return self.__aluno_repository.find_by_id(id)
    
#     def create(self, aluno: Aluno) -> Aluno:
#         if aluno is None:
#             raise ValueError("Aluno não pode ser nulo.")
#         if self.find_by_id(aluno.get_id()):
#             raise ValueError("Aluno com esse ID já existe.")
#         return self.__aluno_repository.create(aluno)
    
#     def list_all(self) -> list[Aluno]:
#         return self.__aluno_repository.list_all()
    
#     def delete(self, id: uuid.UUID) -> None:
#         if not id:
#             raise ValueError("ID não pode ser nulo ou vazio.")
#         aluno = self.find_by_id(id)
#         if not aluno:
#             raise ValueError("Aluno não encontrado.")
#         self.__aluno_repository.delete(id)