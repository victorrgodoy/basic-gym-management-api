from fastapi import FastAPI
import app.domain
from app.controller.aluno_controller import router as aluno_router
from app.controller.instrutor_controller import router as instrutor_router
from app.controller.administrador_controller import router as administrador_router
from app.controller.check_in_controller import router as check_in_router

app = FastAPI(title="Basic Gym Management API")

app.include_router(aluno_router)
app.include_router(instrutor_router)
app.include_router(administrador_router)
app.include_router(check_in_router.router)
app.include_router(instrutor_router)
