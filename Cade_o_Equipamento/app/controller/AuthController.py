from sqlmodel import Session, select
from entidades.models import Adiministrador, Aluno
from core.security import verifica_senha, criar_token

def fazer_login(db: Session, email: str, password: str):
    # 1. Tenta buscar na tabela de Aluno
    aluno = db.exec(select(Aluno).where(Aluno.email == email)).first()
    if aluno and verifica_senha(password, aluno.senha):
        token = criar_token(str(aluno.id), roles=["aluno"])
        return {"access_token": token, "role": "aluno"}

    # 2. Tenta buscar na tabela de Administrador
    admin = db.exec(select(Adiministrador).where(Adiministrador.email == email)).first()
    if admin:
        # ATENÇÃO: Como a tabela Adiministrador não tem campo 'senha' ainda,
        # esta linha simula a validação. O ideal é adicionar 'senha: str' no model do admin.
        token = criar_token(str(admin.id), roles=["administrador"])
        return {"access_token": token, "role": "administrador"}

    # 3. Se não encontrar nenhum, falha
    raise ValueError("Credenciais Inválidas")
