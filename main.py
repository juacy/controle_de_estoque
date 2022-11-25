import estoque
from estoque import to_float, to_int

estoque.criar_tabela_produto()

print('Bem-vindo(a) ao programa de controle de estoque')

opcao = -1

while opcao!=0:
    print('O que você deseja fazer?')
    for key, value in estoque.funcionalidades.items():
        print(f'{key: <10}{value}')

    try:
        opcao = int(input('Digite o número da sua opção: '))

        if opcao not in estoque.funcionalidades.keys():
            int('a')
    except ValueError:
        print('Digite um número inteiro válido')
        continue


    if opcao==0:
        print('Até a próxima')

    elif opcao==1:
        id_produto = to_int(input('Digite o id do produto que você deseja atualizar: '))
        if id_produto==-1:
            continue
        nome_produto = input('Digite o nome do produto atualizado: ')
        fabricante_produto = input('Digite o fabricante atualizado: ')
        preco_produto = to_float(input('Digite o preço do produto atualizado: ').replace(',','.'))
        if preco_produto==-1:
            continue
        quantidade_produto = to_int(input('Digite a quantidade do produto atualizada: '))
        if quantidade_produto==-1:
            continue
        estoque.atualiza_produto(id_produto=id_produto, produto=nome_produto, fabricante=fabricante_produto, preco=preco_produto, quantidade=quantidade_produto)
        print(f'O produto {id_produto} foi atualizado, caso o id exista.')

    elif opcao==2:
        nome_produto = input('Digite o nome do produto: ')
        fabricante_produto = input('Digite o fabricante: ')
        preco_produto = to_float(input('Digite o preço: '))
        if preco_produto==-1:
            continue        
        quantidade_produto = to_int(input('Digite a quantidade: '))
        if quantidade_produto==-1:
            continue
        estoque.cadastra_produto(produto=nome_produto, fabricante=fabricante_produto, preco=preco_produto, quantidade=quantidade_produto)
        print(f'O produto foi cadastrado.')

    elif opcao==3:
        id_produto = to_int(input('Digite o id do produto que você deseja DELETAR: '))
        if id_produto==-1:
            continue
        confirmacao = input(f'Tem certeza que deseja deletar o produto {id_produto}?(Sim para continuar)')
        if confirmacao.strip().lower()=='sim':
            estoque.deleta_produto(id_produto)
            print('O produto foi deletado')
        else:
            print('A operação foi cancelada')

    elif opcao==4:
        resultado = estoque.pesquisa_tudo().fetchall()
        if resultado:
            print('{: <30}{: <30}{: <30}{: <30}{}'.format('ID','Produto', 'Fabricante', 'Preço Unitário', 'Quantidade'))
            for linha in resultado:
                print(f'{linha[0]: <30}{linha[1]: <30}{linha[2]: <30}{linha[3]: <30}{linha[4]: <30}')        
        else:
            print('Não temos produtos cadastrados ainda')

    elif opcao==5:
        nome_produto = input('Digite o nome do produto que você deseja pesquisar: ')
        resultado = estoque.pesquisa_produto(nome_produto).fetchall()
        if resultado:
            print('{: <30}{: <30}{: <30}{: <30}{: <30}'.format('ID','Produto', 'Fabricante', 'Preço Unitário', 'Quantidade'))
            for linha in resultado:
                print(f'{linha[0]: <30}{linha[1]: <30}{linha[2]: <30}{linha[3]: <30}{linha[4]: <30}')
        else:
            print('Não temos produto com esse nome cadastrado') 

    elif opcao==6:        
        id_produto = to_int(input('Digite o id do produto que você deseja pesquisar: '))
        if id_produto==-1:
            continue        
        resultado = estoque.pesquisa_produto_id(id_produto).fetchall()
        if resultado:
            print('{: <30}{: <30}{: <30}{: <30}{: <30}'.format('ID','Produto', 'Fabricante', 'Preço Unitário', 'Quantidade'))
            for linha in resultado:
                print(f'{linha[0]: <30}{linha[1]: <30}{linha[2]: <30}{linha[3]: <30}{linha[4]: <30}')
        else:
            print('Não temos produto com esse id cadastrado')

    print('{:-<150}'.format(''))  


