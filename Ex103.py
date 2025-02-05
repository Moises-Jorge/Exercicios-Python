'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. '''
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
print('-' * 30)
nome_jogador = str(input('Nome do Jogador: '))
gols = str(input('Numero de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome_jogador.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome_jogador, gols)