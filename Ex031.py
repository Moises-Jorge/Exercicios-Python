# programa que pergunta a distância de uma viagem em km. Calcule o preço da passagem, cobrando 50kz por km para viagens de até 200km e 45kz para viagens mais longas.

distancia = float(input('Informe a distância da viagem por favor: '))

if(distancia <= 200):
    preco = distancia * 50
else:
    preco = distancia * 45

print('Vc tera que pagar {}kz pela viagem!'.format(preco))