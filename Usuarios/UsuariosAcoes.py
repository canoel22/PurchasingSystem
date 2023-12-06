import PySimpleGUI as sg
from getpass import getpass
from tabulate import tabulate
from Usuarios.TelaUsuarios import *

def PedirDoCarrinho(cur, conexao, valores, conta, janela): # valores = {['idItem'],['idPedido']}

    sql = '''select * from ItemCarrinhoDeCompras 
            where idItem = %s and idCarrinho = (
                select idCarrinho from CarrinhoDeCompras where idConta = %s
                )'''
    cur.execute(sql, (valores["idItem"], conta))
    verify = cur.fetchall()

    if verify == []:
        print("Este item não existe no seu carrinho de compras")
        return


    sql = "select * from Pedido where idPedido = %s and idConta = %s"
    cur.execute(sql, (valores["idPedido"], conta))
    verify = cur.fetchall()

    if verify == []:
        print("Este pedido não existe na sua conta")
        return

    sql = "delete from ItemCarrinhoDeCompras where idItem = %s"
    cur.execute(sql, (valores["idItem"],))
    conexao.commit()

    sql = "insert into ItemPedido (idItem, idPedido) values(%s,%s)"
    cur.execute(sql, (valores["idItem"], valores["idPedido"]))
    conexao.commit()

    print("Pedido inserido")
    janela["confirmacao"].update("Adicionado!", visible=True)
    


def RemoverDoCarrinho(cur, conexao, valor, conta, janela):

    sql = '''select * from ItemCarrinhoDeCompras
                where idItem = %s and idCarrinho = (
                    select idCarrinho from CarrinhoDeCompras
                        where idConta = %s
                )
          '''
    cur.execute(sql, (valor, conta))
    verify = cur.fetchall()
    

    if verify == []:
        print("Esse item não está no seu carrinho")
        #Mensagem de erro
        return

    print("Item removido")

    sql = '''delete from ItemCarrinhoDeCompras 
                where idItem = %s
                '''
    cur.execute(sql, (valor,))
    conexao.commit()

    sql = "delete from Item where idItem = %s"
    cur.execute(sql, (valor,))
    conexao.commit()
    janela["confirmacao"].update("Removido!", visible=True)

def PagarPedido(cur, conexao, valores, conta, janela):

    if valores["metodo"] != "Pix" and valores["metodo"] != "Cartao":
        print("Metodo de Pagamento invalido")
        janela["confirmacao"].update("Método de pagamento inválido!", visible=True)
        return

    sql = "select * from Pedido where idPedido = %s and idConta = %s"
    cur.execute(sql, (valores["idPedido"], conta))
    verify = cur.fetchone()

    print (verify)

    if verify is None:
        print("Esse pedido não existe na sua conta")
        return


    sql = "insert into Pagamento (formaPagamento, idPedido) values (%s, %s)"
    cur.execute(sql, (valores["metodo"], int(valores["idPedido"])))
    conexao.commit()

    sql = "update Pedido set statusPedido = 'Pago' where idPedido = %s"
    cur.execute(sql, (valores["idPedido"],))
    conexao.commit()
    janela["confirmacao"].update("Pago!", visible=True)

def CancelarPedido(cur, conexao, valor, conta, janela):

    sql = "delete from Item where idItem in (select idItem from ItemPedido where idPedido = %s);"
    cur.execute(sql, (valor,))
    conexao.commit()

    sql = "delete from ItemPedido where idPedido = %s;"
    cur.execute(sql, (valor,))
    conexao.commit()

    sql = "delete from Pedido where idPedido = %s;"
    cur.execute(sql, (valor,))
    conexao.commit()
    print("OK")
    janela["confirmacao"].update("Cancelado!", visible=True)
    

def AddCarrinho(cur, conexao, valores, conta, janela):

    sql = "insert into Item (quantidade, idProduto) values (%s, %s)"
    cur.execute(sql, (valores["qtd"], valores["idProduto"]))
    idItem = cur.lastrowid
    conexao.commit()

    sql = "select idCarrinho from CarrinhoDeCompras where idConta = %s"
    cur.execute(sql, (conta,))
    idCarrinho = cur.fetchone()

    print("ID do Carrinho: ", idCarrinho)

    sql = "insert into ItemCarrinhoDeCompras (idItem, idCarrinho) values(%s,%s)"
    cur.execute(sql, (idItem, idCarrinho))
    conexao.commit()
    janela["confirmacao"].update("Adicionado!", visible=True)


def AddPedido(cur, conexao, valores, idPedido, conta, janela):

    sql = "select * from Pedido where idPedido = %s and idConta = %s"
    cur.execute(sql, (idPedido, conta))
    verify = cur.fetchone()

    print (verify)

    if verify is None:
        print("Esse pedido não existe na sua conta")
        return


    sql = "SELECT idProduto FROM Produto WHERE idProduto = %s"
    cur.execute(sql, (valores["idProduto"],))
    produto_existente = cur.fetchone()

    if produto_existente is None:
        print("Este produto não existe.")
        return

    sql = "insert into Item (quantidade, idProduto, precoTotal) values (%s, %s, 0)"
    cur.execute(sql, (valores["qtd"], valores["idProduto"]))
    idItem = cur.lastrowid
    conexao.commit()

    sql = "insert into ItemPedido (idItem, idPedido) values(%s,%s)"
    cur.execute(sql, (idItem, idPedido))
    conexao.commit()

    print("Pedido inserido")
    janela["confirmacao"].update("Adicionado!", visible=True)

def InserirPedido(cur, conexão, conta):

    sql = "insert into Pedido (statusPedido, valorTotal,idConta, data) values(\"Vazio\", 0, %s, curdate())"
    cur.execute(sql, (conta,))

    idPedido = cur.lastrowid

    return idPedido

def MostrarProdutos(cur, conexao):

    sql = '''SELECT *
    FROM Produto;
    '''
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados

def MostrarItensCarrinho(cur, conexao, conta):

    sql = '''SELECT *
    FROM ItemCarrinhoDeCompras ic, Produto p, Item i
    WHERE ic.idCarrinho = %s and ic.idItem = i.idItem and i.idProduto = p.idProduto;
    '''
    
    cur.execute(sql, (conta,))
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados

def MostrarItensPedido(cur, conexao, idPedido, conta):
    sql = "select * from Pedido where idPedido = %s and idConta = %s"
    cur.execute(sql, (idPedido, conta))
    verify = cur.fetchone()

    print (verify)

    if verify is None:
        print("Esse pedido não existe na sua conta")
        return

    sql = '''SELECT *
    FROM ItemPedido ip, Produto p, Item i
    WHERE ip.idPedido = %s and ip.idItem = i.idItem and i.idProduto = p.idProduto;
    '''
    
    cur.execute(sql, (idPedido,))
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    layout = [
        [sg.Text('Itens no Pedidos')],
        [sg.Multiline(dados_formatados, size=(90, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('Itens no pedido', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_seus_pedidos()
            break
