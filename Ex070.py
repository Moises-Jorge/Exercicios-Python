'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    1. Qual é o total gasto na compra.
    2. Quantos produtos custam de 1000.
    3. Qual é o nome do produto mais barato'''
print('-' * 30)
print('     LOJA SUPER BARATAO')
print('-' * 30)
qtd_produtos = preco_total = produtos_caros = preco_produto_barato = 0
while True:
    # Leitura dos Valores
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    # Calculos
    qtd_produtos += 1
    preco_total += preco
    if preco > 1000:
        produtos_caros += 1
    if qtd_produtos == 1:
        preco_produto_barato = preco
        nome_produto_barato = nome_produto
    elif preco < preco_produto_barato:
        preco_produto_barato = preco
        nome_produto_barato = nome_produto
    # Verificacao se o usuario deseja continuar
    cond_saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    while cond_saida not in 'SN': # Nao para de tentar ler enquanto o usuario nao digita a opcao correta
        cond_saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if cond_saida == 'N':
        break
print('\n---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${preco_total}\nTemos {produtos_caros} produtos custando mais de R$1000\nO produto mais barato foi {nome_produto_barato} que custa R${preco_produto_barato}')