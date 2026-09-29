from fastapi import FastAPI
from routes.AdiministradorRoutes import Adiministrador_router
from routes.AlunoRoutes import Aluno_router


app = FastAPI(
    title="Minha API",
    description="API de exemplo com FastAPI",
    version="1.0.0"
)

app.include_router(Adiministrador_router)
app.include_router(Aluno_router)

