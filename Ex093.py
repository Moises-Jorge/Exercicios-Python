'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feito durante o campeonato.'''
dados_jogador = dict()
lista_partidas = list()
dados_jogador['nome'] = str(input('Nome do Jogador: '))
num_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou?: '))
for c in range(num_partidas):
    lista_partidas.append(int(input(f'  Quanto gols na partida {c}?: ')))
dados_jogador['gols'] = lista_partidas[:]
dados_jogador['total'] = sum(lista_partidas)
print('-=' * 30)
print(dados_jogador)
print('-=' * 30)
for k,v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados_jogador["nome"]} jogou {num_partidas} partidas.')
for indice, gol in enumerate(lista_partidas):
    print(f'  => Na partida {indice}, fez {gol} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')