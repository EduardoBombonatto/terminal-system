import os

def removerCliente(telaPrincipalClientes, main):
    os.system('cls')
    #escolher cliente a ser removido
    #no arquivo remover a linha inteira
    print("Remocao de clientes!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalClientes(main)
    return None
