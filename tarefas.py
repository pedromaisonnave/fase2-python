
# Sistema de registro de ideias de negocio

def adicionar_ideia(ideia):
    with open("ideias.txt", "a") as arquivo:
        arquivo.write(ideia + "\n")

def listar_ideias():
    try:
        with open("ideias.txt", "r") as arquivo:
            ideias = arquivo.readlines()
            if not ideias:
                print("Nenhuma ideia registrada ainda.")
            else:
                for i, ideia in enumerate(ideias, 1):
                    print(f"{i}. {ideia.strip()}")
    except FileNotFoundError:
        print("Nenhuma ideia registrada ainda.")

def apagar_ideia():
    try:
        with open("ideias.txt", "r") as arquivo:
            ideias = arquivo.readlines()
        if not ideias:
            print("Nenhuma ideia para apagar.")
            return
        for i, ideia in enumerate(ideias, 1):
            print(f"{i}. {ideia.strip()}")
        numero = input("Digite o número da ideia que quer apagar: ")
        if not numero.isdigit() or int(numero) < 1 or int(numero) > len(ideias):
            print("Número inválido.")
            return
        ideias.pop(int(numero) - 1)
        with open("ideias.txt", "w") as arquivo:
            arquivo.writelines(ideias)
        print("Ideia apagada.")
    except FileNotFoundError:
        print("Nenhuma ideia registrada ainda.")

def editar_ideia():
    try:
        with open("ideias.txt", "r") as arquivo:
            ideias = arquivo.readlines()
        if not ideias:
            print("Nenhuma ideia para editar.")
            return
        for i, ideia in enumerate(ideias, 1):
            print(f"{i}. {ideia.strip()}")
        numero = input("Digite o número da ideia que quer editar: ")
        if not numero.isdigit() or int(numero) < 1 or int(numero) > len(ideias):
            print("Número inválido.")
            return
        novo_texto = input("Digite o novo texto: ")
        ideias[int(numero) - 1] = novo_texto + "\n"
        with open("ideias.txt", "w") as arquivo:
            arquivo.writelines(ideias)
        print("Ideia atualizada.")
    except FileNotFoundError:
        print("Nenhuma ideia registrada ainda.")

while True:
    print("\nO que você quer fazer?")
    print("1 - Adicionar ideia")
    print("2 - Listar ideias")
    print("3 - Apagar ideia")
    print("4 - Editar ideia")
    print("5 - Sair")

    escolha = input("Digite 1, 2, 3, 4 ou 5: ")

    if escolha == "1":
        ideia = input("Digite sua ideia: ")
        adicionar_ideia(ideia)
        print("Ideia salva!")
    elif escolha == "2":
        listar_ideias()
    elif escolha == "3":
        apagar_ideia()
    elif escolha == "4":
        editar_ideia()
    elif escolha == "5":
        print("Saindo.")
        break
    else:
        print("Opção inválida.")
