from sqlmodel import Session,select
from entidade.models import Aluno
from sqlalchemy.exc import OperationalError,IntegrityError
from pydantic import ValidationError
def cadastrar_aluno(db: Session, received_aluno: Aluno):
    try:
        aluno = Aluno.model_validate(received_aluno)
        db.add(aluno)
        db.commit()
        db.refresh(aluno)
    except ValidationError as e:
        return aluno
        raise ValueError("Verifique os dados informados") from e
    except OperationalError as e:
        db.rollback()
        raise RuntimeError("Falha de conexão com o banco de dados ao tentar cadastrar o aluno.") from e
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Esta aluno já está cadastrada no sistema.") from e

    

def buscar_todos_Aluno(db:Session):
    try:
        statement = select(Aluno)
        result = db.exec(statement).all()
        return result
    except OperationalError as e:
        db.rollback()
        raise RuntimeError("Falha de conexão com o banco de dados ao tentar buscar aluno.") from e

def deletar_aluno(db: Session, id: int):
        try:
            Aluno = db.get(Aluno, id)
            if not Aluno:
                raise KeyError(f"Aluno não encontrada.")
            
            db.delete(Aluno)
            db.commit()
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError("Não é possível deletar este Aluno pois existem equipamentos vinculados a ele.") from e
            
        except OperationalError as e:
            db.rollback()
            raise RuntimeError("Falha de comunicação com o banco de dados.") from e

def atualizar_aluno(db: Session, id: int, dados_atualizados: Aluno) -> Aluno:
        try:
            
            aluno = db.get(Aluno, id)
            if not Aluno:
                raise KeyError(f"Aluno informado não localizada.")
        
            aluno_data = dados_atualizados.model_dump(exclude_unset=True)
            for key, value in aluno_data.items():
                setattr(Aluno, key, value)
            
            db.add(Aluno)
            db.commit()
            db.refresh(Aluno)
            
            return Aluno
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError("Erro de integridade nos dados fornecidos.") from e
            
        except OperationalError as e:
            db.rollback()
            raise RuntimeError("Falha de comunicação com o banco de dados.") from e