-- Criação das tabelas 

CREATE TABLE funcionario (
    cpf INT PRIMARY KEY,
    nome VARCHAR(50),
    sobrenome VARCHAR(50),
    data_nascimento DATE,
    endereco VARCHAR(100),
    sexo CHAR(1),
    salario DECIMAL(10, 2),
    banco_codigo INT,
    agencia INT,
    conta VARCHAR(20),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

CREATE TABLE dependente (
    funcionario_cpf INT,
    nome VARCHAR(50),
    sexo CHAR(1),
    data_nascimento DATE,
    tipo_dependente VARCHAR(20),
    PRIMARY KEY (funcionario_cpf, nome),
    FOREIGN KEY (funcionario_cpf) REFERENCES funcionario(cpf)
);

CREATE TABLE departamento (
    id INT PRIMARY KEY,
    nome VARCHAR(50),
    gerente_cpf INT,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (gerente_cpf) REFERENCES funcionario(cpf)
);

CREATE TABLE localizacao_departamento (
    departamento_id INT,
    cidade VARCHAR(50),
    PRIMARY KEY (departamento_id, cidade),
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

CREATE TABLE projeto (
    nome VARCHAR(50) PRIMARY KEY,
    numero INT,
    cidade VARCHAR(50),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

CREATE TABLE trabalha_em (
    funcionario_cpf INT,
    projeto_nome VARCHAR(50),
    horas_trabalhadas DECIMAL(5, 2),
    PRIMARY KEY (funcionario_cpf, projeto_nome),
    FOREIGN KEY (funcionario_cpf) REFERENCES funcionario(cpf),
    FOREIGN KEY (projeto_nome) REFERENCES projeto(nome)
);

-- Inserção de dados

INSERT INTO funcionario VALUES 
(123456789, 'João', 'Silva', '1965-01-09', 'Rua das Flores, 123 - São Paulo - SP', 'M', 3000.00, 123, 4567, '0123456-7', 5),
(333445555, 'Maria', 'Santos', '1955-12-08', 'Avenida Central, 456 - Rio de Janeiro - RJ', 'F', 4000.00, 987, 6543, '7654321-0', 5),
(999887777, 'José', 'Oliveira', '1968-01-19', 'Rua das Palmeiras, 789 - Salvador - BA', 'M', 2500.00, 456, 3210, '9876543-2', 4);

INSERT INTO dependente VALUES 
(123456789, 'Ana', 'F', '1986-04-05', 'Filha'),
(333445555, 'Pedro', 'M', '1983-10-25', 'Filho'),
(333445555, 'Joana', 'F', '1958-05-03', 'Cônjuge');

INSERT INTO departamento VALUES 
(1, 'Pesquisa', 123456789, '1988-05-22', '1986-05-22'),
(2, 'Administração', 333445555, '1995-01-01', '1994-01-01');

INSERT INTO localizacao_departamento VALUES 
(1, 'São Paulo'),
(2, 'Rio de Janeiro');

INSERT INTO projeto VALUES 
('ProdutoX', 1, 'São Paulo', 1),
('ProdutoY', 2, 'Rio de Janeiro', 1),
('ProdutoZ', 3, 'São Paulo', 2);

INSERT INTO trabalha_em VALUES 
(123456789, 'ProdutoX', 32.5),
(333445555, 'ProdutoY', 40.0),
(999887777, 'ProdutoZ', 30.0);

-- Consultas SQL

SELECT * FROM funcionario;

SELECT cpf, COUNT(funcionario_cpf) FROM funcionario f JOIN dependente d ON f.cpf = d.funcionario_cpf GROUP BY cpf;

SELECT * FROM dependente;

SELECT data_nascimento, endereco FROM funcionario WHERE nome = 'João' AND sobrenome = 'Silva';

SELECT * FROM departamento WHERE nome = 'Pesquisa';

SELECT nome, sobrenome, endereco FROM funcionario f JOIN departamento d ON f.departamento_id = d.id WHERE d.nome = 'Pesquisa';

SELECT * FROM projeto;

SELECT nome AS Departamento, endereco AS Endereco FROM departamento d JOIN localizacao_departamento l ON d.id = l.departamento_id WHERE l.cidade = 'São Paulo';

SELECT * FROM projeto JOIN departamento ON departamento_id = departamento.id WHERE cidade = 'São Paulo';

SELECT numero AS Numero_Projeto, departamento_id AS ID_Departamento, nome AS Nome_Departamento, endereco AS Endereco, data_inicio AS Data_Inicio_Departamento FROM projeto JOIN departamento ON departamento_id = departamento.id JOIN localizacao_departamento ON departamento_id = localizacao_departamento.departamento_id WHERE cidade = 'São Paulo';

SELECT nome, sobrenome, endereco FROM funcionario JOIN departamento ON departamento_id = departamento.id WHERE nome = 'Pesquisa';

SELECT data_nascimento, endereco FROM funcionario WHERE nome = 'João' AND sobrenome = 'Silva';

SELECT nome, sobrenome, endereco FROM funcionario JOIN departamento ON departamento_id = departamento.id WHERE nome = 'Pesquisa';

SELECT nome, sobrenome, salario, salario * 0.11 AS INSS FROM funcionario;

SELECT f.nome, f.sobrenome, f.salario * 1.1 AS aumento_salario FROM funcionario f JOIN trabalha_em t ON f.cpf = t.funcionario_cpf JOIN projeto p ON t.projeto_nome = p.nome WHERE p.nome = 'ProdutoX';

SELECT d.nome AS Departamento, CONCAT(f.nome, ' ', f.sobrenome) AS Gerente FROM departamento d JOIN funcionario f ON d.gerente_cpf = f.cpf;

SELECT f.nome, f.sobrenome, f.endereco FROM funcionario f JOIN departamento d ON f.departamento_id = d.id WHERE d.nome = 'Pesquisa';
