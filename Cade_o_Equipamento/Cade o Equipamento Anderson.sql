create table adiministrador (
id INT auto_increment PRIMARY KEY,
nome varchar (50),
telefone varchar (20),
email varchar (50));

create table gestor (
id INT auto_increment PRIMARY KEY,
nome varchar (50),
telefone varchar (20),
email varchar (50),
setor varchar (30),
periudo varchar (15));

create table aluno (
id INT auto_increment PRIMARY KEY,
nome varchar (50),
serie INT,
email varchar (50),
telefone varchar (20),
periudo varchar (15));

create table equipamento (
id INT auto_increment PRIMARY KEY,
Nome_equipamento varchar (50),
estoque INT,
especificaçao varchar (50),
status varchar (15));

create table solicitacao_emprestimo (
id INT auto_increment PRIMARY KEY,
id_aluno INT NOT NULL,
id_equipamento INT NOT NULL,
data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_aluno) REFERENCES aluno (id),
FOREIGN KEY (id_equipamento) REFERENCES equipamento (id));

create table autorizacao_emprestimo (
id INT auto_increment PRIMARY KEY,
id_solicitacao_emprestimo INT NOT NULL,
id_gestor INT NOT NULL,
data_autorizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
data_devolucao Date NOT NULL,
FOREIGN KEY (id_solicitacao_emprestimo) REFERENCES solicitacao_emprestimo (id),
FOREIGN KEY (id_gestor) REFERENCES gestor (id));

create table devolucao_equipamento (
id INT auto_increment PRIMARY KEY,
id_autorizacao_emprestimo INT NOT NULL,
id_gestor INT NOT NULL,
data_devolucao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_autorizacao_emprestimo) REFERENCES autorizacao_emprestimo (id));
