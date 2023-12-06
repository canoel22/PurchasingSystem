
def RegistroClienteWeb(cur, conexao, registro): # FUNCIONANDO BEM
    
    #------Verificar se cpf já existe------
    cur.execute("select idCliente from Usuario where idCliente = %s", (registro["cpf"],))
    exists = cur.fetchone()
    if exists: #Se a tupla existir, então um usuario com este id já existe
        return 0
    
    #------Verificar se login já existe------
    cur.execute("select login from ClienteWeb where login = %s", (registro["login"],))
    exists = cur.fetchone()
    if not exists is None: #Se a tupla existir, então um cliente com este login já existe
        return 0

    #------Inserir na tabela Conta------
    cur.execute("insert into Conta (idConta) values (null)")
    idConta = cur.lastrowid
    conexao.commit()

    #------Inserir na tabela Usuario------
    sql = "insert into Usuario (idCliente, nome, bairro, cidade, estado, idConta) values (%s,%s,%s,%s,%s,%s);"
    cur.execute(sql, (registro["cpf"], registro["nome"], registro["bairro"], registro["cidade"],registro["estado"], idConta))
    registrado = cur.fetchall
    conexao.commit()

    #------Inserir na tabela ClienteWeb------
    sql = "insert into ClienteWeb (login, senha, statusCliente, idCliente) values (%s,%s,%s,%s);"
    cur.execute(sql, (registro["login"], registro["senha"], "Novo", registro["cpf"]))
    conexao.commit()

    return 1


def LoginClienteWeb(cur, conexao, log):
    
    sql = "select idConta from Usuario where idCliente = (select idCliente from ClienteWeb where login = %s and senha = %s);"
    cur.execute(sql, (log["login"], log["senha"]))
    logado = cur.fetchone()

    return logado

def RegistroAtendido(cur, conexao, registro): # FUNCIONANDO BEM
    
    #------Verificar se cpf já existe------
    cur.execute("select idCliente from Usuario where idCliente = %s", (registro["cpf"],))
    exists = cur.fetchone()
    if exists: #Se a tupla existir, então um usuario com este id já existe
        return 0
    
    #------Verificar se telefone já existe------
    cur.execute("select telefone from Atendido where telefone = %s", (registro["telefone"],))
    exists = cur.fetchone()
    if not exists is None: #Se a tupla existir, então um cliente com este telefone já existe
        return 0

    #------Inserir na tabela Conta------
    cur.execute("insert into Conta (idConta) values (null)")
    idConta = cur.lastrowid
    conexao.commit()

    #------Inserir na tabela Usuario------
    sql = "insert into Usuario (idCliente, nome, bairro, cidade, estado, idConta) values (%s,%s,%s,%s,%s,%s);"
    cur.execute(sql, (registro["cpf"], registro["nome"], registro["bairro"], registro["cidade"],registro["estado"], idConta))
    registrado = cur.fetchall
    conexao.commit()

    #------Inserir na tabela Atendido------
    sql = "insert into Atendido (telefone, idCliente) values (%s,%s);"
    cur.execute(sql, (registro["telefone"], registro["cpf"]))
    conexao.commit()

    return 1
