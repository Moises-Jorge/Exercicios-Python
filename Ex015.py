# Programa que recebe a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais o mesmo foi alugado; calcula o preco a pagar, sabendo que o carro custa 60kz por dia e 0,15kz por km percorrido

kmPercorrido = float(input("Quantos km o carro percorreu?: "))
dias = int(input("Por quantos dias?: "))

preco_a_pagar = (kmPercorrido * 0.15) + (dias * 60)

print("Preco a pagar: {}kz\n".format(preco_a_pagar))