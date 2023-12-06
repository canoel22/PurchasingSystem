import PySimpleGUI as sg
from getpass import getpass
from tabulate import tabulate
from Verificacoes.Verificacoes import *
from Consultas.TelaConsulta import*
import os

#--------------------- Todos os pedidos associados a uma conta --------------------------------#
def PedidosAssociados(conexao, cur, id_conta):

    sql = '''SELECT idPedido
        FROM Pedido
        WHERE Pedido.idConta = %s;
        '''
    
    cur.execute(sql, (id_conta,))
    resultado = cur.fetchall()

    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    layout = [
        [sg.Text('Pedidos')],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('Consulta de Pedidos', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_consulta1()
            break

#--------------------- Todos os produtos contidos em um determinado carrinho --------------------------------#

def ProdutosNoCarrinho(conexao, cur, id_carrinho):


    sql = '''SELECT idProduto
        FROM Item, ItemCarrinhoDeCompras
        WHERE Item.idItem = ItemCarrinhoDeCompras.idItem
        AND ItemCarrinhoDeCompras.idCarrinho = %s;
        '''
    
    cur.execute(sql, (id_carrinho,))
    resultado = cur.fetchall()

    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    layout = [
        [sg.Text('Produtos no carrinho')],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_consulta2()
            break



#--------------------- Dados e qtd dos usuários cadastrados no sistema --------------------------------#

def DadosUsuarios(conexao, cur): 

    sql = '''SELECT idCliente, nome
    FROM Usuario;
    '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados

def QtdUsuarios(conexao, cur): 

    sql = '''SELECT COUNT(idCliente) AS quantidade
    FROM Usuario;
    '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados



#--------------------- Forma de pagamento mais utilizada --------------------------------#

def PgtoMaisUsado(conexao, cur): 

    sql = ''' SELECT COUNT(*) AS QtdPagamentos, formaPagamento
    FROM Pagamento
    GROUP BY formaPagamento
    HAVING COUNT(*) >= ALL (
            SELECT COUNT(*) AS QtdPagamentos
            FROM Pagamento
            GROUP BY formaPagamento);
    '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados


#--------------------- Filtrar usuários por bairro, cidade e estado --------------------------------#

def FiltroEndereco(conexao, cur, bairro_desejado, cidade_desejada, estado_desejado): 

    sql = '''
    SELECT nome, idCliente
    FROM Usuario u
    WHERE u.bairro = %s AND u.cidade = %s AND u.estado = %s;
    '''

    cur.execute(sql, (bairro_desejado, cidade_desejada, estado_desejado))
    resultado = cur.fetchall()


    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')
 
    layout = [
        [sg.Text('Clientes nesse endereço')],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_consulta5()
            break


#--------------------- Média anual de vendas --------------------------------#

def MediaAnualDeVenda(conexao, cur, ano_desejado): 


    sql = ''' SELECT AVG(valorTotal) AS MediaAnualDeVenda
    FROM Pedido
    WHERE YEAR(data) = %s;
    '''
    
    cur.execute(sql,(ano_desejado,))
    resultado = cur.fetchall()

    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    layout = [
        [sg.Text('Média anual de vendas')],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_consulta6()
            break


#--------------------- Mês e ano com maior número de vendas --------------------------------#

def MaiorVendas(conexao, cur): 


    sql = ''' SELECT YEAR(data) AS Ano, MONTH(data) AS Mes, COUNT(*) AS NumeroDeVendas
    FROM Pedido
    GROUP BY YEAR(data), MONTH(data)
    HAVING COUNT(*) >= ALL (
        SELECT COUNT(*)
        FROM Pedido
        GROUP BY YEAR(data), MONTH(data));
    '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados
    
#--------------------- Usuários que realizaram compras em todos os meses de um determinado ano --------------------------------#

def TodosMeses(conexao, cur, ano_desejado): 


    sql = '''SELECT idCliente
    FROM (
        SELECT idCliente, YEAR(data) AS Ano, MONTH(data) AS Mes
        FROM Pedido
        JOIN ClienteWeb ON Pedido.idConta = ClienteWeb.idCliente
        GROUP BY idCliente, YEAR(data), MONTH(data)) AS VendasPorCliente
    WHERE Ano = %s
    GROUP BY idCliente
    HAVING COUNT(DISTINCT Mes) = 12;
    '''
    
    cur.execute(sql, (ano_desejado,))
    resultado = cur.fetchall()

    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    layout = [
        [sg.Text('Usuários que realizaram compras em todos os meses nesse ano')],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button('Fechar')]
    ]
    janela = sg.Window('', layout)

    while True:
        event, valores = janela.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            janela.close()
            janela = janela_consulta8()
            break


#--------------------- Quantidade de usuários por status --------------------------------#

def UsuariosPorStatus(conexao, cur): 


    sql = ''' SELECT statusCliente, COUNT(*) AS QuantidadeDeUsuarios
    FROM ClienteWeb
    GROUP BY statusCliente;
    '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados

#--------------------- Produto mais vendido --------------------------------#
def MaisVendido(conexao, cur): 

    sql = '''SELECT Produto.idProduto, Produto.nomeProduto, COUNT(*) AS QuantidadeVendida
    FROM Item
    JOIN Produto ON Item.idProduto = Produto.idProduto
    GROUP BY Produto.idProduto, Produto.nomeProduto
    HAVING COUNT(*) >= ALL (
        SELECT COUNT(*)
        FROM Item
        GROUP BY idProduto
);

 '''
    
    cur.execute(sql)
    resultado = cur.fetchall()
    dados_formatados = tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql')

    return dados_formatados
