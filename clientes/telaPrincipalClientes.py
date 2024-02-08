import os
from clientes.cadastrarCliente import *
from clientes.atualizarCliente import *
from clientes.removerClientes import *

def telaPrincipalClientes(main):
    os.system('cls')
    print("\033[94mMenu de clientes da loja\033[0m")
    print("\033[93mEscolha uma opção\033[0m")
    print("Numero | Ação")
    print("-------|----------------")
    print("1      | Cadastrar clientes")
    print("2      | Atualizar clientes")
    print("3      | Remover clientes")
    print("4      | Voltar a tela inicial")
    print("0      | Sai do sistema")
    print()

    #forca o usuario a escolher uma das opcoes do menu, caso contrario sera invalido!
    while True:
        entrada = input("Digite um número inteiro: ")
        #verifica se o usuario nao apertou enter sem querer, ou nao tem entrada
        if entrada == "":
            continue
        try:
            #verifica se a entrada foi um numero
            numero = int(entrada)
            #se for um numero tem que estar entre as opcoes
            if numero not in (0, 1, 2, 3, 4):
                print("Opção inválida.")
                continue
            break  # Sai do loop se o número estiver correto
        except ValueError:
            print("Opção inválida.")

    if numero == 1:
        #chama a tela de cadastrar cliente
        cadastrarCliente(telaPrincipalClientes, main)
    elif numero == 2:
        #chama a tela de atualizar cliente
        atualizarCliente(telaPrincipalClientes, main)
    elif numero == 3:
        #chama a tela de remover cliente
        removerCliente(telaPrincipalClientes, main)
    elif numero == 4:
        #chama a tela inicial
        main()
    else:
        #sai do sistema
        print("Saiu do sistema!")
        return None