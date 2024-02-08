import os

def cadastraProduto(telaPrincipalProduto, main):
    os.system('cls')
    #parametros dos produtos: id, nome, preco, descricao (apenas!)
    #parametrosProduto = []
    print("Cadastro de produto!")
    if int(input("digite 0 para voltar a tela de produtos ou digite qualquer outro numero para sair do sistema!: ")) == 0:
        telaPrincipalProduto(main)
    return None