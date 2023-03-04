# Programa que leh o preco de um produto e mostra seu novo preco com 5% de desconto
preco = float(input("Informe o preco do produto: "))

novoPreco = preco - (preco * (5/100))

print("O produto agora custa {}kz\n".format(novoPreco))