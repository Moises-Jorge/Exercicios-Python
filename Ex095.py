'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
dados_jogador = dict()
lista_partidas = list()
lista_jogadores = list()
while True:
    dados_jogador['nome'] = str(input('Nome do Jogador: '))
    num_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou?: '))
    for c in range(num_partidas):
        lista_partidas.append(int(input(f'  Quanto gols na partida {c+1}?: ')))
    dados_jogador['gols'] = lista_partidas[:]
    dados_jogador['total'] = sum(lista_partidas)
    lista_jogadores.append(dados_jogador.copy())
    lista_partidas.clear()
    saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for k in dados_jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for indice, jogador in enumerate(lista_jogadores):
    print(f'{indice:>3} ', end='')
    for v in jogador.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    if opcao <= len(lista_jogadores) - 1:
        print(f'  -- LEVANTAMENTO DO JOGADOR {lista_jogadores[opcao]["nome"]}')
        for i, gol in enumerate(lista_jogadores[opcao]['gols']):
            print(f'     No jogo {i+1} fez {gol} gols.')
    else:
        print(f'ERRO! Nao existe jogador com codigo {opcao}!')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')