from sqlmodel import Session,select
from entidade.models import Adiministrador
from sqlalchemy.exc import OperationalError,IntegrityError
from pydantic import ValidationError
def cadastrar_adiministrador(db: Session, received_categoria: Adiministrador):
    try:
        categoria = Adiministrador.model_validate(received_categoria)
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except ValidationError as e:
        raise ValueError("Verifique os dados informados") from e
    except OperationalError as e:
        db.rollback()
        raise RuntimeError("Falha de conexão com o banco de dados ao tentar cadastrar a categoria.") from e
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Esta categoria já está cadastrada no sistema.") from e

    

def buscar_todas_categoria_Adiministrador(db:Session):
    try:
        statement = select(Adiministrador)
        result = db.exec(statement).all()
        return result
    except OperationalError as e:
        db.rollback()
        raise RuntimeError("Falha de conexão com o banco de dados ao tentar buscar categorias.") from e

def deletar_adiministrador(db: Session, id: int):
        try:
            categoria = db.get(Adiministrador, id)
            if not categoria:
                raise KeyError(f"Adiministrador  não encontrada.")
            
            db.delete(categoria)
            db.commit()
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError("Não é possível deletar esta Adiministrador pois existem equipamentos vinculados a ela.") from e
            
        except OperationalError as e:
            db.rollback()
            raise RuntimeError("Falha de comunicação com o banco de dados.") from e

def atualizar_adiministrador(db: Session, id: int, dados_atualizados: Adiministrador) -> Adiministrador:
        try:
            
            adiministrador = db.get(Adiministrador, id)
            if not adiministrador:
                raise KeyError(f"Adiministrador informada não localizada.")
        
            categoria_data = dados_atualizados.model_dump(exclude_unset=True)
            for key, value in categoria_data.items():
                setattr(adiministrador, key, value)
            
            db.add(adiministrador)
            db.commit()
            db.refresh(adiministrador)
            
            return adiministrador
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError("Erro de integridade nos dados fornecidos.") from e
            
        except OperationalError as e:
            db.rollback()
            raise RuntimeError("Falha de comunicação com o banco de dados.") from e