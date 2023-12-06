import PySimpleGUI as sg
from Menu.TelasMenu import *
from Consultas.TelaConsulta import *
from Consultas.FuncoesConsulta import *
from Gerente.TelasGerente import *
import threading


#-------------- menu --------------------#

def consultas(conexao, cur, janela):
    while True: 
        escolha, valores = janela.read()
        
        #-------------- se o usuário quiser sair --------------------#
        if escolha == sg.WINDOW_CLOSED or escolha == "sair":
            janela.close()
            janela = janela_gerente
            break

        #--------- Todos os pedidos associados a uma conta" -----------#

        elif escolha == "PedidosAssociados":
            janela.close()
            janela = janela_consulta1()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break  
                elif escolha == 'buscado':
                    id_conta = valores['idConta']
                    PedidosAssociados(conexao, cur, id_conta)


        #--------- Todos os produtos contidos em um carrinho" -----------#

        elif escolha == "ProdutosNoCarrinho":
            janela.close()
            janela = janela_consulta2()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break  
                elif escolha == 'buscado':
                    id_carrinho = valores['idCarrinho']
                    ProdutosNoCarrinho(conexao, cur, id_carrinho) 



        #--------- Dados (e qtd) dos usuários cadastrados no sistema -----------#

        elif escolha == "DadosUsuarios":
            janela.close()
            dados_formatados = DadosUsuarios(conexao, cur)
            qtd_formatadas = QtdUsuarios(conexao, cur)
            janela = janela_consulta3(dados_formatados, qtd_formatadas)

            while True:
                event, valores = janela.read()

                if event == sg.WIN_CLOSED or event == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break
                                        

        #--------- Forma de pagamento mais utilizada -----------#

        elif escolha == "PgtoMaisUsado":
            janela.close()
            dados_formatados = PgtoMaisUsado(conexao, cur)
            janela = janela_consulta4(dados_formatados)

            while True:
                event, valores = janela.read()

                if event == sg.WIN_CLOSED or event == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break
                    
        #--------- Filtro de usuário por bairro, cidade e estado -----------#

        elif escolha == "FiltroEndereco":
            janela.close()
            janela = janela_consulta5()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break  
                elif escolha == 'buscado':
                    bairro = valores['bairro']
                    cidade = valores['cidade']
                    estado = valores['estado']
                    FiltroEndereco(conexao, cur, bairro, cidade, estado) 


        #--------- Média anual de vendas -----------#

        elif escolha == "MediaAnualDeVenda":
            janela.close()
            janela = janela_consulta6()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break  
                elif escolha == 'buscado':
                    ano = valores['ano']
                    MediaAnualDeVenda(conexao, cur, ano) 
      
            
        #--------- Mês e ano com maior número de vendas -----------#

        elif escolha == "MaiorVendas":
            janela.close()
            dados_formatados = MaiorVendas(conexao, cur)
            janela = janela_consulta7(dados_formatados)

            while True:
                event, valores = janela.read()

                if event == sg.WIN_CLOSED or event == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break
                          
        #--------- Usuários que realizaram compras em todos os meses de um determinado ano -----------#

        elif escolha == "TodosMeses":
            janela.close()
            janela = janela_consulta8()

            while True:
                escolha, valores = janela.read()

                if escolha == sg.WIN_CLOSED or escolha == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break  
                elif escolha == 'buscado':
                    ano = valores['ano']
                    TodosMeses(conexao, cur, ano)       


        #--------- Quantidade de usuários por status -----------#

        elif escolha == "UsuariosPorStatus":
            janela.close()
            dados_formatados = UsuariosPorStatus(conexao, cur)
            janela = janela_consulta9(dados_formatados)

            while True:
                event, valores = janela.read()

                if event == sg.WIN_CLOSED or event == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break
                               


        #--------- Produto mais vendido-----------#

        elif escolha == "MaisVendido":
            janela.close()
            dados_formatados = MaisVendido(conexao, cur)
            janela = janela_consulta10(dados_formatados)

            while True:
                event, valores = janela.read()

                if event == sg.WIN_CLOSED or event == 'voltar':
                    janela.close()
                    janela = janela_consultas()
                    break
                          