import uuid

class Aluno:

    def __init__(self, nome: str, email: str, cpf: str):
        self.__id = uuid.uuid4() 
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__ativo = True  

    def get_id(self) -> uuid.UUID:
        return self.__id
    
    def get_nome(self) -> str:
        return self.__nome
    
     def get_email(self) -> str:
        return self.__email

    def get_cpf(self) -> str:
        return self.__cpf
    
    def is_ativo(self) -> bool:
        return self.__ativo
    
    def alterar_nome(self, novo_nome: str) -> None:
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio.")

        if len(novo_nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")

        if not all(c.isalpha() or c.isspace() for c in novo_nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")

        self.__nome = novo_nome
    
    def alterar_email(self, novo_email: str) -> None:
        if not novo_email:
            raise ValueError("O email não pode ser vazio.")

        if len(novo_email) > 100:
            raise ValueError("O email não pode ter mais de 100 caracteres.")

        if "@" not in novo_email or "." not in novo_email:
            raise ValueError("O email deve conter '@' e '.'.")        

        self.__email = novo_email

    def desativar_matricula(self) -> None:
        if not self.__ativo:
            raise ValueError("O aluno já está inativo.")
        self.__ativo = False

    def ativar_matricula(self) -> None:
        if self.__ativo:
            raise ValueError("O aluno já está ativo.")
        self.__ativo = True

