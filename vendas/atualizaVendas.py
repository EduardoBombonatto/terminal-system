import os

def atualizaVenda(telaPrincipalVendas, main):
    os.system('cls')
    #parametros a ser atualizado no arquivo
    #id = 0, nomeCliente = 1, nomeProduto = 2
    print("Atualizacao de venda!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalVendas(main)
    return None