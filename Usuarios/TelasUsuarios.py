import PySimpleGUI as sg

# MENU PRINCIPAL DO USUARIO
def janela_usuarios():
    sg.theme('BluePurple')
    layout_usuarios = [
        [sg.Text("Sua Conta", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Seu Carrinho", size=(30, 1), button_color=("white", "#4682B4"), key="ver_carrinho", pad=((0, 0), (10, 10)))],
        [sg.Button("Seus Pedidos", size=(30, 1), button_color=("white", "#4682B4"), key="ver_pedidos", pad=((0, 0), (10, 10)))],
        [sg.Button("Ver Produtos", size=(30, 1), button_color=("white", "#4682B4"), key="ver_produtos", pad=((0, 0), (10, 10)))],
        [sg.Button("Sair", size=(12, 1), button_color=("white", "#4682B4"), key="sair", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Sua Conta", layout_usuarios, background_color="white", element_justification='c')

# OPCOES DO CARRINHO
def janela_seu_carrinho():
    sg.theme('BluePurple')
    layout_seu_carrinho = [
        [sg.Text("Seu Carrinho", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Ver Produtos no Carrinho", size=(30, 1), button_color=("white", "#4682B4"), key="prod_carrinho", pad=((0, 0), (10, 10)))],
        [sg.Button("Mover do Carrinho aos Pedidos", size=(30, 1), button_color=("white", "#4682B4"), key="carrinho_to_pedido", pad=((0, 0), (10, 10)))],
        [sg.Button("Remover Item do Carrinho", size=(30, 1), button_color=("white", "#4682B4"), key="remove_carrinho", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Seu Carrinho", layout_seu_carrinho, background_color="white", element_justification='c')


def janela_pedido_carrinho():
    sg.theme('BluePurple')
    layout_pedido_carrinho = [
        [sg.Text("Mover itens para Pedidos", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idItem', default_text='ID do Item')],
        [sg.InputText(key='idPedido', default_text='ID do Pedido')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Concluir', size=(16, 2), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Mover para Pedidos", layout_pedido_carrinho, background_color="white", element_justification='c')

def janela_remove_carrinho():
    sg.theme('BluePurple')
    layout_remove_carrinho = [
        [sg.Text("Remover Item do Carrinho", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idItem', default_text='ID do Item')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Concluir', size=(16, 2), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Remover Item", layout_remove_carrinho, background_color="white", element_justification='c')


# OPÇÕES DOS PEDIDOS
def janela_seus_pedidos():
    sg.theme('BluePurple')
    layout_seus_pedidos = [
        [sg.Text("Seus Pedidos", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Ver Pedidos", size=(30, 1), button_color=("white", "#4682B4"), key="lista_pedidos", pad=((0, 0), (10, 10)))],
        [sg.Button("Realizar Pagamento", size=(30, 1), button_color=("white", "#4682B4"), key="pagar_pedido", pad=((0, 0), (10, 10)))],
        [sg.Button("Cancelar Pedido", size=(30, 1), button_color=("white", "#4682B4"), key="cancela_pedido", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Seus Pedidos", layout_seus_pedidos, background_color="white", element_justification='c')

# IMPLEMENTAR JANELA DE VER PEDIDOS

def janela_pagamento():
    sg.theme('BluePurple')
    layout_pagamento = [
        [sg.Text("Pagamento de Pedido", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='metodo', default_text='Metodo de Pagamento')],
        [sg.InputText(key='idPedido', default_text='ID do Pedido')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Concluir', size=(16, 2), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Pagamento", layout_pagamento, background_color="white", element_justification='c')

def janela_cancela_pedido():
    sg.theme('BluePurple')
    layout_cancela_pedido = [
        [sg.Text("Cancelar Pedido", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idPedido', default_text='ID do Pedido')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Concluir', size=(16, 2), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Cancelar Pedido", layout_cancela_pedido, background_color="white", element_justification='c')



# OPÇÕES DOS PRODUTOS
def janela_produtos():
    sg.theme('BluePurple')
    layout_produtos = [
        [sg.Text("Produtos em Estoque", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Lista de Produtos", size=(30, 1), button_color=("white", "#4682B4"), key="lista_produtos", pad=((0, 0), (10, 10)))],
        [sg.Button("Adicionar aos Pedidos", size=(30, 1), button_color=("white", "#4682B4"), key="add_pedido", pad=((0, 0), (10, 10)))],
        [sg.Button("Adicionar ao Carrinho", size=(30, 1), button_color=("white", "#4682B4"), key="add_carrinho", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Produtos em Estoque", layout_produtos, background_color="white", element_justification='c')

# IMPLEMENTAR JANELA DE VER PEDIDOS

def janela_adiciona_produto_pedido():
    sg.theme('BluePurple')
    layout_adiciona_produto_pedido = [
        [sg.Text("Adicionar Item a um Pedido", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idProduto', default_text='ID do Produto')],
        [sg.InputText(key='qtd', default_text='Quantidade')],
        [sg.InputText(key='idPedido', default_text='ID do Pedido')],
        [sg.Button("Ou crie um novo Pedido", key='novo_pedido', button_color=("white", "#4682B4"), size=(18, 1), pad=((0, 0), (0, 0)))],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 70), (25, 25))), sg.Button('Concluir', size=(6, 1), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Adicionar a um Pedido", layout_adiciona_produto_pedido, background_color="white", element_justification='c')

def janela_adiciona_produto_carrinho():
    sg.theme('BluePurple')
    layout_adiciona_produto_pedido = [
        [sg.Text("Adicionar Item ao Carrinho", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idProduto', default_text='ID do Produto')],
        [sg.InputText(key='qtd', default_text='Quantidade')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Concluir', size=(16, 2), button_color=("white", "#4682B4"), key="concluido")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]   
    ]
    return sg.Window("Adicionar a um Carrinho", layout_adiciona_produto_pedido, background_color="white", element_justification='c')


def janela_listarProdutos(dados_formatados):
    layout_listarProdutos = [
        [sg.Text("Produtos", size=(60, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(60, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Lista de produtos", layout_listarProdutos, background_color="white", element_justification='c')



def janela_listarProdutosCarrinho(dados_formatados):
    layout_listarProdutos = [
        [sg.Text("Produtos no carrinho", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Multiline(dados_formatados, size=(90, 10), disabled=True)],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=(((0, 0), (20, 15))))]
    ]
    return sg.Window("Produtos no carrinho", layout_listarProdutos, background_color="white", element_justification='c')


def janela_listarProdutosPedido():
    layout_listarpedido = [
        [sg.Text("Digite o id do pedido:", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.InputText(key='idPedido', default_text='')], 
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Buscar', size=(16, 2), button_color=("white", "#4682B4"), key="buscado")]
    ]
    return sg.Window("Listar produtos no pedidos", layout_listarpedido, background_color="white", element_justification='c')




