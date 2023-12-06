--------------------- Trigger para criptografar senha --------------------------------

CREATE TRIGGER Criptografia
BEFORE INSERT
ON ClienteWeb
FOR EACH ROW
SET NEW.senha = SHA2(NEW.senha, 256);


--------------------- Trigger para atualizar o estoque pós pedido --------------------------------

DELIMITER //

CREATE TRIGGER AtualizaPosPedido
AFTER UPDATE ON Pedido
FOR EACH ROW
BEGIN
    IF NEW.statusPedido = 'Pago' AND OLD.statusPedido != 'Pago' THEN
        UPDATE Produto
        SET estoque = estoque - (
            SELECT quantidade
            FROM Item, Pedido
            WHERE idPedido = NEW.idPedido
              AND idProduto = produto.idProduto
        )
        WHERE idProduto IN (
            SELECT idProduto
            FROM Item
            WHERE idPedido = NEW.idPedido
        );
    END IF;
END;
//


--------------------- Trigger para atualizar o estoque pós cancelamento --------------------------------#
DELIMITER //

CREATE PROCEDURE Update_After_Cancel(IN newStatusPedido VARCHAR(255), IN oldStatusPedido VARCHAR(255), IN newIdPedido INT)
BEGIN
    IF newStatusPedido = 'cancelado' AND oldStatusPedido != 'cancelado' THEN
        UPDATE Produto
        SET estoque = estoque + (
            SELECT quantidade
            FROM Item
            WHERE idPedido = newIdPedido
              AND idProduto = Produto.idProduto
        )
        WHERE idProduto IN (
            SELECT idProduto
            FROM Item
            WHERE idPedido = newIdPedido
        );
    END IF;
END;
//


--------------------- Trigger para calcular preço total do produto por qtd --------------------------------#

DELIMITER //

CREATE TRIGGER CalcularPrecoTotal
BEFORE INSERT ON item
FOR EACH ROW
BEGIN
    DECLARE valorUnitario DECIMAL(10, 2);
    DECLARE total DECIMAL(10, 2);

    SELECT precoUnid FROM Produto WHERE idProduto = NEW.idProduto INTO valorUnitario;
    
    SET total = NEW.quantidade * valorUnitario;
    
    SET NEW.precoTotal = total;
END
//



--------------------- Trigger para atualizar preço de cada pedido --------------------------------#

DELIMITER //

CREATE TRIGGER AtualizaPrecoPedido
AFTER INSERT ON Item
FOR EACH ROW
BEGIN
    -- Calculate the new total value for the order
    DECLARE newTotal DECIMAL(10, 2);
    
    SELECT SUM(precoTotal) INTO newTotal
    FROM Item
    WHERE idPedido = NEW.idPedido;

    -- Update the order_total in the orders table
    UPDATE Pedido
    SET valorTotal = newTotal
    WHERE idPedido = NEW.idPedido;
END;
//
--------------------- Trigger para criar o carrinho de uma conta nova ----------------------------#

DELIMITER //

CREATE TRIGGER GerarCarrinho
AFTER INSERT ON Conta
FOR EACH ROW
BEGIN
    DECLARE Conta_id INTEGER;

    SET Conta_id = NEW.idConta;
    
    INSERT INTO CarrinhoDeCompras (idCarrinho, idConta) values (Conta_id, Conta_id);

END

//

DELIMITER ;