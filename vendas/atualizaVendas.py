import os

def atualizaVenda(telaPrincipalVendas, main):
    os.system('cls')
    #parametros a ser atualizado no arquivo
    #id = 0, nomeCliente = 1, nomeProduto = 2
    print("Atualizacao de venda!")
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
    telaPrincipalVendas(main)