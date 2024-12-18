''' Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
vitorias = 0
while True:
    print('=-' * 15)
    num_pessoa = int(input('Diga um valor: '))
    num_pc = randint(0, 10)
    resultado = num_pessoa + num_pc
    opcao = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    
    print('-' * 30)
    print(f'Voce jogou {num_pessoa} e o computador {num_pc}.', end='')
    print(f'Total deu {resultado} e DEU PAR' if resultado % 2 == 0 else f'Total deu {num_pessoa + num_pc} e DEU IMPAR')
    print('-' * 30)
    
    if resultado % 2 == 0 and opcao == 'P':
        print('Voce VENCEU!\nVamos jogar novamente...')
    elif resultado % 2 != 0 and opcao == 'I':
        print('Voce VENCEU!\nVamos jogar novamente...')
    else:
        print('Voce PERDEU!')
        break
    vitorias += 1
print('=-' * 15)
print(f'GAME OVER! Voce venceu {vitorias} vezes.')