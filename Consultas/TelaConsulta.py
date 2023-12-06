import PySimpleGUI as sg
import time

def janela_consultas():
    sg.theme('BluePurple')
    layout_login = [
        [sg.Text("Consultas", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Todos os pedidos associados a uma conta", size=(50, 1), button_color=("white", "#4682B4"), key="PedidosAssociados", pad=((0, 0), (10, 5)))],
        [sg.Button("Todos os produtos contidos em um carrinho", size=(50, 1), button_color=("white", "#4682B4"), key="ProdutosNoCarrinho", pad=((0, 0), (10, 5)))],
        [sg.Button("Dados (e qtd) dos usuários cadastrados no sistema", size=(50, 1), button_color=("white", "#4682B4"), key="DadosUsuarios", pad=((0, 0), (10, 10)))],
        [sg.Button("Forma de pagamento mais utilizada", size=(50, 1), button_color=("white", "#4682B4"), key="PgtoMaisUsado", pad=((0, 0), (10, 10)))],
        [sg.Button("Filtro de usuário por bairro, cidade e estado", size=(50, 1), button_color=("white", "#4682B4"), key="FiltroEndereco", pad=((0, 0), (10, 10)))],
        [sg.Button("Média anual de vendas", size=(50, 1), button_color=("white", "#4682B4"), key="MediaAnualDeVenda", pad=((0, 0), (10, 10)))],
        [sg.Button("Mês e ano com maior número de vendas", size=(50, 1), button_color=("white", "#4682B4"), key="MaiorVendas", pad=((0, 0), (10, 10)))],
        [sg.Button("Usuários que compraram em todos os meses de um ano", size=(50, 1), button_color=("white", "#4682B4"), key="TodosMeses", pad=((0, 0), (10, 10)))],
        [sg.Button("Quantidade de usuários por status", size=(50, 1), button_color=("white", "#4682B4"), key="UsuariosPorStatus", pad=((0, 0), (10, 10)))],
        [sg.Button("Produto mais vendido", size=(50, 1), button_color=("white", "#4682B4"), key="MaisVendido", pad=((0, 0), (10, 10)))],
        [sg.Button("Sair", size=(12, 1), button_color=("white", "#4682B4"), key="sair", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Consultas", layout_login, background_color="white", element_justification='c')

def janela_consulta1():
    layout_consulta1 = [
        [sg.Text("Todos os pedidos associados a uma conta", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idConta', default_text='ID da conta desejada:')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Consulta 1", layout_consulta1, background_color="white", element_justification='c')


def janela_consulta2():
    layout_consulta2 = [
        [sg.Text("Todos os produtos contidos em um carrinho", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idCarrinho', default_text='ID do carrinho desejado:')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Consulta 2", layout_consulta2, background_color="white", element_justification='c')


def janela_consulta3(dados_formatados, qtd_formatadas):
    layout_consulta3 = [
        [sg.Text("Dados (e qtd) dos usuários cadastrados no sistema", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True), sg.Multiline(qtd_formatadas, size=(20, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Consulta 3", layout_consulta3, background_color="white", element_justification='c')


def janela_consulta4(dados_formatados):
    layout_consulta4 = [
        [sg.Text("Forma de pagamento mais utilizada", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Consulta 4", layout_consulta4, background_color="white", element_justification='c')


def janela_consulta5():
    layout_consulta5 = [
        [sg.Text("Filtro de usuário por bairro, cidade e estado", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='bairro', default_text='Bairro:')], 
        [sg.InputText(key='cidade', default_text='Cidade:')], 
        [sg.InputText(key='estado', default_text='Estado:')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Consulta 5", layout_consulta5, background_color="white", element_justification='c')


def janela_consulta6():
    layout_consulta6 = [
        [sg.Text("Média anual de vendas", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='ano', default_text='Ano:')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))),  sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Consulta 6", layout_consulta6, background_color="white", element_justification='c')


def janela_consulta7(dados_formatados):
    layout_consulta7 = [
        [sg.Text("Mês e ano com maior número de vendas", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Consulta 7", layout_consulta7, background_color="white", element_justification='c')


def janela_consulta8():
    layout_consulta8 = [
        [sg.Text("Usuários que realizaram compras em todos os meses de um determinado ano", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='ano', default_text='Ano:')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Consulta 2", layout_consulta8, background_color="white", element_justification='c')



def janela_consulta9(dados_formatados):
    layout_consulta9 = [
        [sg.Text("Quantidade de usuários por status", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Consulta 8", layout_consulta9, background_color="white", element_justification='c')


def janela_consulta10(dados_formatados):
    layout_consulta10 = [
        [sg.Text("Produto mais vendido", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Consulta 10", layout_consulta10, background_color="white", element_justification='c')
