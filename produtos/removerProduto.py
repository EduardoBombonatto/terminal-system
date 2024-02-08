import os

def removerProduto(telaPrincipalProduto, main):
    os.system('cls')
    #produto a ser removido
    #no arquvio vai remover a linha inteira
    print("Remocao de produto!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalProduto(main)
    return None