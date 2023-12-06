
def RegistraProduto(cur, conexao, valores):

    sql = "insert into Produto (nomeProduto, estoque, precoUnid) values (%s, %s, %s);"
    cur.execute(sql, (valores["nomeProduto"], valores["estoque"], valores["precoUnid"]))
    idProd = cur.lastrowid
    conexao.commit()

    return idProd

def InserirItens(cur, conexao, valores):

    sql = "insert into Item (idProduto, quantidade) values (%s, %s);"
    cur.execute(sql, (valores["idProduto"], valores["quantidade"]))
    idItem = cur.lastrowid
    conexao.commit()

    return idItem


def DeletaCliente(cur, conexao, valores):

    sql = "delete from ClienteWeb where idCliente = %s"
    cur.execute(sql, (valores["idCliente"],))
    conexao.commit()

    sql = "delete from Usuario where idCliente = %s"
    cur.execute(sql, (valores["idCliente"],))
    conexao.commit()

    return


def DeletaProduto(cur, conexao, valores): #Deleta também todos os itens associados a este produto

    sql = "delete from Item where idProduto = %s"
    cur.execute(sql, (valores["idProduto"],))
    conexao.commit()

    sql = "delete from Produto where idProduto = %s"
    cur.execute(sql, (valores["idProduto"],))
    conexao.commit()

    return
    

def DeletaItem(cur, conexao, valores):

    sql = "delete from Item where idItem = %s"
    cur.execute(sql, (valores["idItem"],))
    conexao.commit()

    return
