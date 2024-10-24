Apresentação

Introdução

O propósito do nosso projeto é desenvolver um aplicativo de gestão de estoque que permita às empresas monitorar produtos, rastrear vendas e otimizar operações. O código foi desenvolvido em Python e utiliza JSON para o armazenamento de dados, implementando um sistema CRUD (Create, Read, Update, Delete).

Desenvolvimento

Carregando e Salvando

A função carregar é responsável por abrir o arquivo JSON no modo leitura. 
Utilizamos o bloco “try...except” para a possibilidade de o arquivo não ser encontrado, imprimindo uma mensagem de erro quando isso acontece. 
A função json.load é utilizada para carregar e armazenar os dados lidos no arquivo.
O comando print permite visualizar rapidamente os dados carregados, facilitando a depuração e execução do desenvolvedor.

Iniciando

Ao ser chamado, o programa inicia o estoque com os dados salvos do arquivo JSON. Se o arquivo não existir, o estoque será iniciado como um dicionário vazio.

Desenvolvimento 2

	•	CRUD

Adicionar

A função adicionar foi elaborada para que o usuário possa adicionar um novo produto ao seu estoque. Se o produto inserido já estiver presente, uma condição é aplicada para informar que o produto já existe.

Atualizar

A função atualizar permite que o usuário atualize a quantidade de um produto que já está em seu estoque. Caso o usuário insira o nome de um produto que não se encontra no estoque, uma mensagem será exibida informando que o produto não foi encontrado.

Remover

A função remover foi desenvolvida para permitir que o usuário remova um produto presente em seu estoque. Se o usuário tentar remover um produto que não se encontra no estoque, o programa informará que o produto não foi encontrado.

Visualizar

A função visualizar permite ao usuário visualizar o estoque atual, exibindo o nome e a quantidade de cada produto registrado. Caso não haja produtos registrados, será exibida uma mensagem informando que o estoque está vazio.

	•	Menu Interativo

O menu interativo foi criado para que o usuário possa escolher e realizar diversas ações em seu estoque, incluindo adicionar, atualizar, remover e visualizar produtos. O menu apresenta as seguintes opções:

	1	Adicionar produto
	2	Atualizar produto
	3	Remover produto
	4	Visualizar estoque
	5	Sair

Foi implementada uma condição para que, caso o usuário digite um número inexistente, uma mensagem de erro informe que a opção é inválida.

Conclusão

Em resumo, desenvolvemos um aplicativo de gestão de estoque que facilita o monitoramento de produtos, o rastreio de vendas e a otimização das operações. Utilizando Python e JSON, implementamos um sistema eficiente e fácil de usar, com um menu interativo que permite aos usuários gerenciar seu estoque de forma prática.

https://genstock.my.canva.site/