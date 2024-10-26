import json

#Carregando os dados do estoque no arquivo json (estoque.json)
def carregar(arquivo='estoque.json'):
    try:
        with open(arquivo, 'r') as f:
            data = json.load(f)
            print("Dados carregados:", data) 
            return data
    except FileNotFoundError:
        print("Arquivo não encontrado.") 
        return {}

#Salvando os dados do estoque no arquivo json (estoque.json)
def salvar(estoque, arquivo='estoque.json'):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)
        print("Dados salvos:", estoque)  # Depuração

estoque = carregar()

#CRUD:
#Adicionar
def adicionar(nome, quantidade):
    if nome in estoque:
        print(f"O produto '{nome}' já existe no estoque.")
    else:
        estoque[nome] = {'quantidade': quantidade}  # Adiciona o produto ao estoque
        salvar(estoque) 
        print(f"Produto '{nome}' adicionado com sucesso.")

#Atualizar
def atualizar(nome, quantidade=None):
    if nome in estoque:
        if quantidade is not None:
            estoque[nome]['quantidade'] = quantidade
        salvar(estoque)
        print(f"O Produto '{nome}' foi atualizado com sucesso!")
    else:
        print(f"O Produto '{nome}' não foi encontrado no estoque.")

#Remover
def remover(nome):
    if nome in estoque:
        del estoque[nome]
        salvar(estoque)
        print(f"O Produto '{nome}' foi removido com sucesso!")
    else:
        print(f"O Produto '{nome}' não foi encontrado no estoque.")

#Visualizar
def visualizar():
    print("\nEstoque Atual:")
    if estoque:
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto} - Quantidade: {detalhes['quantidade']}")
    else:
        print("Estoque vazio.")

#Menu de interação do usuário
def menu():
    while True:
        print("\nEscolha a opção desejada:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Remover produto")
        print("4. Visualizar estoque")
        print("5. Sair")
        
        opcao = input("Digite sua opção: ")

        if opcao == '1':
            nome = input("Insira o nome do produto: ")
            quant = int(input("Quantidade: "))
            adicionar(nome, quant)

        elif opcao == '2':
            nome = input("Insira o nome do produto que deseja atualizar: ")
            quant = input("Nova quantidade de produto no estoque: ")
            atualizar(nome, int(quant) if quant else None)

        elif opcao == '3':
            nome = input("Digite o nome do produto a ser removido: ")
            remover(nome)

        elif opcao == '4':
            visualizar()

        elif opcao == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()