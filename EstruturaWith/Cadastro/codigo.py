def vizualizar():
    with open("/home/adriel/Documentos/Python/CadastroUsers/dados.txt", "r") as ler:
        leitura = ler.read()
        print(leitura)
def cadastrar():
    with open("/home/adriel/Documentos/Python/CadastroUsers/dados.txt", "a") as escrever:
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        escrever.write(f"\nNome: {nome} | Idade: {idade}\n")
        print("Usuário cadastrado com sucesso!")
def menu():
    while True:
        print(
    """
=================MENU==================

1 - VIZUALIZAR
2 - CADASTRAR
3 - SAIR

=======================================
    """)
        try:
            opc = int(input("Digite uma das opções: "))
            print("=======================================")
            if(opc == 1):
                vizualizar()
            elif(opc == 2):
                cadastrar()
            elif(opc == 3):
                print("Encerrando...")
                break
            else:
                print("Opção indisponível!")
                menu()
        except:
            print("OPS... Inválido! Tente novamente!")
            menu()
menu()

