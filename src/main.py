from fastapi import FastAPI


import app.domain
from app.controller.exercicio_controller import router as exercicio_router

from app.controller.aluno_controller import router as aluno_router
from app.controller.exercicio_controller import router as exercicio_router
from app.controller.ficha_treino_controller import router as ficha_treino_router

from app.controller.instrutor_controller import router as instrutor_router
from app.controller.administrador_controller import router as administrador_router
from app.controller.check_in_controller import router as check_in_router

app = FastAPI(title="Basic Gym Management API")

app.include_router(aluno_router)
app.include_router(exercicio_router)
app.include_router(ficha_treino_router)