import os

def atualizaProduto(telaPrincipalProduto, main):
    os.system('cls')
    #parametros a ser atualizado no arquivo
    #id = 0, nome = 1, preco = 2, descricao = 3
    print("Atualizacao de produto!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalProduto(main)
    return None
