def exibir_menu():
    print("\n--- Inventário de Produtos ---")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos")
    print("4. Sair")

def adicionar_produto(inventario):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(inventario):
    nome = input("Digite o nome do produto a ser removido: ")
    
    if nome in inventario:
        del inventario[nome]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no inventário.")

def listar_produtos(inventario):
    if inventario:
        print("\n--- Produtos no Inventário ---")
        for nome, info in inventario.items():
            print(f"Produto: {nome}, Preço: R$ {info['preco']}, Quantidade: {info['quantidade']}")
    else:
        print("O inventário está vazio.")

def main():
    inventario = {}
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto(inventario)
        elif opcao == '2':
            remover_produto(inventario)
        elif opcao == '3':
            listar_produtos(inventario)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
