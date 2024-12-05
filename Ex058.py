''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos palpites Foram necessários para vencer. '''
from random import randint
num_pc = randint(0, 10)

print('Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10.\nSerah que voce consegue advinhar qual foi?')
num_user = int(input('Qual eh o seu palpite?: '))
tentativas = 0

while num_user != num_pc:
    if num_user < num_pc:
        num_user = int(input('Errado, Eh mais. Tente de novo: '))
    else:
        num_user = int(input('Errado, Eh menos. Tente de novo: '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabens!')
