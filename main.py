import os
from produtos.telaPrincipalProduto import telaPrincipalProduto

def main():
    #limpa a tela do terminal
    os.system('cls')
    #menu do sistema
    print("\033[91mBem vindo ao sistema da loja Yorick Coveiro fudido!\033[0m")
    print("\033[93mEscolha uma opção\033[0m")
    print("Numero | Ação")
    print("-------|----------------")
    print("1      | Produtos")
    print("2      | Clientes")
    print("3      | Vendas")
    print("4      | Usuários")
    print("0      | Sair do sistema")
    print()

    numero = int(input("Digite sua escolha: "))
    #forca o usuario a escolher uma das opcoes do menu, caso contrario sera invalido!
    while numero not in (0,1,2,3,4):
        numero = int(input("Numero invalido, escolha um numero acima: "))
    
    if numero == 1:
        #chama a tela de Produtos
        telaPrincipalProduto(main)
    if numero == 2:
        #chama a tela de Clientes
        os.system('cls')
        print("Clientes")
    if numero == 3:
        #chama a tela de Vendas
        os.system('cls')
        print("Vendas")
    if numero == 4:
        #chama a tela de Usuarios
        os.system('cls')
        print("Usuarios")
    if numero == 0:
        #sai do sistema
        os.system('cls')
        print("Saiu do sistema!")
    return None

if __name__ == '__main__':
    main()  