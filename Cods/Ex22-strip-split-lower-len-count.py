import time 
try:
    nome = str(input("Digite seu nome completo: "))
    aux = nome.split() # Divide a string numa lista com cada elemento separado por seu espaço;
    auxi = aux[0]
except:
    print("Ops..")
else:
    print("Analisando seu nome...")
    time.sleep(2)
    print("-"*35)
    print("Seu nome em Maiúscula é {}".format(nome.upper()))
    print("Seu nome em minúscula é {}".format(nome.lower()))
    print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
    print("Seu primeiro nome é {} e ele tem {} letras".format(auxi, len(auxi)))
# len = tamanho da string com os espaços;
# count = quantas vezes aparece tal letra ou espaço;
