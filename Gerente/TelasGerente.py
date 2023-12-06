import PySimpleGUI as sg

def janela_gerente():
    sg.theme('BluePurple')
    layout_gerente = [
        [sg.Text("Gerência do sistema", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Consultas", size=(30, 1), button_color=("white", "#4682B4"), key="consultas", pad=((0, 0), (10, 5)))],
        [sg.Button("Inserir novo produto", size=(30, 1), button_color=("white", "#4682B4"), key="inserir_produto", pad=((0, 0), (10, 10)))],
        [sg.Button("Inserir novo item", size=(30, 1), button_color=("white", "#4682B4"), key="inserir_item", pad=((0, 0), (10, 10)))],
        [sg.Button("Deletar cliente", size=(30, 1), button_color=("white", "#4682B4"), key="deletar_cliente", pad=((0, 0), (10, 10)))],
        [sg.Button("Deletar item", size=(30, 1), button_color=("white", "#4682B4"), key="deletar_item", pad=((0, 0), (10, 10)))],
        [sg.Button("Deletar produto", size=(30, 1), button_color=("white", "#4682B4"), key="deletar_produto", pad=((0, 0), (10, 10)))],
        [sg.Button("Sair", size=(12, 1), button_color=("white", "#4682B4"), key="sairG", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Menu gerente", layout_gerente, background_color="white", element_justification='c')


def janela_inserirProduto():
    sg.theme('BluePurple')
    layout_inserirProduto = [
        [sg.Text("Inserir produto", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idProduto', default_text='ID do Produto')], # idProduto é autoincrement, então n precisa de input né?
        [sg.InputText(key='nomeProduto', default_text='Nome do Produto')],
        [sg.InputText(key='estoque', default_text='Estoque')],
        [sg.InputText(key='precoUnid', default_text='Preço da unidade')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Registrar', size=(16, 2), button_color=("white", "#4682B4"), key="registrado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Inserir produto", layout_inserirProduto, element_justification= 'c')


def janela_inserirItem():
    sg.theme('BluePurple')
    layout_inserirProduto = [
        [sg.Text("Inserir item", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idItem', default_text='ID do Item')], # Mesmo caso que o comentario de cima
        [sg.InputText(key='quantidade', default_text='Quantidade')],
        [sg.InputText(key='idProduto', default_text='ID do produto a que está relacionado')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Registrar', size=(16, 2), button_color=("white", "#4682B4"), key="registrado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Inserir tem", layout_inserirProduto, element_justification= 'c')


def janela_deletarCliente():
    sg.theme('BluePurple')
    layout_deletarCliente = [
        [sg.Text("Deletar cliente", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idCliente', default_text='ID do cliente')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Deletar', size=(16, 2), button_color=("white", "#4682B4"), key="deletado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Deletar cliente", layout_deletarCliente, element_justification= 'c')

def janela_deletarItem():
    sg.theme('BluePurple')
    layout_deletarItem = [
        [sg.Text("Deletar item", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idItem', default_text='ID do item')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Deletar', size=(16, 2), button_color=("white", "#4682B4"), key="deletado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Deletar item", layout_deletarItem, element_justification= 'c')

def janela_deletarProduto():
    sg.theme('BluePurple')
    layout_deletarProduto = [
        [sg.Text("Deletar produto", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idProduto', default_text='ID do produto')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Deletar', size=(16, 2), button_color=("white", "#4682B4"), key="deletado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Deletar produto", layout_deletarProduto, element_justification= 'c')