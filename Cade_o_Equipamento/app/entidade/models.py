from sqlmodel import Field, SQLModel,Relationship
from enum import Enum
from typing import Optional

class Adiministrador(SQLModel, table=True):
    __tablename__="adiministrador"
    id: int | None = Field(default=None,primary_key=True)
    nome: str =Field(max_length=50)
    telefone: str =Field(max_length=50)
    email: str =Field(max_length=50)

class Aluno(SQLModel, table=True):
    __tablename__="aluno"
    id: int | None = Field(default=None,primary_key=True)
    nome: str =Field(max_length=50)
    serie: int 
    email: str =Field(max_length=50)
    telefone: str =Field(max_length=50)
    periudo: str =Field(max_length=15)
    senha: str =Field(max_length=255)






