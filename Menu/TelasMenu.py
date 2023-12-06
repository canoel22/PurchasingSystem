import PySimpleGUI as sg


def janela_login():
    sg.theme('BluePurple')
    layout_login = [
        [sg.Text("Sistema de compras online", size=(30, 2), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Login como Cliente Web", size=(30, 2), button_color=("white", "#4682B4"), key="login_usuario", pad=((0, 0), (10, 5)))],
        [sg.Text("Registrar conta", size=(12, 1), text_color='#000080', enable_events=True, key="registrar_usuario", justification='center', pad=((0, 0),(0, 15)))],
        [sg.Button("Login por Atendente", size=(30, 2), button_color=("white", "#4682B4"), key="login_atendente", pad=((0, 0), (10, 10)))],
        [sg.Text("Registrar conta", size=(12, 1), text_color='#000080', enable_events=True, key="registrar_atendente", justification='center', pad=((0, 0),(0, 15)))],
        [sg.Button("Login como Gerente", size=(30, 2), button_color=("white", "#4682B4"), key="login_gerente", pad=((0, 0), (10, 10)))],
        [sg.Button("Sair", size=(12, 1), button_color=("white", "#4682B4"), key="sair", pad=((0, 0), (20, 15)))] 
    ]
    return sg.Window("Login", layout_login, background_color="white", element_justification='c')


def janela_login_usuario():
    sg.theme('BluePurple')
    layout_login_usuario = [
        [sg.Text("Login Usuário",text_color='blue', size=(20, 1), font=('Helvetica', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Input("Login", size=(30, 10), justification="center", key= "login")],
        [sg.Input("Senha", size=(30,10), justification="center", key= "senha")],
        [sg.Button("Logar", size=(30, 2), button_color=("white", "#4682B4"), key="usuario_logou", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))],
        [sg.Text("", size=(30, 2), text_color='red', key="mensagem_erro", justification='center', visible=False)]
    ]
    return sg.Window("Login usuário", layout_login_usuario, background_color="white", element_justification='c')

def janela_registrar_usuario():
    sg.theme('BluePurple')
    layout_registrar_usuario = [
        [sg.Text('Cadastro de Novo Usuário', font=('Helvetica', 25), justification='center', pad=((50,50), (20,20)))],
        [sg.InputText(key='nome', default_text='Nome')],
        [sg.InputText(key='login', default_text='Login')],
        [sg.InputText(key='senha', default_text='Senha')],
        [sg.InputText(key='cpf', default_text='CPF')],
        [sg.InputText(key='bairro', default_text='Bairro')],
        [sg.InputText(key='estado', default_text='Estado')],
        [sg.InputText(key='cidade', default_text='Cidade')],
        [sg.Button("Voltar", key='voltar', button_color=("white","#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Registrar', size=(16, 2), button_color=("white", "#4682B4"), key="registrado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Login de usuario", layout_registrar_usuario, element_justification= 'c')
    
def janela_login_atendente():
    sg.theme('BluePurple')
    layout_login_atendente = [
        [sg.Text("Login Atendente",text_color='blue', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Input("Telefone", size=(30, 10), justification="center", key= "telefone")],
        [sg.Input("Senha", size=(30,10), justification="center", key= "senha")],
        [sg.Button("Logar", size=(30, 2), button_color=("white", "#6495ED"), key="login", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))],
        [sg.Text("", size=(30, 2), text_color='red', key="mensagem_erro", justification='center', visible=False)]
    ]
    return sg.Window("Login atendente", layout_login_atendente, background_color="white", element_justification='c')

def janela_registrar_atendente():
    sg.theme('BluePurple')
    layout_registrar_atendente = [
        [sg.Text('Cadastro de Novo Usuário', font=('Helvetica', 25), justification='center', pad=((50,50), (20,20)))],
        [sg.InputText(key='nome', default_text='Nome')],
        [sg.InputText(key='telefone', default_text='Telefone')],
        [sg.InputText(key='cpf', default_text='CPF')],
        [sg.InputText(key='bairro', default_text='Bairro')],
        [sg.InputText(key='estado', default_text='Estado')],
        [sg.InputText(key='cidade', default_text='Cidade')],
        [sg.Button("Voltar", key='voltar', button_color=("white", "#4682B4"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Registrar', size=(16, 2), button_color=("white", "#4682B4"), key="registrado")],
        [sg.Text("", size=(30, 2), text_color='red', key="confirmacao", justification='center', visible=False)]
    ]
    return sg.Window("Login atendente", layout_registrar_atendente, element_justification= 'c')
    

def janela_login_gerente():
    sg.theme('BluePurple')
    layout_login_gerente = [
        [sg.Text("Login Gerente",text_color='blue', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Input("Login", size=(30, 10), justification="center", key= "loginG")],
        [sg.Input("Senha", size=(30,10), justification="center", key= "senhaG")],
        [sg.Button("Logar", size=(30, 2), button_color=("white", "#6495ED"), key="loginGerente", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "#4682B4"), key="voltar", pad=((0, 0), (20, 15)))],
        [sg.Text("", size=(30, 2), text_color='red', key="mensagem_erro", justification='center', visible=False)]
    ]
    return sg.Window("Login gerente", layout_login_gerente, background_color="white", element_justification='c')
