from sqlmodel import Session
from db.db import database  # Ajuste conforme o nome do seu arquivo de banco/engine
from entidades.models import Adiministrador, Aluno
from core.security import hash_senha  # Sua função de criptografia de senha

def criar_usuarios_iniciais():
    engine = database.engine  
    
    with Session(engine) as session:
        print("Iniciando a inserção dos dados no banco...")

        # 1. Criando o Aluno (Usando os campos exatos do seu models.py)
        novo_aluno = Aluno(
            nome="João Aluno",
            serie=3,
            email="aluno@email.com",
            telefone="49999999999",
            periudo="Noturno",
            senha=hash_senha("123456")  # Salva a senha criptografada
        )

        # 2. Criando o Administrador
        # Nota: Como sua classe Adiministrador não tem o campo 'senha' no models.py,
        # se você tentar passar 'senha="123"', dará erro. Vamos inserir os campos existentes:
        novo_admin = Adiministrador(
            nome="Coordenador Almoxarifado",
            telefone="49988888888",
            email="admin@email.com"
        )

        session.add(novo_aluno)
        session.add(novo_admin)
        
        session.commit()
        print("✅ Dados criados com sucesso no banco de dados!")
        print("Aluno cadastrado -> E-mail: aluno@email.com | Senha: 123456")

if __name__ == "__main__":
    criar_usuarios_iniciais()
