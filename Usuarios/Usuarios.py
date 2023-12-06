import PySimpleGUI as sg
from Menu.TelasMenu import *
from Consultas.TelaConsulta import *
from Consultas.FuncoesConsulta import *
from Consultas.Consultas import *
from Usuarios.TelaUsuarios import *
from Usuarios.UsuarioAcoes import *

#-------------- menu --------------------#

def usuarios(cur, conexao, janela, idcon):

    conta = idcon[0] # id da Conta em que o usuário está logado

    while True:

        escolha, valores = janela.read()

        #-------------- se o usuário quiser sair --------------------#
        if escolha == sg.WINDOW_CLOSED or escolha == "sair": 
            break

        #-------------- se o usuário quiser ver seu carrinho --------------------#

        elif escolha == "ver_carrinho":
            janela.close()
            janela = janela_seu_carrinho()

            while True:
                escolha, valores = janela.read()

                # --- Voltar --- #
                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # voltar ao menu Usuario
                    janela.close()
                    janela = janela_usuarios()
                    break

                # --- Ver itens no Carrinho --- #
                elif escolha == "prod_carrinho":
                    janela.close()
                    dados_formatados = MostrarItensCarrinho(cur, conexao, conta)
                    janela = janela_listarProdutosCarrinho(dados_formatados)

                    while True:
                        event, valores = janela.read()

                        if event == sg.WIN_CLOSED or event == 'voltar':
                            janela.close()
                            janela = janela_seu_carrinho()
                            break


                # --- Pedir itens do carrinho --- #
                elif escolha == "carrinho_to_pedido":
                    janela.close()
                    janela = janela_pedido_carrinho()

                    while True:
                        escolha, valores = janela.read()
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar":
                            janela.close()
                            janela = janela_seu_carrinho()
                            break
                        elif escolha == "concluido":
                            PedirDoCarrinho(cur, conexao, valores, conta, janela)
                            

                # --- Remover item do carrinho --- #
                elif escolha == "remove_carrinho":
                    janela.close()
                    janela = janela_remove_carrinho()

                    while True:
                        escolha, valores = janela.read()
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar": 
                            janela.close()
                            janela = janela_seu_carrinho()
                            break
                        elif escolha == "concluido":
                            idItem = valores["idItem"]
                            RemoverDoCarrinho(cur, conexao, idItem, conta, janela)



        #-------------- se o usuário quiser ver seus pedidos --------------------#

        elif escolha == "ver_pedidos":
            janela.close()
            janela = janela_seus_pedidos()

            while True:
                escolha, valores = janela.read()
                
                # --- Voltar --- #
                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # voltar ao menu Usuario
                    janela.close()
                    janela = janela_usuarios()
                    break

                # --- Listar pedidos do usuário logado --- #
                elif escolha == "lista_pedidos":
                    janela.close()
                    janela = janela_listarProdutosPedido()

                    while True:
                        escolha, valores = janela.read()

                        if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                            janela.close()
                            janela = janela_seus_pedidos()
                            break  
                        elif escolha == 'buscado':
                            idPedido = valores['idPedido']
                            MostrarItensPedido(cur, conexao, idPedido, conta)


                # --- Pagar um pedido --- #
                elif escolha == "pagar_pedido":
                    janela.close()
                    janela = janela_pagamento()

                    while True:
                        escolha, valores = janela.read()
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar": 
                            janela.close()
                            janela = janela_seus_pedidos()
                            break
                        elif escolha == "concluido":
                            PagarPedido(cur, conexao, valores, conta, janela)


                # --- Cancelar um pedido --- #
                elif escolha == "cancela_pedido":
                    janela.close()
                    janela = janela_cancela_pedido()

                    while True:
                        escolha, valores = janela.read()
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar": 
                            janela.close()
                            janela = janela_seus_pedidos()
                            break
                        elif escolha == "concluido":
                            idPedido = valores["idPedido"]
                            CancelarPedido(cur, conexao, idPedido, conta, janela)
   

        #-------------- se o usuário quiser ver produtos em estoque --------------------#

        elif escolha == "ver_produtos":
            janela.close()
            janela = janela_produtos()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WINDOW_CLOSED or escolha == "voltar": # voltar ao menu Usuario
                    janela.close()
                    janela = janela_usuarios()
                    break

                elif escolha == "lista_produtos":
                    janela.close()
                    dados_formatados = MostrarProdutos(cur, conexao)
                    janela = janela_listarProdutos(dados_formatados)

                    while True:
                        event, valores = janela.read()

                        if event == sg.WIN_CLOSED or event == 'voltar':
                            janela.close()
                            janela = janela_produtos()
                            break

                # --- Adicionar um pedido --- #
                elif escolha == "add_pedido":
                    janela.close()
                    janela = janela_adiciona_produto_pedido()
                    
                    pop = False # Identificador do botão de Novo Pedido

                    while True:
                        escolha, valores = janela.read()

                        if not pop:
                            idPedido = valores["idPedido"]
                        
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar": 
                            janela.close()
                            janela = janela_produtos()
                            break

                        elif escolha == "novo_pedido":
                            if not pop:
                                idPedido = InserirPedido(cur, conexao, conta)
                            pop = True # Ativação do novo pedido

                        elif escolha == "concluido":
                            AddPedido(cur, conexao, valores, idPedido, conta, janela)



                # --- adiciona um produto a um carrinho --- #

                elif escolha == "add_carrinho":
                    janela.close()
                    janela = janela_adiciona_produto_carrinho()

                    while True:
                        escolha, valores = janela.read()
                        if escolha == sg.WINDOW_CLOSED or escolha == "voltar": 
                            janela.close()
                            janela = janela_produtos()
                            break
                        elif escolha == "concluido":
                            AddCarrinho(cur, conexao, valores, conta, janela)
