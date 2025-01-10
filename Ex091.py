'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
jogadores = dict()
# Ciclo do Sorteio (alimentando o dicionario)
for c in range(4):
    jogadores[f'jogador{c+1}'] = randint(1,6)
print('Valores sorteados:')
# Ciclo de apresentacao dos valores sorteados
for key, value in jogadores.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
# Codigo para ordenacao do dicionario por valor
jogadores_ordenados = {k: v for k, v in sorted(jogadores.items(), key=lambda item: item[1], reverse=True)}
c = 0
for key, value in jogadores_ordenados.items():
    print(f'{c+1:>4}º lugar: {key} com {value}.')
    sleep(1)
    c += 1