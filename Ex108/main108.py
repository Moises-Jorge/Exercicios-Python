from moeda import aumentar, dobro, metade, moeda

preco = float(input('Digite o preco: R$'))
print(f'A metade de {moeda(preco)} eh {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} eh {moeda(dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(aumentar(preco, 10))}')