try:

    nomeProduto = input("Insira o nome do produto: ")
    precoProduto = float(input("Insira o preço do produto: "))

    if precoProduto < 50.00:
        print("Produto Preço Baixo")
    elif 50.00 <= precoProduto <= 100.00:
        print("Produto Preço Médio")
    else:
        print("Produto Preço Alto")

except(ValueError, TypeError):
    print('[ERRO] Caractere inválido! Tente novamente.')
   
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados!')