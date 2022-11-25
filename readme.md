# Código criado com o objetivo de criar um pequeno controle de estoque

## Objetivos:

- Cadastrar dados de um produto novo;
- Defina os atributos padrão dos produtos que serão cadastrados;
- Implementar uma estratégia de pesquisa dos produtos cadastrados;
- Implementar uma estratégia de exibição dos produtos cadastrados;
- Implementar uma estratégia de atualização dos contatos cadastrados;
- Criar mensagens de erro de erro para controlar possíveis entradas inconsistentes;
- Implementar uma estratégia de deleção dos contatos cadastrados; e
- Bônus: Criar uma estratégia para salvar os dados do estoque em um arquivo.

## Como executar:

- Clonar o repositório atual
- Executar o script configuracao.py caso queira que a tabela já tenha alguns dados de exemplo, caso não queira pode pular esse papo
- Executar o script main.py

Ao executar, o programa irá perguntar o que você deseja fazer, as opções disponíveis hoje são:

- Sair do programa
- Atualizar um produto por id
- Cadastrar um produto
- Deletar um produto por id
- Listar todos os produtos
- Pesquisar produtos por nome
- Pesquisar um produto por id

## Como funciona:

O projeto é basicamente um CRUD(Create, read, update,delete) feito em um banco de dados SQLite. Ao executar o script main.py o arquivo estoque.db será criado e nele que será armazenado qualquer dado inserido.

Para quem quiser, antes de executar o script main.py podemos executar o configuracao.py, onde ele também criará o arquivo estoque.db mas com a inserção de alguns dados de exemplo.

Dentro do estoque.db criamos a tabela produto com o seguinte schema

Coluna      | Tipo
------------|---------
id          | Inteiro
produto     | Texto
fabricante  | Texto
preco       | Float
quantidade  | Inteiro

Ao executar o código main.py lemos e escrevemos dados nessa tabela, de acordo com as funcionalidades escolhidas.

O arquivo estoque.py contém as funções que são utilizadas nos outros scripts.

## Pontos a melhorar:

- Se durante a operação, algum campo não passe pela validação a operação é cancelada e a pessoa precisa iniciar de novo. Podemos implementar uma forma de que se o input é inválido a pessoa apenas digite o input novamente.
- O modo de pesquisa por nome só vai funcionar caso o nome do produto bata exatamente com o que está cadastrado, isso poderia ser melhorado.
- Para atualizar um produto, a pessoa deve saber o id do produto. Podiamos inserir um mecanismo de confirmação da operação exibindo o produto do id digitado.
- Poderia ter um modo de exportar os dados para um CSV por exemplo
- Temos um modo de pesquisa de listar todos os produtos, caso tenhamos muitos isso pode ser ruim para ler/navegar
- Ao atualizar um produto, caso a pessoa insera um id que não exista isso não gerará erro mas também não salvará a modificação. Poderia criar uma verificação que só pode inserir id's existentes.

