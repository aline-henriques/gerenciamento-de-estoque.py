import os
import json

#Carregando dados do estoque no arquivo json (estoque.json)
arquivo = os.path.join(os.path.dirname(__file__), 'estoque.json') 

def carregar():

    with open(arquivo, 'r') as f:
        return json.load(f)
   

#Salvando os dados do estoque no arquivo json (estoque.json)
def salvar(estoque):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)
    print("Dados salvos")

#Iniciando o programa

#CRUD:
#Adicionar
def adicionar(nome, quantidade):
    estoque = carregar()
    estoque.append({'nome': nome, 'quantidade': quantidade})
   
    salvar(estoque) 
    

#Atualizar
def atualizar(nome, quantidade=None):
    if nome in estoque:
        if quantidade is not None:
            estoque[nome]['quantidade'] = quantidade
        salvar(estoque)
        print(f"O Produto '{nome}' foi atualizado com sucesso!")
    else:
        print(f"O Produto '{nome}' não foi encontrado no estoque.")

#Rmover
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
        opcao = input("Escolha a opção desejada: ")
        print("\n1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Remover produto")
        print("4. Visualizar estoque")
        print("5. Sair")

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
