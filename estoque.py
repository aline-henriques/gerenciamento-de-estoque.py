import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'estoque.json')

if not os.path.exists(arquivo):    
    with open(arquivo, 'w') as f:
        json.dump({}, f)  

def carregar():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar(estoque):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)
    print("Dados salvos")
    

#CRUD
#Adicionar
def adicionar(nome, quantidade):
    estoque = carregar()
    if nome in estoque:
        print(f"O produto '{nome}' já existe no estoque.")
    else:
        estoque[nome] = {'quantidade': quantidade}
        salvar(estoque)
        print(f"O produto '{nome}' foi adicionado com sucesso.")

#Atualizar
def atualizar(nome, quantidade):
    estoque = carregar()
    if nome in estoque:
        estoque[nome]['quantidade'] = quantidade
        salvar(estoque)
        print(f"O produto '{nome}' foi atualizado com sucesso!")
    else:
        print(f"O produto '{nome}' não foi encontrado no estoque.")

#Remover
def remover(nome):
    estoque = carregar()
    if nome in estoque:
        del estoque[nome]
        salvar(estoque)
        print(f"O produto '{nome}' foi removido com sucesso!")
    else:
        print(f"O produto '{nome}' não foi encontrado no estoque.")

#Visualizar
def visualizar():
    estoque = carregar()
    print("\nEstoque Atual:")
    if estoque:
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto} - Quantidade: {detalhes['quantidade']}")
    else:
        print("Estoque vazio.")



#Menu
def menu():
    while True:
        print("\nEscolha a opção desejada:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Remover produto")
        print("4. Visualizar estoque")
        print("5. Sair")
        
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Insira o nome do produto que deseja adicionar: ")
            quant = int(input("Quantidade: "))
            adicionar(nome, quant)

        elif opcao == '2':
            nome = input("Insira o nome do produto que deseja atualizar: ")
            quant = int(input("Nova quantidade de produto no estoque: "))
            atualizar(nome, quant)

        elif opcao == '3':
            nome = input("Digite o nome do produto a ser removido: ")
            remover(nome)

        elif opcao == '4':
            visualizar()

        elif opcao == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()
