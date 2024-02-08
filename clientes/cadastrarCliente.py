import os

def cadastrarCliente(telaPrincipalClientes, main):
    os.system('cls')
    #parametros dos clientes: id, nome, cpf, endereco, email
    #parametrosClientes = []
    print("Cadastro de clientes!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalClientes(main)
    return None
