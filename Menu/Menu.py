import PySimpleGUI as sg
from Menu.TelasMenu import *
from Verificacoes.Verificacoes import *
from Menu.RegistroUsuarios import *
from Gerente.TelasGerente import *
from Gerente.Gerente import *
from Usuarios.TelaUsuarios import *
from Usuarios.Usuarios import *
import time;

#-------------- menu --------------------#

def menu(conexao, cur, janela):
    should_exit = False
    while True: #Loop da janela de login 
        escolha, valores = janela.read()
        
        #-------------- se o usuário quiser sair --------------------#
        if escolha == sg.WINDOW_CLOSED or escolha == "sair":
            print(escolha)
            janela.close()
            should_exit = True
            break

        if should_exit:
            break
        #--------- se o usuário quiser logar como cliente web -----------#

        elif escolha == "login_usuario":
            janela.close()
            janela = janela_login_usuario()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_login()
                    break

                elif escolha == "usuario_logou": # Se o usuário clicar no botão "Login"
                    logado = LoginClienteWeb(cur, conexao, valores)

                    if(logado is None): #Verifica se o cliente já está cadastrado 
                        janela["mensagem_erro"].update("Login falhou! Cliente não cadastrado.", visible=True)

                    else:
                        janela.close()
                        janela = janela_usuarios()
                        while conexao != False:
                            usuarios(cur, conexao, janela, logado)
                            break

                        # chamar a janela do menu de cliente passando "logado" como a tupla do cliente logado

        #--------- se o usuário quiser se registrar como cliente web -----------#

        elif escolha == "registrar_usuario":
            janela.close()
            janela = janela_registrar_usuario()

            while True:
                escolha, valores = janela.read()
                if escolha == sg.WINDOW_CLOSED or escolha == "voltar":
                    janela.close()
                    janela = janela_login()
                    break
                elif escolha == 'registrado':
                    sucesso = RegistroClienteWeb(cur, conexao, valores)
                    if sucesso:
                        #mensagem de confirmacao
                        janela["confirmacao"].update("Registrado!", visible=True)
                        print("Sucesso")
                        idCliente_logado = valores["cpf"]
                    else:
                        # mensagem de erro
                        janela["confirmacao"].update("Erro! Uusuário já existe.", visible=True)

                   


        #--------- se o usuário quiser se logar por meio do atendente -----------#

        elif escolha == "login_atendente":
            janela.close()
            janela = janela_login_atendente()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_login()
                    break

                elif escolha == "login": # Se o usuário clicar no botão "Login"
                    telefoneUsuario = valores["telefone"]
                    senhaUsuarioA = valores["senha"]
                    logado = VerificaAtendente(cur, telefoneUsuario)
                    print(logado)
                    if(logado != None and senhaUsuarioA == "senhaAtendente" ): #Verifica se o cliente já está cadastrado (1 = NÃO)
                        janela.close()
                        janela = janela_usuarios()
                        while conexao != False:
                            usuarios(cur, conexao, janela, logado)
                            break
                    else:
                        janela["mensagem_erro"].update("Login falhou! Cliente não cadastrado.", visible=True)


        #--------- se o usuário quiser se registrar por meio do atendente -----------#

        elif escolha == "registrar_atendente":
            janela.close()
            janela = janela_registrar_atendente()

            while True:
                escolha, valores = janela.read()
                if escolha == sg.WINDOW_CLOSED or escolha == "voltar":
                    janela.close()
                    janela = janela_login()
                    break
                elif escolha == "registrado":
                    sucesso = RegistroAtendido(cur, conexao, valores)
                    if sucesso:
                        # mensagem de sucesso
                        janela["confirmacao"].update("Registrado!", visible=True)
                        idCliente_logado = valores["cpf"]
                    else:
                        # mensagem de erro
                        janela["confirmacao"].update("Erro! Uusuário já existe.", visible=True)


        #------------------------ se o gerente quiser logar -------------------------#

        elif escolha == "login_gerente":
            janela.close()
            janela = janela_login_gerente()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_login()
                    break

                elif escolha == "loginGerente": # Se o usuário clicar no botão "Login"
                    loginGerente = valores["loginG"]
                    senhaGerente = valores["senhaG"]

                    if loginGerente != "gerente" or senhaGerente != "senhaGerente": #Veerifica se o gerente já está cadastrado (1 = NÃO)
                        janela["mensagem_erro"].update("Login falhou! Dados incorretos.", visible=True) #Mensagem de erro pra gerente 
                    else:
                        janela.close()
                        janela = janela_gerente()
                        while conexao != False:
                            gerente(conexao, cur, janela)
                            break
            
