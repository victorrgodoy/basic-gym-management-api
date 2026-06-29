import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.config.database import Base, DATABASE_URL  
from app.domain.usuario import Usuario
from app.domain.aluno import Aluno
from app.domain.instrutor import Instrutor
from app.domain.matricula import Matricula
from app.domain.administrador import Administrador

load_dotenv()
from app.domain.exercicio import Exercicio
from app.domain.ficha_treino import FichaTreino
from app.domain.item_treino import ItemTreino


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata 

def run_migrations_offline() -> None:
    config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    """Run migrations in 'offline' mode."""
    url = DATABASE_URL 
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    configuration = config.get_section(config.config_ini_section, {})
    
    configuration["sqlalchemy.url"] = DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()