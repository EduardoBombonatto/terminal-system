import os
from produtos.cadastrarProduto import *
from produtos.atualizaProduto import *
from produtos.removerProduto import *

def telaPrincipalProduto(main):
    os.system('cls')
    print("\033[92mMenu de produtos da loja\033[0m")
    print("\033[93mEscolha uma opção\033[0m")
    print("Numero | Ação")
    print("-------|----------------")
    print("1      | Cadastrar produto")
    print("2      | Atualizar produto")
    print("3      | Remover produto")
    print("4      | Voltar a tela inicial")
    print("0      | Sai do sistema")
    print()

    numero = int(input("Digite sua escolha: "))
    #forca o usuario a escolher uma das opcoes do menu, caso contrario sera invalido!
    while numero not in (0,1,2,3,4):
        numero = int(input("Numero invalido, escolha um numero acima: "))

    if numero == 1:
        #chama a tela de cadastrar produtos
        cadastraProduto(telaPrincipalProduto, main)
    elif numero == 2:
        #chama a tela de atualizar produtos
        atualizaProduto(telaPrincipalProduto, main)
    elif numero == 3:
        #chama a tela de remover produtos
        removerProduto(telaPrincipalProduto, main)
    elif numero == 4:
        #chama a tela inicial
        main()
    else:
        #sai do sistema
        print("Saiu do sistema!")
        return None