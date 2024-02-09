import os

def cadastraProduto(telaPrincipalProduto, main):
    os.system('cls')
    #parametros dos produtos: id, nome, preco, descricao
    parametrosProduto = []
    print("CADASTRO DE PRODUTO")
    #escrever todos os parametros do produto para ir no banco de dados!
    parametrosProduto.append(obterID('bdProdutos.txt'))
    parametrosProduto.append(str(input("digite o nome do produto: ")))
    parametrosProduto.append(round(float(input("digite o preco do produto: ")),2))
    parametrosProduto.append(str(input("digite a descricao do produto: ")))

    #insere os parametros no Banco de Dados
    for parametro in parametrosProduto:
        inserirParametro('bdProdutos.txt',parametro)
    #pula a linha do cursor!
    with open('bdProdutos.txt', 'a') as arquivo:
        arquivo.write('\n')
        arquivo.seek(0)

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
    
def obterID(bdProdutos):
    try:
        with open(bdProdutos, 'r') as arquivo:
            ids = [int(linha.strip().split(',')[0]) for linha in arquivo.readlines()]
            if ids:
                return max(ids) + 1
            else:
                return 1
    except FileNotFoundError:
        return 1

def inserirParametro(nome_arquivo, registro):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(str(registro) + ',')