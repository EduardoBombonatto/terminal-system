import os

def atualizarCliente(telaPrincipalClientes, main):
    os.system('cls')
    #parametros a ser atualizado no arquivo
    #id = 0, nome = 1, cpf = 2, endereco = 3, email = 4
    print("Atualizacao de clientes!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalClientes(main)
    return None
