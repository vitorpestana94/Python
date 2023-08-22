CREATE TABLE Clientes(
	cpf VARCHAR(11) PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	idade INT NOT NULL
);

CREATE TABLE Telefones(
	cpf_cliente VARCHAR(11) PRIMARY KEY,
	ddd VARCHAR(2) NOT NULL,
	telefone VARCHAR(9) NOT NULL,
	FOREIGN KEY (cpf_cliente) REFERENCES Clientes(cpf)

);