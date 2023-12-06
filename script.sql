CREATE DATABASE IF NOT EXISTS compraOnline;

USE compraOnline;

CREATE TABLE IF NOT EXISTS Conta (
    idConta INT NOT NULL PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS Usuario (
    idCliente BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(2) NOT NULL,

    idConta INT NOT NULL,
    CONSTRAINT idConta_fk1 FOREIGN KEY (idConta) REFERENCES Conta(idConta) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ClienteWeb (
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(128) NOT NULL,
    statusCliente VARCHAR(50) NOT NULL,
    idCliente BIGINT NOT NULL,
    CONSTRAINT idCliente_fk1 FOREIGN KEY (idCliente) REFERENCES Usuario(idCliente) ON DELETE CASCADE,
    PRIMARY KEY (login, idCliente)
);

CREATE TABLE IF NOT EXISTS Atendido (
    telefone BIGINT NOT NULL,
    idCliente BIGINT NOT NULL,
    CONSTRAINT idCliente_fk2 FOREIGN KEY (idCliente) REFERENCES Usuario(idCliente) ON DELETE CASCADE,
    PRIMARY KEY (telefone, idCliente)
);


CREATE TABLE IF NOT EXISTS CarrinhoDeCompras (
    idCarrinho INT NOT NULL PRIMARY KEY,

    idConta INT NOT NULL,
    CONSTRAINT idConta_fk2 FOREIGN KEY (idConta) REFERENCES Conta(idConta) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Pedido (
    idPedido INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    statusPedido VARCHAR(50) NOT NULL,
    valorTotal INT NOT NULL,
    data DATE NOT NULL,

    idConta INT NOT NULL,
    CONSTRAINT idConta_fk3 FOREIGN KEY (idConta) REFERENCES Conta(idConta) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Produto (
    idProduto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomeProduto VARCHAR(50) NOT NULL,
    estoque INT NOT NULL,
    precoUnid INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Pagamento (
    idPagamento INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    formaPagamento VARCHAR(50) NOT NULL,

    idPedido INT NOT NULL,
    CONSTRAINT idPedido_fk1 FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Item (
    idItem INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    precoTotal DOUBLE(10,2) DEFAULT NULL,
    quantidade INT NOT NULL,

    idProduto INT NOT NULL,
    CONSTRAINT idProduto_fk1 FOREIGN KEY (idProduto) REFERENCES Produto(idProduto) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ItemPedido (
    idItem INT NOT NULL,
    idPedido INT NOT NULL,
    CONSTRAINT idItem_fk1 FOREIGN KEY (idItem) REFERENCES Item(idItem) ON DELETE CASCADE, 
    CONSTRAINT idPedido_fk2 FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido) ON DELETE CASCADE,
    PRIMARY KEY (idItem, idPedido)
);

CREATE TABLE IF NOT EXISTS ItemCarrinhoDeCompras (
    idItem INT NOT NULL,
    idCarrinho INT NOT NULL,
    CONSTRAINT idItem_fk2 FOREIGN KEY (idItem) REFERENCES Item(idItem) ON DELETE CASCADE, 
    CONSTRAINT idCarrinho_fk1 FOREIGN KEY (idCarrinho) REFERENCES CarrinhoDeCompras(idCarrinho) ON DELETE CASCADE,
    PRIMARY KEY (idItem, idCarrinho)
);
