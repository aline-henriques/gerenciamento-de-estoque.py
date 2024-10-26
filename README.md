# Introdução
O objetivo do nosso projeto é desenvolver um aplicativo de gestão de estoque que permita às empresas monitorar produtos, rastrear vendas e otimizar operações de forma prática e eficiente. Utilizamos Python para desenvolver o sistema e JSON para o armazenamento dos dados, aplicando um sistema CRUD (Create, Read, Update, Delete) para facilitar o gerenciamento do estoque.

# Desenvolvimento
Carregando e Salvando Dados
A função carregar é responsável por abrir o arquivo JSON no modo de leitura, carregando os dados do estoque.

	•	Utilizamos o bloco try...except para capturar o erro caso o arquivo não seja encontrado, retornando uma mensagem informativa ao usuário.
	•	A função json.load é usada para carregar os dados, que são armazenados em um dicionário.
	•	Um comando print é incluído para exibir os dados carregados, permitindo uma visualização rápida para depuração e acompanhamento.

A função salvar grava as alterações feitas no estoque no arquivo JSON, salvando o dicionário estoque com indentação para facilitar a leitura.

## Iniciando o Estoque
Ao iniciar o programa, ele tenta carregar os dados do arquivo JSON. Caso o arquivo não exista, o estoque será inicializado como um dicionário vazio, pronto para receber novos produtos.

## CRUD
### Operações de Gestão de Estoque
## Adicionar Produto
A função adicionar permite que o usuário adicione um novo produto ao estoque.

	•	Se o produto já existir, uma mensagem informa o usuário, evitando duplicações.
	•	Caso seja um novo produto, ele é adicionado ao dicionário estoque com a quantidade especificada e salvo no arquivo JSON.

## Atualizar Produto
A função atualizar permite que o usuário modifique a quantidade de um produto existente.

	•	Caso o produto não esteja no estoque, uma mensagem informa o usuário, garantindo clareza no processo.

## Remover Produto
A função remover permite ao usuário excluir um produto do estoque.

	•	Se o produto não estiver no estoque, o programa exibe uma mensagem avisando que o item não foi encontrado.

## Visualizar Estoque
A função visualizar exibe todos os produtos do estoque com suas respectivas quantidades.

	•	Se o estoque estiver vazio, uma mensagem avisa que não há produtos registrados.

## Menu Interativo

O menu interativo permite ao usuário navegar pelas opções e realizar ações no estoque de forma intuitiva:

	1.	Adicionar produto
	2.	Atualizar produto
	3.	Remover produto
	4.	Visualizar estoque
	5.	Sair

Foi implementada uma condição que informa ao usuário se a opção digitada é inválida, caso ele escolha um número fora do menu.

# Conclusão
Em resumo, desenvolvemos um aplicativo de gestão de estoque em Python que utiliza JSON para o armazenamento dos dados. Esse sistema permite monitorar produtos, rastrear quantidades e facilitar o controle de estoque, oferecendo uma interface prática e interativa. Nosso projeto é uma solução simples e eficiente para empresas que buscam otimizar o gerenciamento de seus produtos.

