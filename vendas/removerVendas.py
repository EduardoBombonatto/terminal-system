import os

def removerVendas(telaPrincipalVendas, main):
    os.system('cls')
    #escolher venda a ser cancelada
    #no arquivo remover a linha inteira
    print("Remocao de clientes!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalVendas(main)
    return None
