from fastapi import FastAPI
import app.domain
from app.controller.aluno_controller import router as aluno_router
from app.controller.instrutor_controller import router as instrutor_router

app = FastAPI(title="Basic Gym Management API")

app.include_router(aluno_router)
app.include_router(instrutor_router)