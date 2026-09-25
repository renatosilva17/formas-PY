itens = ["cafe", "chá", "açucar", "todinho"]

def lista():
    print("ITENS DA LOJA")
    if not itens:
        print("a lista está vazia")
    else:
        for indice, item in enumerate(itens, start=1):
            print(f"{indice} - {item}")


while True:
    print("Bem vindo a loja")
    print("1 - mostrar lista")
    print("2 - cadastrar item")
    print("3 - excluir item")
    print("4 - modificar item da lista")
    print("0 - sair")

    opcao = input("digite um numero")


    if opcao == "1":
        lista()
     
    elif opcao == "2":
        novo_item = input("digite o nome  do novo item: ")
        itens.append(f"Item '{novo_item}' cadastro com sucesso!")
     
    elif opcao == "3":
        lista()
        if itens:
            pos = int(input("digite um numero que deseja excluir: "))
            if 1 <= pos <= len(itens):
                removido = itens.pop(pos - 1)
                print(f"Item '{removido}' excluido com sucesso!")
            else:
                print("numero invalido!")
   
    elif opcao == "4":
        lista()
        if itens:
            pos = int(input("Digite o numero do itemque deseja modificar: "))
            if 1 <= pos <= len(itens):
                novo_nome = input("digite o novo nome do item: ")
                antigo = iten[pos - 1]
                itens[pos - 1] = novo_nome
                print (f"Item '{antigo}' modificado para '{novo_nome}'!")
            else:
                print("numero invalido!")

    elif opcao == "0":
        print("saindo do programa. fllw ae")
        break
    else:
        print("opcao invalida! escolha um numero de 0 a 4.")