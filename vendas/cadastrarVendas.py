import os

def cadastraVenda(telaPrincipalVendas, main):
    os.system('cls')
    #parametros dos produtos: id, nomeCliente, nomeProduto
    #parametrosProduto = []
    print("Cadastro de venda!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalVendas(main)
    return None