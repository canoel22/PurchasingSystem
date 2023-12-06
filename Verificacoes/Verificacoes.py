   
#--------------------- verifica se um usuário está cadastrado --------------------------------#

def VerificaUsuario(cur, nomeUsuario, senhaUsuario):
    cur.execute(f"SELECT login,senha FROM ClienteWeb WHERE login = '{nomeUsuario}' AND senha= '{senhaUsuario}'") 
    usuarios_cadastrados = cur.fetchall() 
    if len(usuarios_cadastrados) == 1:
        return 0
    else:
        return 1 #Retorna 1 se não estiver
    

#--------------------- verifica se um usuário está cadastrado --------------------------------#

def VerificaAtendente(cur, telefoneUsuario):

    sql='''SELECT idCliente FROM Atendido WHERE telefone = %s'''

    cur.execute(sql, (telefoneUsuario,)) 
    usuarios_cadastrados = cur.fetchone()
    if usuarios_cadastrados is None:
        return None #Retorna None se não estiver
    else:
        sql = "select idConta from Usuario where idCliente = %s"
        cur.execute(sql, (usuarios_cadastrados[0],))
        logado = cur.fetchone()

        return logado