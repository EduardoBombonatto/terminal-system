import os

def atualizaProduto(telaPrincipalProduto, main):
    os.system('cls')
    #parametros a ser atualizado no arquivo
    #id = 0, nome = 1, preco = 2, descricao = 3
    print("Atualizacao de produto!")
    while True:
        entrada = input("Digite 0 para voltar a pagina de clientes: ")
        #verifica se o usuario nao apertou enter sem querer, ou nao tem entrada
        if entrada == "":
            continue
        try:
            #verifica se a entrada foi um numero
            numero = int(entrada)
            #se for um numero tem que estar entre as opcoes
            if numero != 0:
                print("Opção inválida.")
                continue
            break  # Sai do loop se o número estiver correto
        except ValueError:
            print("Opção inválida.")
    telaPrincipalProduto(main)
