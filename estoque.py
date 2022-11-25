"""
Cadastrar dados de um produto novo;
Defina os atributos padrão dos produtos que serão cadastrados;
Implementar uma estratégia de pesquisa dos produtos cadastrados;
Implementar uma estratégia de exibição dos produtos cadastrados;
Implementar uma estratégia de atualização dos contatos cadastrados;
Criar mensagens de erro de erro para controlar possíveis entradas inconsistentes;
Implementar uma estratégia de deleção dos contatos cadastrados; e
Bônus: Criar uma estratégia para salvar os dados do estoque em um arquivo.
"""

import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

funcionalidades = {
    0:'Sair do programa',
    1:'Atualizar um produto por id',
    2:'Cadastrar um produto',
    3:'Deletar um produto por id',
    4:'Listar todos os produtos',
    5:'Pesquisar produtos por nome',
    6: 'Pesquisar um produto por id'
}

def criar_tabela_produto():
    """ cria a tabela 'produto' caso ela não exista """
    cursor.execute("""
    create table if not exists produto (
        id integer primary key autoincrement,
        produto text,
        fabricante text,
        preco_unitario float,
        quantidade integer
    )
    """)

def cadastra_produto(produto, fabricante, preco, quantidade):
    """ adiciona um novo produto"""
    cursor.execute("insert into produto (produto, fabricante, preco_unitario, quantidade) values (?, ?, ?, ?)", (produto, fabricante, preco, quantidade))
    conexao.commit()

def atualiza_produto(id_produto, produto, fabricante, preco, quantidade):
    """ atualiza um produto pelo id """
    cursor.execute("update produto set produto = ?, fabricante = ?, preco_unitario = ?, quantidade = ? where id = ?", (produto, fabricante, preco, quantidade, id_produto))
    conexao.commit()

def pesquisa_produto(produto):
    """ marca a tarefa como concluida """
    return cursor.execute("select * from produto where produto like ?", (produto, ))

def pesquisa_produto_id(id):
    """ marca a tarefa como concluida """
    return cursor.execute("select * from produto where id = ?", (id, ))

def pesquisa_tudo():
    """ Pesquisa todos os produtos da base """
    return cursor.execute("select * from produto")

def deleta_produto(id): # retorna um cursor
    """ retorna a lista de tarefas cadastras """
    cursor.execute("delete from produto where id = ?", (id,))
    conexao.commit()

def to_float(entrada:str):
    try:
        entrada = float(entrada.replace(',','.').strip())
        if entrada<0:
            print('Digite um número float não negativo')
        return entrada
    except ValueError:
        print('O valor digitado não é valido, digite um float')
        print('A operação foi cancelada')
        return -1

def to_int(entrada:str):
    try:
        entrada = int(entrada)
        if entrada<0:
            print('Digite um número inteiro não negativo')
            return -1
        return entrada
    except ValueError:
        print('O valor digitado não é valido, digite um inteiro')
        print('A operação foi cancelada')
        return -1
