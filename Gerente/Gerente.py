import PySimpleGUI as sg
from Menu.TelasMenu import *
from Consultas.TelaConsulta import *
from Consultas.FuncoesConsulta import *
from Consultas.Consultas import *
from Gerente.TelasGerente import *
from Gerente.RegistroProduto import *
from Menu.TelasMenu import *
6
#-------------- menu --------------------#

def gerente(conexao, cur, janela):
    while True: #Loop da janela de login 
        escolha, valores = janela.read()
        
        #-------------- se o usuário quiser sair --------------------#
        if escolha == sg.WINDOW_CLOSED or escolha == "sairG":
            janela.close()
            janela = janela_login() 
            break

        #--------- se o usuário quiser fazer consultas -----------#

        elif escolha == "consultas":
            janela.close()
            janela = janela_consultas()
            while conexao != False:
                consultas(conexao, cur, janela)
                break


            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break                  
            

        #--------- se o usuário quiser inserir produto -----------#

        elif escolha == "inserir_produto":
            janela.close()
            janela = janela_inserirProduto()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break
                if escolha == "registrado":
                    sucesso = RegistraProduto(cur, conexao, valores)
                    if sucesso:
                        janela["confirmacao"].update("Produto inserido!", visible=True)
                    else:
                        janela["confirmacao"].update("Ocorreu um erro. Tente inserir o produto novamente!", visible=True)
                        janela.close()
                        janela = janela_inserirProduto()
                    

        #--------- se o usuário quiser inserir item -----------#

        elif escolha == "inserir_item":
            janela.close()
            janela = janela_inserirItem()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break
                if escolha == "registrado":
                    sucesso = InserirItens(cur, conexao, valores)
                    if sucesso:
                        janela["confirmacao"].update("Item inserido!", visible=True)
                    else:
                        janela["confirmacao"].update("Ocorreu um erro. Tente inserir o item novamente!", visible=True)
                        janela.close()
                        janela = janela_inserirItem()
                    
        #--------- se o usuário quiser deletar cliente -----------#

        elif escolha == "deletar_cliente":
            janela.close()
            janela = janela_deletarCliente()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break
                if escolha == "deletado":
                    DeletaCliente(cur, conexao, valores)
                    janela["confirmacao"].update("Cliente deletado com sucesso!", visible=True)

                    
                    
        #--------- se o usuário quiser deletar item -----------#

        elif escolha == "deletar_item":
            janela.close()
            janela = janela_deletarItem()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break
                if escolha == "deletado":
                    DeletaItem(cur, conexao, valores)
                    janela["confirmacao"].update("Item deletado com sucesso!", visible=True)


        #--------- se o usuário quiser deletar produto -----------#

        elif escolha == "deletar_produto":
            janela.close()
            janela = janela_deletarProduto()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # se o usuário quiser sair
                    janela.close()
                    janela = janela_gerente()
                    break
                elif escolha == "deletado":
                    DeletaProduto(cur, conexao, valores)
                    janela["confirmacao"].update("Produto deletado com sucesso!", visible=True)



                    