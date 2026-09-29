from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from entidade.models import Adiministrador
from dependencies.dependencies import database
from controller.AdiministradorController import * 

Adiministrador_router = APIRouter()


@Adiministrador_router.get("/categorias",
                           response_model=list[Adiministrador],
                           status_code=status.HTTP_200_OK)
def listarCategorias(db: Session = Depends(database.get_db)):
    try:
        categorias = buscar_todas_categoria_Adiministrador(db)
        return categorias
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@Adiministrador_router.post("/categorias", 
                            status_code=status.HTTP_201_CREATED, 
                            response_model=Adiministrador)
def cadastrarCategoria(categoria: Adiministrador, db: Session = Depends(database.get_db)):  
    try:
        categoria_cadastrada = cadastrar_adiministrador(db, categoria)
        return categoria_cadastrada
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@Adiministrador_router.put("/categorias/{id}", 
                           status_code=status.HTTP_200_OK, 
                           response_model=Adiministrador)
def atualizarCategoria(id: int, dados_atualizados: Adiministrador, db: Session = Depends(database.get_db)):
    try:
        categoria_atualizada = atualizar_adiministrador(db, id, dados_atualizados)
        return categoria_atualizada
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@Adiministrador_router.delete("/categorias/{id}", 
                              status_code=status.HTTP_204_NO_CONTENT)
def deletarCategoria(id: int, db: Session = Depends(database.get_db)):
    try:
        deletar_adiministrador(db, id)
        return None  # Status 204 não retorna corpo na resposta
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
