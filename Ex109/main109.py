from moeda import aumentar, diminuir, dobro, metade, moeda_format

preco = float(input('Digite o preco: R$'))
print(f'A metade de {moeda_format(preco)} eh {metade(preco, True)}')
print(f'O dobro de {moeda_format(preco)} eh {dobro(preco, True)}')
print(f'Aumentando 10%, temos {aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(preco, 13, True)}')