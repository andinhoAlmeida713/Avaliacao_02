from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from dependencies.dependencies import database
from controllers.AuthController import fazer_login

auth_routes = APIRouter()

@auth_routes.post("/auth/login")
def login(
    email: str = Form(...),  # Lê o input name="email" do HTML
    senha: str = Form(...),  # Lê o input name="senha" do HTML
    db: Session = Depends(database.get_db)
):
    try:
        # Executa a sua validação no banco de dados
        info_login = fazer_login(db, email, senha)
        role_usuario = info_login.get("role")

        # Redirecionamento estrito em Python baseado no cargo
        if role_usuario == "administrador":
            return RedirectResponse(url="/administrador", status_code=status.HTTP_303_SEE_OTHER)
        
        elif role_usuario == "aluno":
            return RedirectResponse(url="/pedido-estoque", status_code=status.HTTP_303_SEE_OTHER)
        
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sem permissão.")

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
