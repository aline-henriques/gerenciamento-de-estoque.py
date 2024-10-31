## Introdução
O objetivo do nosso projeto é desenvolver a prototipação de um aplicativo de gestão de estoque, permitindo que empresas monitorem produtos, rastreiem quantidades e otimizem suas operações de maneira prática e eficiente. Utilizamos Python para implementar o sistema e o formato JSON para armazenamento dos dados, aplicando um sistema CRUD (Create, Read, Update, Delete) para gerenciar o estoque de forma organizada e acessível.

## Desenvolvimento

### Carregando e Salvando Dados

Para gerenciar o estoque, começamos importando os módulos “os” e `json`. O módulo `os` permite a manipulação de arquivos e caminhos do sistema, enquanto o `json` é usado para ler e escrever dados em formato JSON. Definimos o caminho do arquivo JSON e verificamos se ele já existe. Caso contrário, o sistema cria um novo arquivo com um dicionário vazio, iniciando o estoque de forma organizada.

A função `carregar` abre o arquivo JSON no modo de leitura, carregando o conteúdo como um dicionário, que representa o estoque atual. A função `salvar` abre o arquivo JSON no modo de escrita, gravando o dicionário `estoque` com uma formatação indentada, o que facilita a leitura e manutenção dos dados. Essa função também exibe uma mensagem para confirmar o salvamento dos dados.

## Desenvolvimento 2

- CRUD - Operações de Gestão de Estoque

### Adicionar Produto:
A função `adicionar` permite que o usuário insira um novo produto no estoque. Primeiramente, ela verifica se o produto já existe, evitando duplicações. Se for um novo item, ele é adicionado ao dicionário `estoque` com a quantidade especificada, e os dados são salvos no arquivo JSON.

### Atualizar Produto
A função `atualizar` permite ao usuário modificar a quantidade de um produto existente. Se o produto não estiver no estoque, o programa exibe uma mensagem informando o usuário, tornando o processo claro e eficiente.

### Remover Produto:
A função `remover` exclui um produto do estoque. Se o item não for encontrado, uma mensagem é exibida para alertar o usuário.

### Visualizar Estoque: 
A função `visualizar` exibe todos os produtos no estoque junto com suas quantidades. Caso o estoque esteja vazio, o programa informa ao usuário que não há produtos registrados.

### Menu Interativo
Implementamos um menu interativo que permite ao usuário navegar facilmente entre as opções de gerenciamento do estoque:

1. Adicionar produto
2. Atualizar produto
3. Remover produto
4. Visualizar estoque
5. Sair

Para garantir a usabilidade, incluímos uma condição que exibe uma mensagem caso a opção digitada pelo usuário seja inválida, facilitando a navegação.

## Conclusão
Desenvolvemos um aplicativo de gestão de estoque em Python que utiliza JSON para armazenar dados. Este sistema oferece uma interface intuitiva e eficiente para gerenciar produtos e monitorar o estoque, oferecendo às empresas uma solução simples e prática para otimizar o controle de seus produtos.

