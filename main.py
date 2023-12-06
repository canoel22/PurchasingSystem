from getpass import getpass
import PySimpleGUI as sg
import mysql.connector
from Menu.Menu import *
from Menu.TelasMenu import *
import os

import PySimpleGUI as sg


#-------------- se conectando ao mysql --------------------#
conexao = mysql.connector.connect( 
        host="localhost", #endereço de ip do servidor usado
        user="carine", #login
        password="senha123", #senha
        database="compraOnline"
)
cur = conexao.cursor()

#--------------------- menu --------------------------------#
janela = janela_login()
while conexao != False:
    menu(conexao, cur, janela)
    break


#-------------- encerra a conexão ao msql --------------------#
cur.close()
conexao.close()
janela.close()