from moeda import aumentar, dobro, metade

preco = float(input('Digite o preco: R$'))
print(f'A metade de R${preco} eh R${metade(preco)}')
print(f'O dobro de R${preco} eh R${dobro(preco)}')
print(f'Aumentando 10%, temos R${aumentar(preco, 10)}')