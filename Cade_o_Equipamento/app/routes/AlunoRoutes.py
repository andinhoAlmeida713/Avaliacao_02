from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from entidade.models import Aluno
from dependencies.dependencies import database
from controller.AlunoController import * 

Aluno_router = APIRouter()


@Aluno_router.get("/aluno",
                           response_model=list[Aluno],
                           status_code=status.HTTP_200_OK)
def listarAluno(db: Session = Depends(database.get_db)):
    try:
        categorias = buscar_todos_Aluno(db)
        return Aluno
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@Aluno_router.post("/aluno", 
                            status_code=status.HTTP_201_CREATED, 
                            response_model=Aluno)
def cadastrarAluno(aluno: Aluno, db: Session = Depends(database.get_db)):  
    try:
        aluno_cadastrado = cadastrar_aluno(db, aluno)
        return aluno_cadastrado
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@Aluno_router.put("/aluno/{id}", 
                           status_code=status.HTTP_200_OK, 
                           response_model=Aluno)
def atualizarAluno(id: int, dados_atualizados: Aluno, db: Session = Depends(database.get_db)):
    try:
        aluno_atualizado = atualizar_aluno(db, id, dados_atualizados)
        return aluno_atualizado
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@Aluno_router.delete("/aluno/{id}", 
                              status_code=status.HTTP_204_NO_CONTENT)
def deletarAluno(id: int, db: Session = Depends(database.get_db)):
    try:
        aluno(db, id)
        return None 
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
