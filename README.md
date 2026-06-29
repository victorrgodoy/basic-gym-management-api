# Basic Gym Management API
Esta API foi desenvolvida para gerenciar o fluxo operacional de uma academia, cobrindo desde o controle de acessos (Alunos, Instrutores, Admins) até o mapeamento de treinos e check-ins.

## Modelo de Domínio

O design da arquitetura e o relacionamento entre as entidades seguem o diagrama de classes mapeado em:
> `docs/modelo.jpeg`

---

## Rodar o projeto

## Requisitos
- Python 3.9+
- Docker e Docker Compose

## Instalação

### 1. Clonar o projeto
```bash
git clone <url-do-repo>
cd basic-gym-management-api
```

### 2. Criar e ativar o ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com base .env.example:

### 4. Subir o banco de dados
```bash
docker-compose up -d
```

### 5. Rodar as migrations
```bash
alembic upgrade head
```

### 6. Iniciar o servidor
```bash
uvicorn src.main:app --reload
```

## Documentação
Acesse `http://localhost:8000/docs` para ver e testar os endpoints via Swagger.

## Migrations

### Gerar nova migration
```bash
alembic revision --autogenerate -m "descricao_da_migration"
```

### Aplicar migrations
```bash
alembic upgrade head
```

### Reverter última migration
```bash
alembic downgrade -1
```

### Ver histórico de migrations
```bash
alembic history
```